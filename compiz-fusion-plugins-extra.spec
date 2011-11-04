%define name compiz-fusion-plugins-extra
%define newname compiz-plugins-extra
%define version 0.8.6
%define rel 3

Summary: Compiz Fusion Main Plugin Set for compiz
Name: %{name}
Version: %{version}
Release: %mkrel %rel
Source0: http://releases.compiz-fusion.org/%{version}/%{newname}-%{version}.tar.bz2
Patch0:  compiz-plugins-extra-0.8.6-libnotify0.7.patch
Patch1:  0001-Treat-screenlets-windows-as-widgets.patch
Patch2:  cubereflex-blue.patch
License: GPL
Group: System/X11
URL: http://www.compiz-fusion.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: dbus-devel
BuildRequires: compiz-devel >= %{version}
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: compiz-fusion-plugins-main-devel >= %{version}
BuildRequires: compiz-bcop
BuildRequires: libGConf2-devel
BuildRequires: MesaGLU-devel
BuildRequires: jpeg-devel
BuildRequires: pango-devel
BuildRequires: libnotify-devel
Requires: compiz

%description
This is the main plugin set from the Compiz Fusion community.

This is a combination of the Compiz Extras and Beryl communities

#----------------------------------------------------------------------------

%package devel
Summary: Development files for Compiz Fusion Extra Plugin Set for compiz
Group: Development/X11

%description devel
Development files for Compiz Fusion Extra Plugin Set for compiz

#----------------------------------------------------------------------------

%prep
%setup -qn %{newname}-%{version}
%patch0 -p0
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la -exec rm -f {} \;
%find_lang %{newname}

%clean
rm -rf %{buildroot}

#----------------------------------------------------------------------------

%files -f %{newname}.lang
%defattr(-,root,root)
%{_libdir}/compiz/lib*.a
%{_libdir}/compiz/lib*.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*.png


%files devel
%{_includedir}/compiz/*.h
%{_libdir}/pkgconfig/*.pc
