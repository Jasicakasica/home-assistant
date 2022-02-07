#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : home-assistant
Version  : 2022.2.3
Release  : 314
URL      : https://github.com/home-assistant/home-assistant/archive/2022.2.3/home-assistant-2022.2.3.tar.gz
Source0  : https://github.com/home-assistant/home-assistant/archive/2022.2.3/home-assistant-2022.2.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: home-assistant-bin = %{version}-%{release}
Requires: home-assistant-license = %{version}-%{release}
Requires: home-assistant-python = %{version}-%{release}
Requires: home-assistant-python3 = %{version}-%{release}
Requires: gTTS-token
Requires: libstoragemgmt-python3
Requires: mutagen
Requires: pypi(aiohttp)
Requires: pypi(aiohttp_cors)
Requires: pypi(atomicwrites)
Requires: pypi(awesomeversion)
Requires: pypi(bcrypt)
Requires: pypi(ciso8601)
Requires: pypi(cryptography)
Requires: pypi(distro)
Requires: pypi(envs)
Requires: pypi(eternalegypt)
Requires: pypi(home_assistant_frontend)
Requires: pypi(httpx)
Requires: pypi(importlib_metadata)
Requires: pypi(jinja2)
Requires: pypi(netdisco)
Requires: pypi(pyjwt)
Requires: pypi(pyotp)
Requires: pypi(pyqrcode)
Requires: pypi(python_slugify)
Requires: pypi(ruamel.yaml)
Requires: pypi(sqlalchemy)
Requires: pypi(ua_parser)
Requires: pypi(user_agents)
Requires: pypi(voluptuous)
Requires: pypi(voluptuous_serialize)
Requires: pypi(xmltodict)
Requires: pypi(zeroconf)
Requires: python-openzwave
BuildRequires : buildreq-distutils3
BuildRequires : pypi(aiohttp)
BuildRequires : pypi(astral)
BuildRequires : pypi(async_timeout)
BuildRequires : pypi(atomicwrites)
BuildRequires : pypi(attrs)
BuildRequires : pypi(awesomeversion)
BuildRequires : pypi(bcrypt)
BuildRequires : pypi(certifi)
BuildRequires : pypi(ciso8601)
BuildRequires : pypi(cryptography)
BuildRequires : pypi(httpx)
BuildRequires : pypi(ifaddr)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(pip)
BuildRequires : pypi(pyjwt)
BuildRequires : pypi(python_slugify)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(sqlalchemy)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi(voluptuous)
BuildRequires : pypi(voluptuous_serialize)
BuildRequires : pypi(wheel)
BuildRequires : pypi(yarl)

%description
Home Assistant |Chat Status|
=================================================================================

%package bin
Summary: bin components for the home-assistant package.
Group: Binaries
Requires: home-assistant-license = %{version}-%{release}

%description bin
bin components for the home-assistant package.


%package license
Summary: license components for the home-assistant package.
Group: Default

%description license
license components for the home-assistant package.


%package python
Summary: python components for the home-assistant package.
Group: Default
Requires: home-assistant-python3 = %{version}-%{release}

%description python
python components for the home-assistant package.


%package python3
Summary: python3 components for the home-assistant package.
Group: Default
Requires: python3-core
Requires: pypi(aiohttp)
Requires: pypi(astral)
Requires: pypi(async_timeout)
Requires: pypi(atomicwrites)
Requires: pypi(attrs)
Requires: pypi(awesomeversion)
Requires: pypi(bcrypt)
Requires: pypi(certifi)
Requires: pypi(ciso8601)
Requires: pypi(cryptography)
Requires: pypi(httpx)
Requires: pypi(ifaddr)
Requires: pypi(jinja2)
Requires: pypi(pip)
Requires: pypi(pyjwt)
Requires: pypi(python_slugify)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(typing_extensions)
Requires: pypi(voluptuous)
Requires: pypi(voluptuous_serialize)
Requires: pypi(yarl)

%description python3
python3 components for the home-assistant package.


%prep
%setup -q -n core-2022.2.3
cd %{_builddir}/core-2022.2.3

%build
## build_prepend content
sed -i 's/==/>=/g' setup.py
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644247931
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/home-assistant
cp %{_builddir}/core-2022.2.3/LICENSE.md %{buildroot}/usr/share/package-licenses/home-assistant/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hass

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/home-assistant/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
