%global _empty_manifest_terminate_build 0
Name:           python-geomet
Version:        0.3.0
Release:        1
Summary:        GeoJSON <-> WKT/WKB conversion utilities
License:        Apache-2.0
URL:            https://github.com/geomet/geomet
Source0:        https://files.pythonhosted.org/packages/be/9c/dc5a874b12bbab2981edf92d7d03b9d37de6261655b57590a166c890b148/geomet-0.3.0.tar.gz
BuildArch:      noarch
%description
Convert GeoJSON to WKT/WKB (Well-Known Text/Binary), and vice versa.

%package -n python3-geomet
Summary:        GeoJSON <-> WKT/WKB conversion utilities
Provides:       python-geomet
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-click
BuildRequires:  python3-six
# General requires
Requires:       python3-click
Requires:       python3-six
%description -n python3-geomet
Convert GeoJSON to WKT/WKB (Well-Known Text/Binary), and vice versa.

%package help
Summary:        GeoJSON <-> WKT/WKB conversion utilities
Provides:       python3-geomet-doc
%description help
Convert GeoJSON to WKT/WKB (Well-Known Text/Binary), and vice versa.

%prep
%autosetup -n geomet-0.3.0 -p1

%build
%py3_build


%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
%{__python3} setup.py test

%files -n python3-geomet -f filelist.lst
%dir %{python3_sitelib}/*


%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon Sep 19 2022 hkgy <kaguyahatu@outlook.com> - 0.3.0-1
- Update to 0.3.0

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 0.2.1.post1-2
- DESC: delete -S git from %autosetup

* Tue Jul 13 2021 OpenStack_SIG <openstack@openeuler.org> - 0.2.1.post1-1
- Package Spec generate
