%define deb_opera %{name}-stable_%{version}_amd64.deb

Summary: Opera Stable
Name: opera
Version: 28.0.1750.40
Release: 28
License: Proprietary
Group: Applications/Internet
URL: http://get.geo.opera.com/pub/opera-stable/
Source0: http://get.geo.opera.com/pub/opera-stable/%{version}/linux/%{deb_opera}
Vendor: Opera Software ASA
Packager: Nobuyuki Ito
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: x86_64
Requires: systemd
BuildRequires: binutils xz tar systemd
Provides: libudev.so.0()(64bit)

%description
Opera Stable

%prep

%setup -T -n %{name} -c

%build

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

# extract data from the deb package
ar p $RPM_SOURCE_DIR/%{deb_opera} data.tar.xz | xz -d -9 | tar x -C $RPM_BUILD_ROOT

# rename libdir
mv $RPM_BUILD_ROOT/usr/lib/x86_64-linux-gnu/%{name} $RPM_BUILD_ROOT/usr/lib/
rm -rf $RPM_BUILD_ROOT/usr/lib/x86_64-linux-gnu
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT%{_libdir}

# create new symlink
rm -f $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -sr $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

# delete some directories that is not needed on Fedora
rm -rf $RPM_BUILD_ROOT%{_datadir}/{lintian}

# correct opera_sandbox permission
# FATAL:setuid_sandbox_client.cc(283)] The SUID sandbox helper binary was found, but is not configured correctly. Rather than run without sandboxing I'm aborting now. You need to make sure that /usr/lib64/opera-stable/opera_sandbox is owned by root and has mode 4755.
chmod 4755 $RPM_BUILD_ROOT%{_libdir}/%{name}/opera_sandbox

# create symlink to libudev.so
mkdir $RPM_BUILD_ROOT%{_libdir}/%{name}/lib
ln -sL %{_libdir}/libudev.so.1 $RPM_BUILD_ROOT%{_libdir}/%{name}/lib/libudev.so.0

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}
