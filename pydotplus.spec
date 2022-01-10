#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pydotplus
Version  : 2.0.2
Release  : 43
URL      : http://pypi.debian.net/pydotplus/pydotplus-2.0.2.tar.gz
Source0  : http://pypi.debian.net/pydotplus/pydotplus-2.0.2.tar.gz
Summary  : Python interface to Graphviz's Dot language
Group    : Development/Tools
License  : MIT
Requires: pydotplus-license = %{version}-%{release}
Requires: pydotplus-python = %{version}-%{release}
Requires: pydotplus-python3 = %{version}-%{release}
Requires: pypi(pyparsing)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyparsing)

%description
PyDotPlus - Python interface to Graphviz's Dot language
        =======================================================

%package license
Summary: license components for the pydotplus package.
Group: Default

%description license
license components for the pydotplus package.


%package python
Summary: python components for the pydotplus package.
Group: Default
Requires: pydotplus-python3 = %{version}-%{release}

%description python
python components for the pydotplus package.


%package python3
Summary: python3 components for the pydotplus package.
Group: Default
Requires: python3-core
Provides: pypi(pydotplus)
Requires: pypi(pyparsing)

%description python3
python3 components for the pydotplus package.


%prep
%setup -q -n pydotplus-2.0.2
cd %{_builddir}/pydotplus-2.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641845553
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pydotplus
cp %{_builddir}/pydotplus-2.0.2/LICENSE %{buildroot}/usr/share/package-licenses/pydotplus/4118ca520dc186a23cda774e2abd6e6aabab218c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pydotplus/4118ca520dc186a23cda774e2abd6e6aabab218c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
