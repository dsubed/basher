Name:       basher
Version:    %{version}
Release:    %(echo `date +%Y%m%d%H%M`)
Summary:    RPM package for %{name}
License:    mit
Requires:   bash 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A linkin script to ,make it easy to override or create new global aliases in bash simple make symbolic links to the verrsions you want to use

%install
rm -rf %{buildroot}
cp -r %{_sourcedir}/* %{buildroot}

%files
/usr/local/bin/viruschecker

%changelog
* Mon Sep 21 2026 Linus Larsson linus.larsson@smhi.se
- First package
