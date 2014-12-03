opera-developer-fedora
======================
### How to Create RPM for OpenSUSE

# download .deb package file from Opera repository
wget http://get.geo.opera.com/pub/opera-developer/<i>version</i>/linux/opera-developer_<i>version</i>_amd64.deb

<i>e.g.</i> wget http://get.geo.opera.com/pub/opera-developer/24.0.1543.0/linux/opera-developer_24.0.1543.0_amd64.deb

# download .deb package file from Ubuntu repository
Check http://packages.ubuntu.com/trusty-updates/libssl1.0.0

wget http://<i>example.com/somewhere</i>

# build rpm package
rpmbuild -bb opera-developer.spec

# install rpm
yum localinstall opera-developer-*.x86_64.rpm

# start to use opera developer
Just click icon or

$ /usr/bin/opera-developer

# screenshot
- Fedora20

https://twitter.com/nobuyuki_ito/status/483313816810180608/
