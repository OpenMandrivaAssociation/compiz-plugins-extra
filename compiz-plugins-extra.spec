%define _disable_ld_no_undefined 1
%define oldname compiz-fusion-plugins-extra

Summary: Compiz Main Plugin Set for compiz
Name: compiz-plugins-extra
Version: 0.9.7.0
Release: 1
Source0: http://releases.compiz.org/%{version}/%{name}-%{version}.tar.bz2
Patch1:  0001-Treat-screenlets-windows-as-widgets.patch
License: GPL
Group: System/X11
URL: http://www.compiz.org/

BuildRequires: cmake
BuildRequires: xsltproc
BuildRequires: intltool
BuildRequires: boost-devel
BuildRequires: compiz-devel >= %{version} compiz
BuildRequires: compiz-plugins-main-devel >= %{version}
BuildRequires: mesaglu-devel
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(pangocairo)
Requires: compiz
%rename %{oldname}

%description
This is the main plugin set from the Compiz community. This is a 
combination of the Compiz Extras and Beryl communities

Contains: 3d addhelper animationaddon bench bicubic crashhandler cubeaddon
extrawm fadedesktop firepaint gears group loginout maximumize mblur reflex
scalefilter shelf showdesktop showmouse splash trailfocus widget.

#----------------------------------------------------------------------------

%package devel
Summary: Development files for Compiz Extra Plugin Set for compiz
Group: Development/X11
Requires: %{name} = %{version}-%{release}
%rename %{oldname}-devel

%description devel
Development files for Compiz Extra Plugin Set for compiz

#----------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p1

%build
%cmake \
	-DCOMPIZ_INSTALL_GCONF_SCHEMA_DIR=%{_sysconfdir}/gconf/schemas \
	-DCOMPIZ_DISABLE_SCHEMAS_INSTALL=TRUE \
	-DCOMPIZ_PACKAGING_ENABLED=TRUE

%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build
find %{buildroot} -name *.la -exec rm -f {} \;


%files
%{_sysconfdir}/gconf/schemas
%{_libdir}/compiz/*.so
%{_datadir}/compiz/*

%files devel
%{_includedir}/compiz/animationaddon
%{_libdir}/pkgconfig/*.pc

