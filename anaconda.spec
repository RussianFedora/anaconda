Name: anaconda
Version: 7.1
Release: 5.16
Copyright: GPL
Summary: The Red Hat Linux installation program.
Group: Applications/System
Source: anaconda-%{PACKAGE_VERSION}.tar.bz2
Source1: anaconda-powerpc.tar.gz
Patch0: anaconda-powerpc.patch
Patch1: anaconda-7.1-badswapfile.patch
Patch2: anaconda-7.1-genlocalelist.patch
Patch3: anaconda-7.1-stubs.patch
Patch4: anaconda-7.1-aboot.patch
Patch5: anaconda-7.1-axp-sonames.patch
Patch6: anaconda-7.1-cl544x.patch
Patch7: anaconda-7.1-alphaboot.patch
Patch8: anaconda-7.1-umask.patch
Patch9: anaconda-7.1-alphachanges.patch
Patch10: anaconda-7.1-gconv.patch
Patch11: anaconda-7.1-indivpkg-notraceback.patch
Patch12: anaconda-7.1-textdbg.patch
Patch13: anaconda-7.1-newrpm-build.patch
Patch14: anaconda-7.1-docbook-style.patch
Patch15: anaconda-7.1-ibmkernelnames.patch
Patch16: anaconda-7.1-deviseries.patch
Patch17: anaconda-7.1-rootonraid.patch
Patch18: anaconda-7.1-yaboot64initrd.patch
Patch19: anaconda-7.1-poptparse.patch
Patch20: anaconda-7.1-modutils.patch
Patch21: anaconda-7.1-ddblocksize.patch
Patch22: anaconda-7.1-iseriescdromeject.patch
Patch23: anaconda-7.1-nodriverdiskoniseries.patch

Obsoletes: anaconda-reconfig
BuildPreReq: pump-devel, kudzu-devel, pciutils-devel, bzip2-devel, e2fsprogs-devel, python-devel db3-devel gtk+-devel gnome-libs-devel
Prereq: chkconfig /etc/init.d
Requires: rpm-python
Excludearch: sparc sparc64

BuildRoot: /var/tmp/anaconda-%{PACKAGE_VERSION}

%description
The anaconda package contains portions of the Red Hat Linux
installation program which can then be run by the user for
reconfiguration and advanced installation options.

%package runtime
Summary: Red Hat Linux installer portions needed only for fresh installs.
Group: Applications/System
AutoReqProv: false
Requires: anaconda = %{version}-%{release}

%description runtime
The anaconda-runtime package contains parts of the Red Hat Linux
installer which are needed for installing new systems. These files are
used to build Red Hat Linux media sets, but are not meant for use on
already installed systems.

%prep

%setup -q -a 1
%ifarch ppc
%patch0 -p1 -b .ibm-mach1
%endif
%patch1 -p1 -b .badswapfile
%patch2 -p1 -b .utf8
%patch3 -p1 -b .stubs
%patch4 -p1 -b .aboot
%patch5 -p1 -b .axp
%patch6 -p1 -b .cl544x
%patch7 -p1 -b .alphaboot
%patch8 -p1 -b .umask
%patch9 -p1 -b .alphachanges
%patch10 -p1 -b .gconv
%patch11 -p1 -b .indivpkg
%patch12 -p1 -b .textdbg
%patch13 -p1 -b .newrpm
%patch14 -p1 -b .docbook
%patch15 -p1 -b .kernelnames
%patch16 -p1 -b .deviseries
%patch17 -p1 -b .raidroot
%patch18 -p1 -b .yaboot64initrd
%patch19 -p1 -b .poptparse
%patch20 -p1 -b .modutils
%patch21 -p1 -b .ddblksize
%patch22 -p1 -b .iseriescdromeject
%patch23 -p1 -b .noddoniseries

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
* Mon Jul 29 2002 Dave Lehman <dlehman@redhat.com>
- change block size for iSeries kernel dd from 4k to 32k (big speedup)
- don't try to eject cdrom on iSeries
- don't prompt for driver disk unless 'dd' cmdline arg given on iseries

* Wed Jul 17 2002 Dave Lehman <dlehman@redhat.com>
- prevent broken poptParseArgv from breaking kickstart parsing

* Tue Jul 16 2002 Dave Lehman <dlehman@redhat.com>
- fixed PReP detection with RAID root
- changes allowing for seperate kernel-iseries and kernel-pseries pkg
- change all references to /dev/iSeries to now refer to /dev/iseries
- prevent yaboot from trying to load an initrd with 64-bit vmlinux

* Mon Jul 8 2002 Dave Lehman <dlehman@redhat.com>
- upgraded to modutils-2.4.14

* Fri Apr 21 2001 Dave Lehman <dlehman@redhat.com>
- added IBM powerpc support (iSeries and pSeries only)

* Sun Apr  8 2001 Anaconda team <bugzilla@redhat.com>
- built new version from CVS

* Fri Jan 12 2001 Matt Wilson <msw@redhat.com>
- sync text with specspo

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

