#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6MimeTreeParserCore
%define devname %mklibname KPim6MimeTreeParserCore -d
%define wlibname %mklibname KPim6MimeTreeParserWidgets
%define wdevname %mklibname KPim6MimeTreeParserWidgets -d

Name: plasma6-mimetreeparser
Version:	24.08.0
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/mimetreeparser/-/archive/%{gitbranch}/mimetreeparser-%{gitbranchd}.tar.bz2#/mimetreeparser-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{ftpdir}/release-service/%{version}/src/mimetreeparser-%{version}.tar.xz
%endif
Summary: KDE library for handling MIME types
URL: https://kde.org/
License: GPL
Group: System/Libraries
Requires: %{libname} = %{EVRD}
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlCore)
BuildRequires: cmake(Qt6QmlNetwork)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6Mbox)
BuildRequires: cmake(KPim6Libkleo)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
BuildRequires: qt6-qtbase-theme-gtk3

%description
KDE library for handling MIME types

%package -n %{libname}
Summary: KDE library for handling MIME types
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for handling MIME types

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{wlibname}
Summary: KDE library for handling MIME types (Widgets)
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{wlibname}
KDE library for handling MIME types (Widgets)

%package -n %{wdevname}
Summary: Development files for %{name} (Widgets)
Group: Development/C
Requires: %{wlibname} = %{EVRD}
Requires: %{devname} = %{EVRD}

%description -n %{wdevname}
Development files (Headers etc.) for %{name} (Widgets).

%prep
%autosetup -p1 -n mimetreeparser-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang mimetreeparser6

%files -f mimetreeparser6.lang
%{_datadir}/qlogging-categories6/mimetreeparser.categories

%files -n %{libname}
%{_libdir}/libKPim6MimeTreeParserCore.so.*

%files -n %{wlibname}
%{_libdir}/libKPim6MimeTreeParserWidgets.so.*
%{_qtdir}/qml/org/kde/pim/mimetreeparser

%files -n %{devname}
%{_includedir}/KPim6/MimeTreeParserCore
%{_libdir}/cmake/KPim6MimeTreeParserCore
%{_qtdir}/mkspecs/modules/qt_MimeTreeParserCore.pri
%{_libdir}/libKPim6MimeTreeParserCore.so

%files -n %{wdevname}
%{_includedir}/KPim6/MimeTreeParserWidgets
%{_libdir}/cmake/KPim6MimeTreeParserWidgets
%{_qtdir}/mkspecs/modules/qt_MimeTreeParserWidgets.pri
%{_libdir}/libKPim6MimeTreeParserWidgets.so
