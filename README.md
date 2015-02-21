opera-opensuse
======================
### How to Create RPM for OpenSUSE

# Download .deb package

```bash
wget http://get.geo.opera.com/pub/opera-developer/<i>version</i>/linux/opera-developer_<i>version</i>_amd64.deb
wget http://get.geo.opera.com/pub/opera/desktop/<i>version</i>/linux/opera-stable_<i>version</i>_amd64.deb
```

For example,

```bash
wget http://get.geo.opera.com/pub/opera-developer/24.0.1543.0/linux/opera-developer_29.0.1770.1_amd64.deb
wget http://operasoftware.pc.cdn.bitgravity.com/pub/opera/desktop/27.0.1689.69/linux/opera-stable_27.0.1689.69_amd64.deb
``

# Build rpm package

```bash
rpmbuild -bb SPEC/opera-developer.spec
rpmbuild -bb SPEC/opera-stable.spec
```

# Install rpm

```bash
sudo rpm -i ~/rpmbuild/RPMS/opera*.x86_64.rpm
```

# Run

```bash
$ opera-developer
$ opera
```


Contributions
======================

Pull requests updating spec files into latest'n'greatest opere raleases are welcome.
