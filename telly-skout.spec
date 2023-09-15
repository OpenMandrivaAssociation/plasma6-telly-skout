%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200916
#define commit cc1ac2452e41873741c8b5f3fcafa29ae3ce5a30

Name:		telly-skout
Version:	23.08.1
Release:	%{?git:0.%{git}.}1
Summary:	TV Guide for Plasma Mobile
%if 0%{?git}
Source0:	https://invent.kde.org/plasma-mobile/telly-skout/-/archive/v%{version}/telly-skout-v%{version}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Feedback)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5UnitConversion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	pkgconfig(gmp)

%description
TV Guide for Plasma Mobile

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

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
