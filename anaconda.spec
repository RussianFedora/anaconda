Name: anaconda
Version: 7.0.1
Release: 9tc24
Copyright: GPL
Summary: The Red Hat Linux installer.
Group: Applications/System
Source: anaconda-%{PACKAGE_VERSION}.tar.gz
Obsoletes: anaconda-reconfig
BuildPreReq: pump-devel, kudzu-devel, pciutils-devel, bzip2-devel, e2fsprogs-devel, python-devel
Prereq: chkconfig /etc/init.d
Requires: rpm-python
ExcludeArch: sparc

BuildRoot: /var/tmp/anaconda-%{PACKAGE_VERSION}

%description
The anaconda package contains portions of the Red Hat Linux installer which
may be run be the user for reconfiguration and advanced installation
options.

%package runtime
Summary: Portions of the Red Hat Linux installer only needed for fresh installations.
Group: Applications/System
AutoReqProv: false
Requires: anaconda = %{version}-%{release}

%description runtime
The anaconda-runtime package contains parts of the Red Hat Linux install
which are needed for installing new systems. It is used to build Red Hat
Linux media sets, but the files it contains are not meant for us on
already installed systems.

%prep

%setup -q

%build
make depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
#strip $RPM_BUILD_ROOT/usr/sbin/ddcprobe

strip $RPM_BUILD_ROOT/usr/lib/anaconda/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%post
chkconfig --add reconfig

%preun
if [ $1 = 0 ]; then
	chkconfig --del reconfig
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/sbin/anaconda
/usr/sbin/anaconda-runrescue
/usr/share/anaconda/*
/usr/share/locale/*/*/*
/usr/lib/anaconda/*
%ifarch i386
/usr/sbin/ddcprobe
%endif

%config /etc/rc.d/init.d/reconfig

%files runtime
%defattr(-,root,root)
/usr/lib/anaconda-runtime

%define date    %(echo `LC_ALL="C" date +"%a %b %d %Y"`)

%changelog
* Sat Feb 10 2001 Jason Wilson <jwilson@redhat.com>
- Force to C locale on reconfig startup

* Thu Feb  5 2001 Jason Wilson <jwilson@redhat.com>
- Added libfont into install image

* Sun Jan 28 2001 Jason Wilson <jwilson@redhat.com>
- Give user option to re-specify the language whenever the GUI appears

* Wed Jan 17 2001 Jason Wilson <jwilson@redhat.com>
- Really changed default language back to English
- Changed default language back to English

* Tue Jan 16 2001 Jason Wilson <jwilson@redhat.com>
- CDROM boots fail to set fonts - lets try again

* Mon Jan 15 2001 Jason Wilson <jwilson@redhat.com>
- CDROM boots fail to set fonts - lets try again
- text mode still setting catalogues up wrong

* Fri Jan 12 2001 Jason Wilson <jwilson@redhat.com>
- still still trying to change default locale
- still trying to change default locale
- more updated locale definitions
- potential fix for NFS install

* Thu Jan 11 2001 Jason Wilson <jwilson@redhat.com>
- still trying to change default locale
- changed text mode installs to stay in English

* Tue Jan  9 2001 Jason Wilson <jwilson@redhat.com>
- trying to change default locale
- updated help text translations
- removed korean option

* Sun Jan  7 2001 Jason Wilson <jwilson@redhat.com>
- changed references of zh_TW to zh as help system strips to first two chars
- added more Chinese translations and some help text
- really updated lang-table-kon
- created Chinese specifc boot images
- attempt at Chinese text mode install

* Fri Jan  5 2001 Jason Wilson <jwilson@redhat.com>
- fixed korean lang-table definition
- updated translations for zh_TW locale

* Thu Jan  4 2001 Jason Wilson <jwilson@redhat.com>
- added korean fonts to install image
- added korean to lang-table and removed all but English and TC
- updated Traditional Chinese po translations

* Wed Oct 18 2000 Akira Tagoh <tagoh@redhat.com>
- changed a default timezone from English/NewYork to Asia/Tokyo.

* Wed Oct 18 2000 Adrian Havill <havill@redhat.com>
- added dbcs, fixed ja wordwrap with kon and text mode

* Tue Oct 17 2000 Anaconda team <bugzilla@redhat.com>
- built new version from CVS

* Thu Aug 10 2000 Matt Wilson <msw@redhat.com>
- build on alpha again now that I've fixed the stubs

* Wed Aug  9 2000 Michael Fulbright <drmike@redhat.com>
- new build

* Fri Aug  4 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- allow also subvendorid and subdeviceid in trimpcitable

* Fri Jul 14 2000 Matt Wilson <msw@redhat.com>
- moved init script for reconfig mode to /etc/init.d/reconfig
- move the initscript back to /etc/rc.d/init.d
- Prereq: /etc/init.d

* Thu Feb 03 2000 Michael Fulbright <drmike@redhat.com>
- strip files
- add lang-table to file list

* Wed Jan 05 2000 Michael Fulbright <drmike@redhat.com>
- added requirement for rpm-python

* Mon Dec 06 1999 Michael Fulbright <drmike@redhat.com>
- rename to 'anaconda' instead of 'anaconda-reconfig'

* Fri Dec 03 1999 Michael Fulbright <drmike@redhat.com>
- remove ddcprobe since we don't do X configuration in reconfig now

* Tue Nov 30 1999 Michael Fulbright <drmike@redhat.com>
- first try at packaging reconfiguration tool

