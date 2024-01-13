%define major 6
%define libname %mklibname KPim6MimeTreeParser
%define devname %mklibname KPim6MimeTreeParser -d

Name: plasma6-mimetreeparser
Version:	24.01.90
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/mimetreeparser-%{version}.tar.xz
Summary: KDE library for handling MIME types
URL: http://kde.org/
License: GPL
Group: System/Libraries
Requires: %{libname} = %{EVRD}
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Qml)
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

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

%prep
%autosetup -p1 -n mimetreeparser-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang mimetreeparser6

%files -f mimetreeparser6.lang

%files -n %{libname}
%{_libdir}/*.so*
%{_qtdir}/qml/org/kde/pim/mimetreeparser

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
%{_qtdir}/mkspecs/modules/qt_MimeTreeParserCore.pri
%{_qtdir}/mkspecs/modules/qt_MimeTreeParserWidgets.pri
