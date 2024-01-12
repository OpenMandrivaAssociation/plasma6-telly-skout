%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200916
#define commit cc1ac2462e41873741c8b6f3fcafa29ae3ce6a30

Name:		plasma6-telly-skout
Version:	24.01.90
Release:	%{?git:0.%{git}.}2
Summary:	TV Guide for Plasma Mobile
%if 0%{?git}
Source0:	https://invent.kde.org/plasma-mobile/telly-skout/-/archive/v%{version}/telly-skout-v%{version}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/telly-skout-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6UnitConversion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	pkgconfig(gmp)

%description
TV Guide for Plasma Mobile

%prep
%autosetup -p1 -n telly-skout-%{?git:master}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang telly-skout

%files -f telly-skout.lang
%{_bindir}/telly-skout
%{_datadir}/applications/org.kde.telly-skout.desktop
%{_datadir}/metainfo/org.kde.telly-skout.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.telly-skout.svg
