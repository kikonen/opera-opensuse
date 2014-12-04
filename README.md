opera-opensuse
======================
### How to Create RPM for OpenSUSE

# download .deb package file from Opera repository
wget http://get.geo.opera.com/pub/opera-developer/<i>version</i>/linux/opera-developer_<i>version</i>_amd64.deb
wget http://get.geo.opera.com/pub/opera/desktop/<i>version</i>/linux/opera-stable_<i>version</i>_amd64.deb

<i>e.g.</i> wget http://get.geo.opera.com/pub/opera-developer/24.0.1543.0/linux/opera-developer_24.0.1543.0_amd64.deb
<i>e.g.</i> wget http://get.geo.opera.com/pub/opera/desktop/26.0.1656.32/linux/opera-stable_26.0.1656.32_amd64.deb

# build rpm package
rpmbuild -bb opera-developer.spec
rpmbuild -bb opera.spec

# install rpm
rpm -i opera*.x86_64.rpm

# run
$ opera-developer
$ opera
