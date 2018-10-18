#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : home-assistant
Version  : 0.80.3
Release  : 26
URL      : https://github.com/home-assistant/home-assistant/archive/0.80.3.tar.gz
Source0  : https://github.com/home-assistant/home-assistant/archive/0.80.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: home-assistant-bin = %{version}-%{release}
Requires: home-assistant-license = %{version}-%{release}
Requires: home-assistant-python = %{version}-%{release}
Requires: home-assistant-python3 = %{version}-%{release}
Requires: PyJWT
Requires: aiohttp
Requires: aiohttp-cors
Requires: astral
Requires: async-timeout
Requires: envs
Requires: gTTS-token
Requires: libstoragemgmt-python3
Requires: mutagen
Requires: netdisco
Requires: ua-parser
Requires: user-agents
Requires: voluptuous
Requires: voluptuous-serialize
Requires: xmltodict
Requires: zeroconf
BuildRequires : SQLAlchemy
BuildRequires : async-timeout
BuildRequires : buildreq-distutils3

%description
Home Assistant |Build Status| |Coverage Status| |Chat Status| |Reviewed by Hound|
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

%description python3
python3 components for the home-assistant package.


%prep
%setup -q -n home-assistant-0.80.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539876180
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/home-assistant
cp LICENSE.md %{buildroot}/usr/share/package-licenses/home-assistant/LICENSE.md
python3 -tt setup.py build  install --root=%{buildroot}
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
/usr/share/package-licenses/home-assistant/LICENSE.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
