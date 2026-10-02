Summary:	Cross Platform Password Manager
Name:		keepassxc
Version:	2.7.12
Release:	%{?beta:0.%{beta}.}2
License:	GPLv2+
Group:		File tools
# Forked from dormant http://www.keepassx.org/
Url:		https://www.keepassxc.org/
%if ! 0%{?beta:1}
Source0:	https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz
%else
Source0:	https://github.com/keepassxreboot/keepassxc/archive/master/%{name}-%{version}-%{beta}.tar.gz
%endif
BuildRequires:		asciidoctor
BuildRequires:		cmake >= 3.10
BuildRequires:		ninja
BuildRequires:		qmake5
BuildRequires:		qt5-macros
BuildRequires:		cmake(Qt5Core)
BuildRequires:		cmake(Qt5Concurrent)
BuildRequires:		cmake(Qt5DBus)
BuildRequires:		cmake(Qt5Gui)
BuildRequires:		cmake(Qt5LinguistTools)
BuildRequires:		cmake(Qt5Network)
BuildRequires:		cmake(Qt5Svg)
BuildRequires:		cmake(Qt5Widgets)
BuildRequires:		cmake(Qt5Test)
BuildRequires:		cmake(Qt5X11Extras)
BuildRequires:		pkgconfig(botan-3)
BuildRequires:		pkgconfig(libargon2)
BuildRequires:		pkgconfig(libgcrypt)
BuildRequires:		pkgconfig(libqrencode)
BuildRequires:		pkgconfig(libsodium)
## The following two BuildRequires added for yubikey support
BuildRequires:		pkgconfig(libpcsclite)
BuildRequires:		pkgconfig(libusb)
BuildRequires:		pkgconfig(minizip)
BuildRequires:		pkgconfig(readline)
BuildRequires:		pkgconfig(xi)
BuildRequires:		pkgconfig(xtst)
BuildRequires:		pkgconfig(zlib-ng)
Provides:	keepass = %{version}-%{release}
Provides:	KeePassX = %{version}-%{release}
Provides:	KeePassXC = %{version}-%{release}
%rename keepassx

%description
KeePassXC is a free/open-source password manager or safe which helps you to
manage your passwords in a secure way. You can put all your passwords in one
database, which is locked with one master key or a key-disk. So you only have
to remember one single master password or insert the key-disk to unlock the
whole database. The databases are encrypted using the best and most secure
encryption algorithms currently known (AES and Twofish).

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_bindir}/%{name}-proxy
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/org.%{name}.KeePassXC.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/org.%{name}.KeePassXC.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}*.*
%{_iconsdir}/hicolor/*/mimetypes/*.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-cli.1*

#-----------------------------------------------------------------------------

%package cli
Summary:	CLI interface to the KeePassXC password manager
Group:		File tools

%description cli
Command Line Interface to the KeePassXC password manager.

#-----------------------------------------------------------------------------

%prep
%if 0%{?beta}
%autosetup -p1 -n %{name}-master
%else
%autosetup -p1
%endif
%cmake_qt5 -G Ninja \
	-DKEEPASSXC_BUILD_TYPE=Release \
	-DWITH_XC_AUTOTYPE:BOOL=ON \
	-DWITH_XC_YUBIKEY:BOOL=ON \
	-DWITH_XC_BROWSER:BOOL=ON \
	-DWITH_XC_BROWSER_PASSKEYS:BOOL=ON \
	-DWITH_XC_FDOSECRETS:BOOL=ON \
	-DWITH_XC_KEESHARE:BOOL=ON \
	-DWITH_XC_NETWORKING:BOOL=ON \
	-DWITH_XC_SSHAGENT:BOOL=ON \
	-DWITH_XC_UPDATECHECK:BOOL=OFF


%build
%ninja_build -C build


%install
%ninja_install -C build
