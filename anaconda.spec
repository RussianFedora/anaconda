Name: anaconda
Version: 7.1
Release: 5.19.4
Copyright: GPL
Summary: The Red Hat Linux installation program.
Group: Applications/System
Source: anaconda-%{PACKAGE_VERSION}.tar.bz2

# fonts, keymaps, etc. for powerpc
Source1: anaconda-powerpc.tar.gz

# hack. allows po regeneration
Source2: comps-master

# new pixmaps with (C) 2002
Source3: anaconda-7.1-pixmaps.tar.gz

# new NLS dirs (help, text-help, po) with updated text
Source4: anaconda-7.1-nls.tar.gz

# core patches to allow building on ppc
Patch0: anaconda-powerpc.patch

# patches 1-9 came from CVS
Patch1: anaconda-7.1-badswapfile.patch
Patch2: anaconda-7.1-genlocalelist.patch
Patch3: anaconda-7.1-stubs.patch
Patch4: anaconda-7.1-aboot.patch
Patch5: anaconda-7.1-axp-sonames.patch
Patch6: anaconda-7.1-cl544x.patch
Patch7: anaconda-7.1-alphaboot.patch
Patch8: anaconda-7.1-umask.patch
Patch9: anaconda-7.1-alphachanges.patch

# add new gconv stub from glibc-2.2.4-24
Patch10: anaconda-7.1-gconv.patch

# prevent traceback when "select all" pressed on empty package groups
Patch11: anaconda-7.1-indivpkg-notraceback.patch

# enable Ctl-Z debugging in TUI 
Patch12: anaconda-7.1-textdbg.patch

# new rpm library linkage (4.0.2 -> 4.0.4)
Patch13: anaconda-7.1-newrpm-build.patch

# docbook-style version is hardcoded in sgml
Patch14: anaconda-7.1-docbook-style.patch

# kernel-iseries, kernel-pseries
Patch15: anaconda-7.1-ibmkernelnames.patch

# s,/dev/iSeries,/dev/iseries,g
Patch16: anaconda-7.1-deviseries.patch

# allow yaboot installation when root is RAID
Patch17: anaconda-7.1-rootonraid.patch

# yaboot 1.3.6-1b cannot boot vmlinux w/ initrd on 64-bit systems
# -> no initrd on ppc64 for now (user can build zImage.initrd)
Patch18: anaconda-7.1-yaboot64initrd.patch

# poptParseArgv chokes on blank lines
Patch19: anaconda-7.1-poptparse.patch

# upgrade modutils to 2.4.14 (for ppc64 modules)
Patch20: anaconda-7.1-modutils.patch

# increase block size from 4k to 32k (speeds up iSeries kernel install)
Patch21: anaconda-7.1-ddblocksize.patch

# don't even call the cdrom eject ioctl on iSeries
Patch22: anaconda-7.1-iseriescdromeject.patch

# remove cdrom driver disk support for iSeries
Patch23: anaconda-7.1-nodriverdiskoniseries.patch

# Japanese help text, message file translations
Patch24: anaconda-7.1-japanese-xlations.patch

# hacks to allow Japanese for GUI install only
Patch25: anaconda-7.1-install-ja.patch

# rebuild help texts for all langs on build
Patch26: anaconda-7.1-makealllangs.patch

# bootdisks are not split into net/local on ppc
Patch27: anaconda-7.1-allinstallmethods.patch

# hacks for remote display
Patch28: anaconda-7.1-remotedisplay.patch

# fixes for RAID on iSeries
Patch29: anaconda-7.1-iseriesraid.patch

# fixes (read: hacks) for upgrade on iSeries (32-bit upgraded to 64-bit)
Patch30: anaconda-7.1-iseriesupgrade.patch

# actually scan for cdrom devs on iSeries
Patch31: anaconda-7.1-iseriescdrom.patch

# fix TUI firewall code to allow > 7 netdevs
Patch32: anaconda-7.1-manydevs.patch

# skip bootloader installation if no kernel installed (upgrades)
Patch33: anaconda-7.1-nokernel.patch

# make getFilename sufficiently generic as to get an arbitrary file w/ any method
Patch40: anaconda-7.1-getfilename.patch

# setup iSeries so that side A contains rescue image, B contains installed kernel
Patch41: anaconda-7.1-iseriesboot.patch

# more checks for pSeries partitioning, mount points
Patch50: anaconda-7.1-pseriesrootchecks.patch

# conditionalize bootdisk creation on presence of a floppy
Patch51: anaconda-7.1-nofloppy.patch

# manually load veth and pcnet32 so iSeries net devs work
Patch52: anaconda-7.1-forcemods.patch

# add veth to module-info
Patch60: anaconda-7.1-vethmod.patch

# kickstart bootloader patches for IBM eServers
Patch70: anaconda-7.1-kickstart.patch

# overwrite modules.conf on iSeries upgrade
Patch80: anaconda-7.1-iseriesupgrademods.patch

# German translations
Patch90: anaconda-7.1-german.patch

# include updated/translated text instead of patching/building every time
Patch91: anaconda-7.1-dontmakehelp.patch

# update Copyright date to 2002
Patch92: anaconda-7.1-copyright.patch

# increase rpm verbosity, redirect stdout,stderr to file
Patch100: anaconda-7.1-rpmdebug.patch

# allow iutil.setClock to call /sbin/hwclock on ppc (previously disabled)
Patch101: anaconda-7.1-ppchwclock.patch

# no Xtest for fbdev driver
Patch102: anaconda-7.1-nofbdevxtest.patch

# do not allow creation of RAID partitions or devices on iSeries
Patch103: anaconda-7.1-noiseriesraid.patch

# spawn a zvt for logging output on iSeries
Patch110: anaconda-7.1-iserieslog.patch

# spawn a shell when running on an iSeries
Patch111: anaconda-7.1-iseriesshell.patch

# extra logging for module loading/modules.conf creation
Patch120: anaconda-7.1-moddebug.patch

# updates to contents of scripts directory
Patch130: anaconda-7.1-scriptupdates.patch

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

%setup -q -a 1 -a 3 -a 4
mkdir comps
cp %SOURCE2 comps/ 
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
#%patch12 -p1 -b .textdbg
%patch13 -p1 -b .newrpm
#%patch14 -p1 -b .docbook
%patch15 -p1 -b .kernelnames
%patch16 -p1 -b .deviseries
%patch17 -p1 -b .raidroot
%patch18 -p1 -b .yaboot64initrd
%patch19 -p1 -b .poptparse
%patch20 -p1 -b .modutils
%patch21 -p1 -b .ddblksize
%patch22 -p1 -b .iseriescdromeject
%patch23 -p1 -b .noddoniseries
#%patch24 -p1 -b .japanese
%patch25 -p1 -b .install-ja
#%patch26 -p1 -b .makealllangs
%patch27 -p1 -b .allinstallmethods
%patch28 -p1 -b .remotedisplay
%patch29 -p1 -b .iseriesraid
%patch30 -p1 -b .iseriesupgrade
%patch31 -p1 -b .iseriescdrom
%patch32 -p1 -b .manydevs
%patch33 -p1 -b .nokernel
%patch40 -p1 -b .getfilename
%patch41 -p1 -b .iseriesboot
%patch50 -p1 -b .pseriesrootchecks
%patch51 -p1 -b .nofloppy
%patch52 -p1 -b .forcemods
%patch60 -p1 -b .vethmod
%patch70 -p1 -b .ibmks
%patch80 -p1 -b .iseriesupgrademods
%patch92 -p1 -b .copyright
#%patch90 -p1 -b .german
#%patch91 -p1 -b .nomake
#%patch100 -p1 -b .rpmdbg
%patch101 -p1 -b .ppchwclock
%patch102 -p1 -b .nofbdevxtest
%patch103 -p1 -b .noiseriesraid
#%patch110 -p1 -b .iserieslog
#%patch111 -p1 -b .iseriesshell
#%patch120 -p1 -b .dbgmods
%patch130 -p1 -b .07112002

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
* Thu Nov 14 2002 Dave Lehman <dlehman@redhat.com>
- po update for Japanese

* Thu Nov 07 2002 Dave Lehman <dlehman@redhat.com>
- update compose scripts
- remove mkfs verbosity patch

* Mon Nov 04 2002 Dave Lehman <dlehman@redhat.com>
- extra verbose logging during filesystem creation

* Fri Nov 01 2002 Dave Lehman <dlehman@redhat.com>
- actually apply the copyright patch this time

* Tue Oct 29 2002 Dave Lehman <dlehman@redhat.com>
- German NLS updates
- moved NLS changes and new ppc texts into a tarball
- don't apply patches to NLS (po, help)

* Thu Oct 24 2002 Dave Lehman <dlehman@redhat.com>
- reversed a stupid typo in anaconda-powerpc.patch

* Mon Oct 21 2002 Dave Lehman <dlehman@redhat.com>
- overwrite modules.conf on iSeries upgrade
- fixed nofloppy patch (#76436)
- updated ja.po from Akira Tagoh

* Fri Oct 18 2002 Dave Lehman <dlehman@redhat.com>
- revert a booboo in the noiseriesraid patch (gnomefsedit.c)
- kickstart fixes for IBM eServers

* Thu Oct 17 2002 Dave Lehman <dlehman@redhat.com>
- add veth to module-info
- don't apply textdbg, iserieslog patches

* Wed Oct 16 2002 Dave Lehman <dlehman@redhat.com>
- force load of veth.o as probeDevices fails to setup veths

* Tue Oct 15 2002 Dave Lehman <dlehman@redhat.com>
- conditionalize bootdisk, etc. on presence of a floppy drive
- add patches for log, shell consoles on iSeries

* Wed Oct 9 2002 Dave Lehman <dlehman@redhat.com>
- update copyright statements to say (C) 2002
- fixed a broken check in pseriesrootchecks patch

* Wed Oct 2 2002 Dave Lehman <dlehman@redhat.com>
- add checks for '/' on primary, '/' on same disk as PReP (for pSeries)

* Fri Sep 27 2002 Dave Lehman <dlehman@redhat.com>
- use addRamDisk instead of addinitrd on iSeries (doh!)
- allow getFilename to get any file in the tree
- new default boot setup on iseries (A side: rescue, B side: regular)

* Wed Sep 18 2002 Dave Lehman <dlehman@redhat.com>
- update modules.conf to reflect interface name changes on iSeries upgrade
- prevent RAID device/partition creation on iSeries
- prevent Xtest if fbdev is X driver (pSeries)
- make yaboot.install exit gracefully if no kernel installed on upgrade

* Tue Sep 17 2002 Dave Lehman <dlehman@redhat.com>
- fixed handling of > 7 net devices in firewall_text.py

* Mon Sep 16 2002 Dave Lehman <dlehman@redhat.com>
- fix iSeries cdrom detection for fstab, since kudzu doesn't do it
- Japanese PO update
- fix reading fstab on iSeries (need to *really* fix like i20/)

* Fri Sep 13 2002 Dave Lehman <dlehman@redhat.com>
- work around broken instClass on upgrade w/o cmdline arg
- update mk-images, mk-images.ppc
- fix iseries post-upgrade snafu

* Thu Sep 12 2002 Dave Lehman <dlehman@redhat.com>
- revert setClock change

* Thu Sep 12 2002 Dave Lehman <dlehman@redhat.com>
- prevent iutil.setClock from happening on ppc
- refine iSeries upgradeonly postAction hacks

* Fri Sep 6 2002 Dave Lehman <dlehman@redhat.com>
- iSeries upgrade from 32-bit distro hacks (/dev/iSeries,veth)

* Wed Aug 28 2002 Dave Lehman <dlehman@redhat.com>
- fix raidtab creation on iSeries ('/dev/iseries')

* Tue Aug 27 2002 Dave Lehman <dlehman@redhat.com>
- never try xmouse on iSeries, since if DISPLAY is set it's remote

* Mon Aug 26 2002 Dave Lehman <dlehman@redhat.com>
- unset DISPLAY if GUI installer startup fails or TUI is forced

* Fri Aug 16 2002 Dave Lehman <dlehman@redhat.com>
- added code to unset DISPLAY if netconfig fails for local install

* Tue Aug 13 2002 Dave Lehman <dlehman@redhat.com>
- added netconfig if display set and local method selected

* Mon Aug 12 2002 Dave Lehman <dlehman@redhat.com>
- hacked loader to _not_ set LANG, etc. or load catalogs or fonts for Japanese

* Wed Aug 7 2002 Dave Lehman <dlehman@redhat.com>
- hacked Makefiles to rebuild message catalogs, etc. during rpmbuild

* Tue Aug 6 2002 Dave Lehman <dlehman@redhat.com>
- added Japanese help text translations
- hacked loader to allow selection of ja_JP w/o loading it until anaconda
- updated ppc fonts

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

