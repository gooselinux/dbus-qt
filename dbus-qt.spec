
%define qt3pkg qt
%if 0%{?fedora} > 8 || 0%{?rhel} >= 6
%define qt3pkg qt3
%endif

Summary: Qt-based library for using D-BUS
Name:	 dbus-qt
Version: 0.70
Release: 7.2%{?dist}

License: AFL or GPLv2+
URL: 	 http://www.freedesktop.org/software/dbus/
Source0: http://ranger.befunk.com/fink/dbus-qt3-%{version}.tar.bz2
Group: 	 System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gettext
BuildRequires: libxml2-devel
BuildRequires: %{qt3pkg}-devel
BuildRequires: dbus-devel

%description
D-BUS add-on library to integrate the standard D-BUS library with
the Qt3 thread abstraction and main loop.

%package devel
Summary: Libraries and headers for %{name} 
Group:	 Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: dbus-devel
Requires: %{qt3pkg}-devel
%description devel
%{summary}.

%prep
%setup -q  -n dbus-qt3-%{version}


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh

%configure --disable-static

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT 

make install DESTDIR=$RPM_BUILD_ROOT

# Unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


%clean
rm -rf $RPM_BUILD_ROOT 


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files 
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libdbus-qt-*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/dbus-1.0/dbus/connection.h
%{_includedir}/dbus-1.0/dbus/message.h
%{_includedir}/dbus-1.0/dbus/server.h
%{_includedir}/dbus-1.0/dbus/dbus-qt.h
%{_libdir}/libdbus-qt-*.so

%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 0.70-7.2
- Rebuilt for RHEL 6
Related: rhbz#566527

* Fri Nov 13 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.70-7.1
- Fix conditional for RHEL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.70-5
- fix license tag

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.70-4
- s/qt-devel/qt3-devel/ (f9+)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.70-3
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Dennis Gilmore <dennis@ausil.us> 0.70-2
- rebuild for F8 and update license

* Tue Jan 30 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.70-1
- dbus-qt

* Tue Jun 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.62-2
- enable qt4 bindings
- BR: gettext

* Wed Jun 14 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.62-1
- 0.62

* Tue May 30 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.61-3
- Requires: dbus = %%version

* Mon May 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.61-2
- %%post/%%postun: /sbin/ldconfig

* Mon May 15 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.61-1
- first try

