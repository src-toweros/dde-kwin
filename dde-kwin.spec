%global sname deepin-kwin

Name:           dde-kwin
Version:        5.0.13+c1
Release:        6
Summary:        KWin configuration for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{name}_%{version}.orig.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kwin-devel
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  gsettings-qt-devel
BuildRequires:  libepoxy-devel
BuildRequires:  dtkcore-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  cmake(KDecoration2)
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  dtkgui-devel
BuildRequires:  kf5-ki18n-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       dde-qt5integration%{?_isa}
Requires:       kwin%{?_isa} >= 5.15
Obsoletes:      deepin-wm <= 1.9.38
Obsoletes:      deepin-wm-switcher <= 1.1.9
Obsoletes:      deepin-metacity <= 3.22.24
Obsoletes:      deepin-metacity-devel <= 3.22.24
Obsoletes:      deepin-mutter <= 3.20.38
Obsoletes:      deepin-mutter-devel <= 3.20.38

Requires:       kf5-kconfig-core
Requires:       kf5-kcoreaddons
Requires:       kf5-kglobalaccel-libs
Requires:       kf5-ki18n
Requires:       kf5-kwindowsystem
Requires:       kdecoration

%description
This package provides a kwin configuration that used as the new WM for Deepin
Desktop Environment.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kwin-devel%{?_isa}
Requires:       qt5-qtx11extras-devel%{?_isa}
Requires:       gsettings-qt-devel%{?_isa}
Requires:       dtkcore-devel%{?_isa}
Requires:       kf5-kglobalaccel-devel%{?_isa}


%description devel
Header files and libraries for %{sname}.

%prep
%setup -q -n %{name}-%{version}
sed -i 's:/lib:/%{_lib}:' plugins/kwin-xcb/lib/CMakeLists.txt
sed -i 's:/usr/lib:%{_libdir}:' plugins/kwin-xcb/plugin/main.cpp
sed -i 's:/usr/lib:%{_libexecdir}:' deepin-wm-dbus/deepinwmfaker.cpp

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DKWIN_VERSION=$(rpm -q --qf '%%{version}' kwin-devel) .
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
chmod 755 %{buildroot}%{_bindir}/kwin_no_scale

%ldconfig_scriptlets

%files
%doc CHANGELOG.md
%license LICENSE
%{_sysconfdir}/xdg/*
%{_bindir}/deepin-wm-dbus
%{_bindir}/kwin_no_scale
%{_libdir}/libkwin-xcb.so.*
%{_qt5_plugindir}/org.kde.kdecoration2/libdeepin-chameleon.so
%{_qt5_plugindir}/platforms/lib%{name}-xcb.so
%{_datadir}/dde-kwin-xcb/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/kwin/scripts/*
%{_datadir}/kwin/tabbox/*
%{_libdir}/qt5/plugins/kwin/effects/plugins/libblur.so
%{_libdir}/qt5/plugins/kwin/effects/plugins/libmultitasking.so
%{_libdir}/qt5/plugins/kwin/effects/plugins/libscissor-window.so


%files devel
%{_libdir}/libkwin-xcb.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}

%changelog
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.0.13+c1-6
- Package init
