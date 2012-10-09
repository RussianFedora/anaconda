%define livearches %{ix86} x86_64 ppc ppc64

Summary: Graphical system installer
Name:    anaconda
Version: 18.14
Release: 1%{?dist}
License: GPLv2+
Group:   Applications/System
URL:     http://fedoraproject.org/wiki/Anaconda

# To generate Source0 do:
# git clone http://git.fedorahosted.org/git/anaconda.git
# git checkout -b archive-branch anaconda-%{version}-%{release}
# ./autogen.sh
# make dist
Source0: %{name}-%{version}.tar.bz2
Patch0:	anaconda-18.8-rfremixify.patch
Patch1:	anaconda-18.8-fix-hardcoded-product-name.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%define dmver 1.02.17-6
%define gettextver 0.11
%define genisoimagever 1.1.9-4
%define gconfversion 2.28.1
%define intltoolver 0.31.2-3
%define libnlver 1.0
%define libselinuxver 1.6
%define pykickstartver 1.99.18
%define rpmpythonver 4.2-0.61
%define slangver 2.0.6-2
%define yumver 3.4.3-32
%define partedver 1.8.1
%define pypartedver 2.5-2
%define pythonpyblockver 0.45
%define e2fsver 1.41.0
%define nmver 1:0.7.1-3.git20090414
%define dbusver 1.2.3
%define createrepover 0.4.7
%define yumutilsver 1.1.11-3
%define iscsiver 6.2.0.870-3
%define pythoncryptsetupver 0.1.1
%define mehver 0.15-1
%define sckeyboardver 1.3.1
%define libblkidver 2.17.1-1
%define fcoeutilsver 1.0.12-3.20100323git

BuildRequires: audit-libs-devel
BuildRequires: bzip2-devel
BuildRequires: device-mapper-devel >= %{dmver}
BuildRequires: e2fsprogs-devel >= %{e2fsver}
BuildRequires: elfutils-devel
BuildRequires: gettext >= %{gettextver}
BuildRequires: gtk3-devel
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel
BuildRequires: glade-devel
BuildRequires: pygobject3
BuildRequires: intltool >= %{intltoolver}
BuildRequires: libarchive-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libXxf86misc-devel
BuildRequires: libblkid-devel >= %{libblkidver}
BuildRequires: libcurl-devel
BuildRequires: libgnomekbd-devel
BuildRequires: libnl-devel >= %{libnlver}
BuildRequires: libselinux-devel >= %{libselinuxver}
BuildRequires: libsepol-devel
BuildRequires: libxklavier-devel
BuildRequires: libxml2-python
BuildRequires: newt-devel
BuildRequires: pango-devel
BuildRequires: pykickstart >= %{pykickstartver}
BuildRequires: python-devel
BuildRequires: python-pyblock >= %{pythonpyblockver}
BuildRequires: python-urlgrabber >= 3.9.1-5
BuildRequires: python-nose
BuildRequires: rpm-devel
BuildRequires: rpm-python >= %{rpmpythonver}
BuildRequires: slang-devel >= %{slangver}
BuildRequires: transifex-client
BuildRequires: xmlto
BuildRequires: yum >= %{yumver}
BuildRequires: zlib-devel
BuildRequires: NetworkManager-devel >= %{nmver}
BuildRequires: NetworkManager-glib-devel >= %{nmver}
BuildRequires: dbus-devel >= %{dbusver}
BuildRequires: dbus-python
%ifarch %livearches
BuildRequires: desktop-file-utils
%endif
BuildRequires: iscsi-initiator-utils-devel >= %{iscsiver}
%ifarch s390 s390x
BuildRequires: s390utils-devel
%endif

Requires: anaconda-widgets = %{version}-%{release}
Requires: gnome-icon-theme-symbolic
Requires: python-meh >= %{mehver}
Requires: policycoreutils
Requires: rpm-python >= %{rpmpythonver}
Requires: comps-extras
Requires: parted >= %{partedver}
Requires: pyparted >= %{pypartedver}
Requires: yum >= %{yumver}
Requires: libxml2-python
Requires: python-urlgrabber >= 3.9.1-5
Requires: system-logos
Requires: pykickstart >= %{pykickstartver}
Requires: device-mapper >= %{dmver}
Requires: device-mapper-libs >= %{dmver}
Requires: dosfstools
Requires: e2fsprogs >= %{e2fsver}
Requires: gzip
Requires: libarchive
Requires: python-babel
%ifarch %{ix86} x86_64 ia64
Requires: dmidecode
%endif
Requires: python-pyblock >= %{pythonpyblockver}
Requires: libuser-python
Requires: newt-python
Requires: authconfig
Requires: system-config-firewall-base
Requires: cryptsetup-luks
Requires: python-cryptsetup >= %{pythoncryptsetupver}
Requires: mdadm
Requires: lvm2
Requires: util-linux >= 2.15.1
Requires: dbus-python
Requires: python-pwquality
Requires: python-bugzilla
Requires: python-nss
Requires: tigervnc-server-minimal
Requires: pytz
Requires: libxklavier
#libxklavier requires iso-codes, but does not have it as Requires: (see #813833)
Requires: iso-codes
Requires: libgnomekbd
%ifarch %livearches
Requires: usermode
Requires: zenity
%endif
Requires: createrepo >= %{createrepover}
Requires: squashfs-tools
%if ! 0%{?rhel}
Requires: hfsplus-tools
%endif
Requires: genisoimage >= %{genisoimagever}
Requires: GConf2 >= %{gconfversion}
%ifarch %{ix86} x86_64
Requires: syslinux >= 3.73
Requires: makebootfat
Requires: device-mapper
%endif
%ifarch s390 s390x
Requires: openssh
%endif
Requires: isomd5sum
Requires: yum-utils >= %{yumutilsver}
Requires: NetworkManager >= %{nmver}
Requires: nm-connection-editor
Requires: dhclient
Requires: anaconda-yum-plugins
Requires: libselinux-python >= %{libselinuxver}
Requires: fcoe-utils >= %{fcoeutilsver}
Requires: kbd
Requires: chrony
Requires: rdate
Requires: rsync
%ifarch %{sparc}
Requires: elftoaout piggyback
%endif
%ifarch x86_64
Requires: mactel-boot
%endif
Obsoletes: anaconda-images <= 10
Provides: anaconda-images = %{version}-%{release}
Obsoletes: anaconda-runtime < %{version}-%{release}
Provides: anaconda-runtime = %{version}-%{release}
Obsoletes: booty

%description
The anaconda package contains the program which was used to install your
system.

%package widgets
Summary: A set of custom GTK+ widgets for use with anaconda
Group: System Environment/Libraries
Requires: pygobject3
Requires: python

%description widgets
This package contains a set of custom GTK+ widgets used by the anaconda installer.

%package widgets-devel
Summary: Development files for anaconda-widgets
Group: Development/Libraries
Requires: glade

%description widgets-devel
This package contains libraries and header files needed for writing the anaconda
installer.  It also contains Python and Glade support files, as well as
documentation for working with this library.

%package dracut
Summary: The anaconda dracut module
BuildArch: noarch
Requires: dracut >= 19
Requires: dracut-network
Requires: xz
Requires: pykickstart

%description dracut
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the anaconda
runtime on NFS/HTTP/FTP servers or local disks.

%prep
%setup -q
sed -i 's!Fedora!RFRemix!g' po/*.po
%patch0 -p1
%patch1 -p1

# Hack to regenerate gmo files
pushd po
rm -f po/*.gmo
for i in `ls *.po`; do
  msgfmt -o `echo $i | sed 's!.po!.gmo!'` $i
done
popd

%build
%configure --disable-static \
           --enable-introspection \
           --enable-gtk-doc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}

%ifarch %livearches
desktop-file-install --vendor="" --dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop
%else
%{__rm} -rf %{buildroot}%{_bindir}/liveinst %{buildroot}%{_sbindir}/liveinst
%endif

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%ifarch %livearches
%post
update-desktop-database &> /dev/null || :
%endif

%ifarch %livearches
%postun
update-desktop-database &> /dev/null || :
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%doc docs/command-line.txt
%doc docs/install-methods.txt
%doc docs/mediacheck.txt
/lib/systemd/system/*
/lib/systemd/system-generators/*
/lib/udev/rules.d/70-anaconda.rules
%{_bindir}/instperf
%{_sbindir}/anaconda
%{_sbindir}/handle-sshpw
%{_sbindir}/logpicker
%{_sbindir}/anaconda-cleanup-initramfs
%{_datadir}/anaconda
%{_prefix}/libexec/anaconda
%{_libdir}/python*/site-packages/pyanaconda/*
%{_libdir}/python*/site-packages/log_picker/*
%{_bindir}/analog
%{_bindir}/anaconda-cleanup
%ifarch %livearches
%{_bindir}/liveinst
%{_sbindir}/liveinst
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/*
%{_sysconfdir}/X11/xinit/xinitrc.d/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*
%endif

%files widgets
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{_libdir}/python*/site-packages/gi/overrides/*
%{_datadir}/anaconda/tzmapdata/*

%files widgets-devel
%{_libdir}/libAnacondaWidgets.so
%{_includedir}/*
%{_datadir}/glade/catalogs/AnacondaWidgets.xml
%{_datadir}/gtk-doc

%files dracut
%dir /usr/lib/dracut/modules.d/80%{name}
/usr/lib/dracut/modules.d/80%{name}/*

%changelog
* Tue Oct  9 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 18.14-1.R
- update to 18.14

* Mon Oct  8 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 18.13-1.R
- update to 18.13

* Fri Oct  5 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 18.12-1.R
- update to 18.12

* Tue Oct  2 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 18.11-1.R
- update to 18.11

* Thu Sep 27 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 18.10-1.R
- update to 18.10

* Mon Sep 24 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 18.8-2.R
- RFRemixify
- fix hardcoded names in fedora-welcome

* Thu Sep 20 2012 Kalev Lember <kalevlember@gmail.com> - 18.8-2
- Rebuilt with new libgladeui

* Fri Sep 14 2012 Chris Lumens <clumens@redhat.com> - 18.8-1
- Make sure the InstallOptionsNDialogs get the correct space labels. (clumens)
- Get rid of the big pause going from the storage spoke back to the hub.
  (clumens)
- Don't fail when making updates if the symlink already exists. (clumens)
- Make sure to set the default TZ in ksdata so the completed method works.
  (clumens)
- Allow creation of biosboot and prepboot partitions in the custom spoke.
  (dlehman)
- Hide removable disks containing install media from the custom spoke.
  (dlehman)
- Make the minimum size for custom spoke partitions 1MB. (dlehman)
- The return value of execWithRedirect is an integer. (dlehman)
- Only include following free space in partitions' max size. (dlehman)
- Handle btrfs volumes with a dataLevel of None. (dlehman)
- Handle newDevice partitions smaller than the default of 500MB. (#853125)
  (dlehman)
- Add underlines to the expander and encryption checkbox in custom
  partitioning. (clumens)
- Remember to mark an environment as selected in the store. (clumens)
- Rename the addon/environment store columns to make sense. (clumens)
- Use slightly less confusing labels for the various back buttons. (clumens)
- Add a property to SpokeWindow for setting the single button's label.
  (clumens)
- Rename the SpokeWindow's back button to just button. (clumens)
- Use the blocking read to avoid busy wait in TUI progress (msivak)
- Make progress hub spokes possible and move the root password there (msivak)
- Don't let user hit Add button if no new layouts are selected (vpodzime)
- Gtk.ListStore.iter_previous now returns new iterator (#849060) (vpodzime)
- Write storage configs after payload install for live installs. (#856836)
  (dlehman)
- Update the pot file for various important string changes. (clumens)
- Attempt to fix word wrapping issues with the betanag dialog (#853913).
  (clumens)
- CONTINUE -> BEGIN INSTALLATION (#856614). (clumens)
- Language selection should work the same as keyboard selection (#854570).
  (clumens)
- Fix ransom notes cycling. (clumens)
- Improve the clarity of the custom checkbutton label. (dlehman)
- Add error handling around significant ui-initiated storage operations.
  (dlehman)
- Improve error granularity slightly in automatic partitioning. (dlehman)
- Fix detection of preexisting md arrays again. (dlehman)
- Handle changes to sizes of predefined devices in custom spoke. (dlehman)
- Fix traceback when switching device type to BTRFS. (dlehman)
- Validate mountpoints in the add-a-mountpoint dialog. (dlehman)
- Tell 'lvm' that yes, we really, really want to remove PV (vpodzime)
- Use 250ms interval for installation progress updating (vpodzime)
- network spoke: hide for live CD and image installs (#854586) (rvykydal)
- Fixed luks_add_key() (jsafrane)
- Display a radio button next to the environment choices. (clumens)
- Update TODO list. (clumens)
- Set the busy spinning cursor while the UI is loading. (clumens)
- network spoke: add "No network devices available" status (rvykydal)
- network spoke: clear device info if no network devices are found (#853903)
  (rvykydal)
- fix root password setup (#855481) (bcl)
- Rewrite expand_langs to return more items (vpodzime)
- Don't try to setup X layouts in text installation (#852447) (vpodzime)
- Add UTF-8 enconding suffix to our language strings (#854688) (vpodzime)
- Require rsync (vpodzime)
- Don't rely on chrony.conf file being available (#854899) (vpodzime)
- Require chrony and rdate, because Anaconda needs them (#854899) (vpodzime)
- Use the real path to dracut-lib.sh (#851362) (jkeating)
- fixup live install (#853988, #854962) (bcl)
- Only check media if we really want it (#853404) (jkeating)
- Fix thinko in anaconda arg handling portion of multilib patch. (dlehman)
- Honor kickstart and command line switches to enable multilib. (dlehman)
- Quitting the live installer shouldn't reboot the system (#854904). (clumens)
- The kickstart language-related command is "lang", not "language". (clumens)
- Fix btrfs/lvm/raid kickstart installs (#853649). (clumens)
- Store "en" as the default, not "en_US". (clumens)
- Mark ksdata.*.execute invocations as another step (vpodzime)
- Reorder and comment options passed to rsync (vpodzime)
- Fix bug in writing keyboard configuration files (vpodzime)
- network spoke: require connection only for url and nfs methods (#853899)
  (rvykydal)
- Drop the addBase handling in anaconda - if you want a group, list a group.
  (notting)
- Don't depend on storage or instClass in EFIGRUB (pjones)
- Use self.stage1_device where appropriate in EFIGRUB. (pjones)
- Explicitly disable the rootpw lock (#853788) (jkeating)
- require nm-connection-editor (#854586) (bcl)
- Include packaging log in exception reports. (dlehman)
- Add Kazakh as a valid translation. (clumens)
- Deselect any existing environment when selecting a new one (#851510).
  (clumens)
- Use chvt command for tty switching (vpodzime)
- Use the disk's serial number instead of index as an ID. (clumens)
- Use the disk's ID for deleting from the shopping cart, not an index
  (#853798). (clumens)
- Use the F18_Partition class (#853593). (clumens)
- Remove anaconda.instLanguage object and language module (vpodzime)
- Remove lang-table and localeinfo.py (vpodzime)
- parse-kickstart: handle 'network --ipv6=auto ...' (wwoods)
- parse-kickstart: set IPV6INIT=yes when using ipv6 (#830434) (wwoods)
- Make TUI password spoke behave the same as it's GUI counterpart (msivak)
- Remove ROOT_PATH/etc/localtime before symlinking timezone (vpodzime)
- Continue post-installation steps even if writing NTP configuration fails
  (vpodzime)
- update transifex.txt for newui (bcl)
- Handle invalid spoke input (#853253) (jkeating)
- Remove unnecessary (and broken) import (#853576) (jkeating)
- Destroy the Add Mountpoint dialog when escape is pressed (#853058). (clumens)
- Keep the current spoke on top of the hub. (clumens)
- And then fix an assortment of non-packaging pylint errors, too. (clumens)
- Fix problems in the packaging module that pylint detected. (clumens)
- Update runpylint to find newui modules correctly. (clumens)
- Prevent duplicate mountpoint creation. (dlehman)
- If there's only one disk, select it by default. (dlehman)
- Evaulate growth potential for all reqs, even when allocating a fixed req.
  (dlehman)
- Do not honor partitions' disk attr when reallocating them. (dlehman)
- Set size is a safe max size for partitions. (dlehman)
- Set the ANACONDA udev property in the post-switchroot udevdb. (dlehman)
- Calculate size func kwargs at call time to pick up changes. (dlehman)
- Add support md devices and btrfs raid features in the custom spoke. (dlehman)
- Move the BTRFS options to last and remove unsupported options. (dlehman)
- Remove "Technology" ComboBoxes from device options for now. (dlehman)
- Tweak setContainerMembers to work with a defined md array. (dlehman)
- Add support for named md devices. (dlehman)
- Make sure a disk is partitioned before treating it as such. (#849707)
  (dlehman)
- Setup python path /after/ we've done updates (jkeating)
- Fix a string substitution think-o (jkeating)
- We now BuildRequires python-babel as well. (clumens)
- Update TODO list. (clumens)
- Only show groups in the UI if they have members that install by default
  (default or manadtory packages). (notting)
- Symlink /run/initramfs/inst.{updates,product} to /tmp (jkeating)
- Use shutil.move for replacing old config with the new one (vpodzime)
- Honor user's choice on NTP (ON/OFF) (vpodzime)
- Don't crash if someone gives us bad timezone (vpodzime)
- Use expand_langs to find matching language (LanguageSpoke) (vpodzime)
- Move expandLangs to localization module (vpodzime)
- Use Gtk.main_level() to check if main loop is already running (vpodzime)
- Move setup from ImagePayload to LiveImagePayload. (clumens)
- Avoid duplicates in the packages property. (clumens)
- Set a progress message when liveinst starts installing software. (clumens)
- Fix default definitions of some payload class methods. (clumens)
- Add a spaceRequired property for LiveImagePayload. (clumens)
- getDirSize should stay on a single filesystem, not look at submounts.
  (clumens)
- Don't look for existing installations on live devices. (clumens)
- We don't need image_file in the live payload. (clumens)
- Now that we're using rsync, the livecd and rootfs do not have to match.
  (clumens)
- Disable software selection and source spokes on live installs. (clumens)
- Fix args to LiveImagePayload.setup (#852272). (clumens)
- require anaconda-widgets (bcl)
- Handle already mounted optical devices (#851274) (jkeating)
- Return full device object of selected optical drive (jkeating)
- Add a method to determine if device is mounted (jkeating)
- anaconda-cleanup: fix DeviceTree args (bcl)
- Unset install_device if repo setup fails (jkeating)
- _peopleRepositoriesFilter -> _peopleRepositoriesFilterEntry (#852182).
  (clumens)
- on_*_changed callbacks take one argument, not two. (clumens)
- Use the correct icon size constant. (clumens)
- remove dead code (setMethodstr, expandFTPMethod) (wwoods)
- parse-kickstart: update some TODO comments (wwoods)
- parse-kickstart: simplify logging (wwoods)
- enable fastestmirror yum plugin (#849797) (bcl)
- networking: remove Network() object (rvykydal)
- networking: use ksdata.network.hostname instead of actual installer hostname
  (rvykydal)
- networking: consolidate writing/copying of configuration files (rvykydal)
- networking: 70-persistent-net.rules doesn't exist anymore. (rvykydal)
- networking: disable ipv6 directly in installed system config file (rvykydal)
- networking: mirror end-of-installation network config tweaks in ksdata.
  (rvykydal)
- networking: write configuration in doInstall (rvykydal)
- Add mounts before swaps so the default selection is a mount. (dlehman)
- Use MB if a new mountpoint size does not include a unit spec. (#850839)
  (dlehman)
- Correctly handle partitions with sizes smaller than 500MB. (#850839)
  (dlehman)
- Don't include removed devices in Storage.unusedDevices. (dlehman)
- Handle SameSizeSet growth trimming when all members are too large. (dlehman)
- Add several missing yum lock aqcuisitions. (#851212) (dlehman)
- Offer completions for new mountpoints. (dlehman)
- Add old_source checking for closest mirror and url methods too (#851336).
  (clumens)
- Revert "Only use mounted media that has repodata" (jkeating)
- Only use mounted media that has repodata (jkeating)
- _bootloaderClass -> bootloaderClass for some platforms (#848173). (clumens)
- Make the storage info bar clickable to reveal error messages. (clumens)
- Move the software-specific error message out of the DetailedErrorDialog
  class. (clumens)
- Add a gui password spoke (jkeating)
- Put traceback reports on a diet. (clumens)

* Wed Aug 22 2012 Chris Lumens <clumens@redhat.com> - 18.7-1
- Do another _main_window -> main_window change. (clumens)
- Mark the storage category title for translation. (clumens)
- _actions should be set up in the __init__ method. (clumens)
- Don't require hfs-tools on RHEL (#849987). (clumens)
- dracut: remove workarounds for broken splitsep() (wwoods)
- dracut: update Requires: in spec (wwoods)
- Use ksdata.timezone and timezone module instead of anaconda.timezone
  (vpodzime)
- Remove the last usage of the system-config-date in Anaconda (vpodzime)
- Add support for swap --hibernation on LVM (vpodzime)
- Don't rely on selection staying selected when doing crazy things to it
  (vpodzime)
- Replace nonexisting icon with an existing one (DatetimeSpoke) (vpodzime)
- integer out of range for L format code (hamzy)
- Network spoke: use chr() instead of str() to convert dbus.Byte (#849395)
  (rvykydal)
- verify package checksums against metadata (bcl)
- use F18_PartData for hibernation flag support. (bcl)
- fix Gtk import in software.py (bcl)
- dracut: fix rd.neednet use in parse-kickstart (#849672) (wwoods)
- parse-anaconda-net: Add missing semicolon for dhclient.conf (bcl)
- anaconda-modprobe: fix .ko removal (bcl)
- Only devices that already exist may be ISO install sources (#849482).
  (clumens)
- Use python-meh's MainExceptionWindow's main_window property (vpodzime)
- dracut: fix syntax error in parse-kickstart (wwoods)
- Show fstype as "Unknown" for devices with unrecognised formatting. (dlehman)
- BTRFS magic for custom spoke. (dlehman)
- The device type of preexisting devices cannot be changed. (dlehman)
- Revert old hack that disabled btrfs in the old ui. (dlehman)
- Use correct device instance when updating selector w/ new device. (dlehman)
- Fix a traceback when clicking on the summary in custom spoke. (dlehman)
- Move device size calculation and setting into DeviceFactory. (dlehman)
- Stop pretending btrfs subvols can have a size. (dlehman)
- Fix a typo in StorageDevice._setSize. (dlehman)
- dracut: add info about special variables to README (wwoods)
- dracut: fix invalid use of 'eth0' (wwoods)
- dracut: drop upgrade-specific hack (wwoods)
- dracut: set "$netif" correctly in initqueue/online scripts (wwoods)
- dracut: fix old-style static ip=xxx gw=yyy... (wwoods)
- dracut: import anaconda-lib.sh in pre-udev hook (wwoods)
- dracut: fix set_neednet so network comes up (#849672) (wwoods)
- dracut: drop save_netinfo (wwoods)
- move anaconda-modprobe to pre-udev hook, silence modprobe errors (wwoods)
- parse-kickstart: fix crash with PXE + ks=file: (#844478) (wwoods)
- parse-kickstart: clarify/refactor Network handling (wwoods)
- Actually create default ifcfg files (#849012) (rvykydal)
- Don't fail on write of nonexisting IfcfgFile(SimpleConfigFile) (#849012,
  #849095) (rvykydal)
- If dracut left the DVD mounted, don't try to remount it (#849152). (clumens)
- Add support for most device editing functions. (dlehman)
- Various fixes, cleanups, and added logging for the custom spoke. (dlehman)
- Work around some signal handling issues in the custom spoke. (dlehman)
- Make choosing an auto-selected page after refresh slightly less fallible.
  (dlehman)
- Raise an exception if a new device ends up with size 0. (dlehman)
- Split out logic to determine container based on factory and/or device.
  (dlehman)
- Allow adding disks to a container's disk set. (dlehman)
- Allow passing a device into newDevice for adjustment. (dlehman)
- Add PartitionFactory class so partitions don't need a separate code path.
  (dlehman)
- Add a convenience method for scheduling resize actions. (dlehman)
- Return early from doKickstartStorage if there are no disks selected.
  (dlehman)
- Remove isomd5sum-static from build requires (vpodzime)
- Don't rely on having some network devices available (vpodzime)
- Enlightbox mainExceptionWindow (vpodzime)
- Put mainExceptionWindow in a WindowGroup (vpodzime)
- Bump required yum version to get the environment code. (notting)
- Add a flag so we don't get spurious 'change' events from the treeview while
  we're setting up the UI. (notting)
- Wire in the new environment logic through the UI. (notting)
- Add a local method for exposing group visibility from the comps file.
  (notting)
- Add methods to yumpayload for handling environments. (notting)
- Add some nicer wording to the column heads in the software selection UI.
  (notting)
- Rename 'description' to 'groupDescription'. (notting)
- dracut: add README (wwoods)

* Thu Aug 16 2012 Chris Lumens <clumens@redhat.com> - 18.6-1
- Remove linuxrc.s390 (dcantrell)
- Source in url-lib.sh if we don't have it (#847831) (jkeating)
- parse-kickstart: add proc_cmdline (fix init_logger()) (wwoods)
- Remove the data/bootdisk directory tree. (clumens)
- Remove duplicate boot disk setting code (#848841). (clumens)
- Force authconfig to be installed on the target system (#848803). (clumens)

* Wed Aug 15 2012 Chris Lumens <clumens@redhat.com> - 18.5-1
- Mark/unmark some strings for translation, as appropriate. (clumens)
- Save the distro label into the right variable for retranslation. (clumens)
- Add custom widget files to POTFILES.in. (clumens)
- Fix attribution on common UI code. (clumens)
- don't set armMachine in class definition (bcl)
- libudev now has a version of .1 (hamzy)
- Load anaconda-lib.sh if necessary (jkeating)
- Use shell code to work around missing basename (jkeating)
- Enable text mode once again! (jkeating)
- Update text prompt to include c for continue (jkeating)
- Don't continue if incomplete spokes exist (jkeating)
- Return a bool for timezone completed property (jkeating)
- Add a text progress hub to do the install (jkeating)
- text based storage spoke. (jkeating)
- Allow updating tmux.conf via makeupdates. (clumens)
- Prevent yum messages from showing on tty (jkeating)
- Remove unused imports from the installclasses. (clumens)
- NoSuchGroup is provided by packaging now.  yuminstall is on the way out.
  (clumens)
- Set transaction color in case of multilib install. (clumens)
- Add selinux-specific RPM macro setup. (clumens)
- Add the user-agent to urlgrabber from the old yuminstall.py. (clumens)
- Fix inheritance problems with the gui *Spoke classes. (clumens)
- Only setup python-meh when doing graphical installs (jkeating)
- Call the correct method to schedule the screen (jkeating)
- Add a missing import of os (jkeating)
- Don't display indirect spokes in the hub (jkeating)
- Revert "Remove unncessary __init__ definition. (clumens)" (jkeating)
- Honor displayMode from kickstart files (jkeating)
- Merge master into newtui (jkeating)
- Remove the base_tests file for now (jkeating)
- Remove unused import of UIObject (jkeating)
- Fix up detailederror for new common UI code (jkeating)
- Translate the base text hub class (jkeating)
- Translate the base tui class strings (jkeating)
- Remove unncessary __init__ definition. (clumens) (jkeating)
- Translate some strings in the base tui spokes classes (jkeating)
- Always use collect directly from common (jkeating)
- Add comment headers to the new files (jkeating)
- Ad source files to POTFILES.in (msivak)
- Merge remote-tracking branch 'origin/master' into newtui (msivak)
- import localization stuff and use it to translate more strings (msivak)
- finish renaming _mainloop (msivak)
- Fix naming for data attribute and move the NormalSpoke.__init__ under the
  proper class (msivak)
- Improve documentation and add licensing headers (msivak)
- Add translations to the simpleline framework (msivak)
- Add translations to Password Spoke (msivak)
- Add elementary timezone spoke (msivak)
- Pass screen args argument to prompt and input methods + fix for run-text-
  spoke (msivak)
- Merge master into newtui (msivak)
- Add automake files for TUI (msivak)
- add couple of tests and fix write method of widget (newline added unwanted
  space) (msivak)
- add couple of tests and support for them (msivak)
- add documentation and comments to TUI classes (msivak)
- Add documentation to the simpleline library for TUI (msivak)
- Add the new Summary hub and Password TUI spokes + tools to test TUI stuff
  (msivak)
- Fix bits and pieces to make TUI hub and spoke model work + example Hub and
  Password spoke (msivak)
- Create common abstract classes usable for all types of UI (msivak)
- Create the base classes for TUI Hub and Spoke model (msivak)
- Make collect and part of UserInterface setup more generic (msivak)
- Text based UI framework core (msivak)

* Mon Aug 13 2012 Chris Lumens <clumens@redhat.com> - 18.4-1
- dracut: fix inst.ks.sendmac (#826657) (wwoods)
- dracut: suppress ks errors from missing %include (wwoods)
- dracut: add comment to run_kickstart() (wwoods)
- Remove unused writeKS methods. (clumens)
- Only show unused devices that haven't been removed/deleted. (dlehman)
- Don't unexpand already-expanded pages when trying to expand them again.
  (dlehman)
- Make parents of hidden devices appear to be leaves. (dlehman)
- Remove the right device name from the lvm filter when unhiding device.
  (dlehman)
- Take configured filesystems into account when checking package space.
  (dlehman)
- Make sure the ksdata autopart type matches the storage one. (dlehman)
- Base auto-generated name prefixes on productName, not device type. (dlehman)
- Remove shrink code that was a workaround for the old ui flow. (dlehman)
- Remove old ui progress args from devicelibs.btrfs. (dlehman)
- Make sure we allocate partitions and grow lvm as needed in kickstart.
  (dlehman)
- Streamline autopart request setup slightly. (dlehman)
- Make it possible to call setUpBootLoader safely at any time. (dlehman)
- Move setup of new partition weight arg to Storage.newPartition. (dlehman)
- Use a copy of the main Storage instance during custom partitioning. (dlehman)
- Track requested sizes of btrfs subvols. (dlehman)
- Add a method to retrieve a devicetree device by id number. (dlehman)
- Fix DiskLabel so it can be deep-copied. (dlehman)
- Add a method to produce a deep copy of a Storage instance. (dlehman)
- Fix subtraction for Size. (dlehman)
- Add support for creating device based on a top-down specification. (dlehman)
- Add size-set managers to keep a set of growable requests in sync. (dlehman)
- Add a function to estimate required disk space for an md array. (dlehman)
- Add a method to estimate disk space needs for a new logical volume. (dlehman)
- Add a convenience method for new btrfs subvols and drop subvol size args.
  (dlehman)
- Use the UEFI shim to load grub. (pjones)
- Check that Gtk.main is not already running before starting another one
  (vpodzime)
- With tmux, we no longer need to start up a shell during VNC installs.
  (clumens)
- We no longer need getkeymaps, mapshdr, or readmap. (clumens)
- Remove the last references to isysLoadKeymap. (clumens)
- remove Security class (bcl)
- replace lokkit for selinux settings (#815540) (bcl)
- tests: Add tests for new SimpleConfigFile features (bcl)
- tests: cleanup whitespace in simpleconfig_test.py (bcl)
- simpleconfig: rewrite to better support commented config files (bcl)
- If the anaconda process crashes, don't delete its window. (clumens)
- On interactive installs, default the root account to locked. (clumens)
- Make the keyboard layout test a big text area instead of a single line.
  (clumens)
- Remove our loadKeymap code from isys (vpodzime)
- Replace system-config-keyboard with our methods using ksdata.keyboard
  (vpodzime)
- A little fix of newui -> master merge (iscsi offload devices) (rvykydal)
- Require new version of python-meh (vpodzime)
- Modify kernelPackages to select the right kernel for ARM systems. (dmarlin)
- ARM: clean up the kernel selection to be consistent with the rest of the code
  (dennis)
- add command line option to set the arm platform. (dennis)
- Add support to determine the ARM processor variety and select the correct
  kernel to install. (dmarlin)
- TODO list updates. (clumens)
- Sent pot file updates to the master branch in transifex, not f17. (clumens)

* Fri Aug 03 2012 Chris Lumens <clumens@redhat.com> - 18.3-1
- New graphical user interface.
- Removed loader.

* Wed Apr 18 2012 Brian C. Lane <bcl@redhat.com> - 18.2-1
- Fixes from F17 branch

* Mon Apr 09 2012 Brian C. Lane <bcl@redhat.com> - 17.20-1
- make dev_is_mounted more reliable (wwoods)
- fix failure to run multiple udev-triggered jobs (#811008) (wwoods)

* Fri Apr 06 2012 Brian C. Lane <bcl@redhat.com> - 17.19-1
- copy installer image to RAM during upgrades (#810391) (wwoods)
- fix repo={hd,cdrom}:DEV:PATH (#810136) (wwoods)
- read flags using filename globs (bcl)
- Fix repo={http,ftp,nfs} (#810005) (wwoods)
- Fix "memcheck=0" (and other store_true boot args) (wwoods)
- write new options to zipl.conf (dan)

* Tue Apr 03 2012 Brian C. Lane <bcl@redhat.com> - 17.18-1
- Revert "Wait for device activation / "online" hook if rd.neednet is set"
  (bcl)
- Add missing os import to platform.py (bcl)

* Tue Apr 03 2012 Brian C. Lane <bcl@redhat.com> - 17.17-1
- Don't allow /usr as a separate partition (#804913) (clumens)
- use /sys/class/dmi instead of dmidecode (bcl)
- restore the GPT blacklist code (bcl)
- add virtio rsyslogd logging to anaconda (bcl)
- dracut/parse-kickstart: handle network --device=link (or none) (wwoods)
- dracut: fix kssendmac/inst.ks.sendmac (wwoods)
- Set ONBOOT=yes for at least one wired netdev by default (#806466) (wwoods)
- detect live backing device (#809342) (dlehman)
- Wait for device activation / "online" hook if rd.neednet is set (wwoods)
- Fix kickstart failure if ks is on the same disk as stage2 (wwoods)
- fix 'mount: Too many levels of symbolic links' error message (wwoods)
- support {stage2,repo}=.../path/to/file.img (#808499) (wwoods)
- dracut when_diskdev_appears: only run cmd once per device (wwoods)
- dracut: don't do kickstart twice, don't use root.info (wwoods)
- Don't use the bootloader config path to find the splash image (#807510)
  (pjones)

* Wed Mar 28 2012 Brian C. Lane <bcl@redhat.com> - 17.16-1
- makeupdates: install liveinst to /usr/sbin (bcl)
- liveinst: adjust updates path (#807397) (bcl)
- dracut: add missing spaces for module loading (#804522) (bcl)
- Don't set MALLOC_PERTURB_ when calling grub2-install. (workaround #806784)
  (pjones)

* Tue Mar 27 2012 Brian C. Lane <bcl@redhat.com> - 17.15-1
- make ks=file:... parse kickstart earlier (#806931) (wwoods)
- Let "root=..." override "repo=..." (wwoods)
- dracut cleanup: use consistent filenames for cmdline.d files (wwoods)
- fix "strsep: command not found" error with repo:hd:.. (#806966) (wwoods)
- load modules needed by Anaconda (#804522) (bcl)
- Fix nfs/nfsiso (NM handover problems / empty net.ifaces) (wwoods)
- Format PReP partition (hamzy)

* Thu Mar 22 2012 Brian C. Lane <bcl@redhat.com> - 17.14-1
- Revert "dracut: use /run/install/source for repodir" (bcl)
- Disable creation of btrfs filesystems aside from kickstart. (#787341)
  (dlehman)
- fix text mode KeyError crash (#804483) (wwoods)
- Default to text-mode if 'console=XXX' was provided (#804506) (wwoods)
- dracut startup: "Loading $product $version $arch installer..." (wwoods)
- fix nfsiso:...:/path/to/filename.iso (#804515) (wwoods)
- fix typo in makeupdates (bcl)
- makeupdates: add support for updating systemd services/targets (wwoods)
- disable warnings about boot options needing 'inst.XXX' (wwoods)
- Create default ifcfg-* for each interface (#804504, #804716) (wwoods)
- save ifcfg for every interface we bring up (wwoods)
- Let systemd handle terminal setup, fix possible race with NM (wwoods)
- Migrate PPC from Yaboot to Grub2 for Anaconda (hamzy)
- dracut: fix anaconda-netroot for inst.repo=nfsiso:.. (wwoods)
- dracut: accept inst.updates or updates for live.updates (wwoods)
- makeupdates: put files the right places (wwoods)
- dracut: use /run/install/source for repodir (wwoods)
- read args from 80kickstart.conf (bcl)

* Fri Mar 16 2012 Brian C. Lane <bcl@redhat.com> - 17.13-1
- anaconda.service Wants=NetworkManager.service (wwoods)
- make sure we save the network setup for any network device we used (wwoods)
- make sure parse-kickstart's ifcfg files get copied to the system (wwoods)
- fedora-import-state.service is in initscripts now (wwoods)
- Add flag to disable available-memory check (for debugging etc.) (wwoods)
- fix logic for setting set rd.{luks,dm,md,lvm}=0 (wwoods)
- fix run_kickstart for the non-repo case (wwoods)
- run_kickstart: go back to targeted cmdline parsing (wwoods)
- parse-kickstart: write ifcfg files for all net devs (wwoods)
- add the traditional anaconda dhcpclass (wwoods)
- cleanups and fixes for ksdevice/bootdev handling (wwoods)
- drop unused when_netdev_online function (wwoods)
- make run_kickstart re-parse the whole commandline (wwoods)
- set rd.{luks,dm,md,lvm}=0 unless the user says otherwise (wwoods)
- handle inst.* cmdline args correctly (bcl)
- fixup for syntax error in inst.ks/--kickstart patch (wwoods)
- set ANACONDA=1 udev property in the right place (wwoods)
- fix inst.ks handling in anaconda (wwoods)
- fixups: run ks early, don't repeat netroot (wwoods)
- fixup: "online" hook renamed "initqueue/online" upstream (wwoods)
- Quiet bash error message if (optional) treeinfo is missing (wwoods)
- a couple small cleanups/fixes for fedora-import-state.service (wwoods)
- anaconda-shell service tweaks (wwoods)
- add fedora-import-state.service (fix NFS root: #799989) (wwoods)
- anaconda-netroot.sh: make sure dracut writes out the ifcfg files (wwoods)
- Use "online" hook to handle anaconda network root devices (wwoods)
- Fetch network kickstarts from the "online" hook (wwoods)
- set wait_for_dev /dev/root in parse-anaconda-repo.sh (wwoods)
- fix find_runtime() and parse_kickstart() (wwoods)
- kickstart parsing fixups: keep running if parse fails (wwoods)
- handle more KickstartErrors (wwoods)
- anaconda-lib: make sure we only run when_*_online jobs once (wwoods)
- add missing newline to /tmp/ks.info (wwoods)
- don't source dracut-lib.sh twice (it causes crashes) (wwoods)
- kickstart: only wait for kickstart if we're actually fetching it (wwoods)
- fetch-kickstart-*: actually do run_kickstart (wwoods)
- python-deps: cleanups/comments (wwoods)
- replace pythondeps.sh with python-deps (python script) (wwoods)
- move parse-kickstart.py back to parse-kickstart (wwoods)
- Makefile.am: use dist_dracut_SCRIPTS to make scripts executable (wwoods)
- fix bad path for parse-kickstart.py (wwoods)
- refactor network handling (support ibft and ksdevice) (wwoods)
- update Makefile.am (wwoods)
- add fetch-kickstart-disk and fetch-kickstart-net (wwoods)
- make cd autoprobe catchall rule actually run for each device (wwoods)
- fix inst.repo=cdrom (wwoods)
- move deprecation warnings into parse-anaconda-options.sh (wwoods)
- add wait_for_kickstart() (wwoods)
- parse-kickstart updates (wwoods)
- anaconda-lib: rename check_isodir, add anaconda_live_root_dir (wwoods)
- anaconda-{nfs,disk}root updates (wwoods)
- split genrules into repo-genrules.sh and kickstart-genrules.sh (wwoods)
- minor parse cleanups for kickstart and repo (wwoods)
- improve handling of anaconda repo root stuff (wwoods)
- parse-kickstart: return filename, drop biospart junk (wwoods)
- make sure edd is loaded, if available (wwoods)
- Drop dmidecode binary, just cat /sys/class/dmi/id/product_serial (wwoods)
- dracut/anaconda-genrules.sh: add catch-all rule for autoprobing CDs (wwoods)
- add more kickstart code, shuffle genrules code around (wwoods)
- move disk_to_dev_path to anaconda-lib (wwoods)
- edit anaconda-urlroot status messages (wwoods)
- fix typo in anaconda-urlroot (wwoods)
- add anaconda-urlroot (handle inst.repo=[http|ftp]) (wwoods)
- whoops, forgot anaconda-lib.sh (wwoods)
- dracut: check for .buildstamp in /run/initramfs (wwoods)
- anaconda-dracut: make sure we execute pythondeps.sh (wwoods)
- dumb typo fix: "convertfs", not "covertfs" (wwoods)
- dracut: move to /usr/lib (wwoods)
- dracut: depend on "convertfs" module (wwoods)
- Make anaconda-dracut subpackage noarch (wwoods)
- Add anaconda dracut module [WIP!] (wwoods)
- Completely remove loader/ (wwoods)
- We've got you cornered now, loader: remove from automake/spec/po (wwoods)
- move linuxrc.s390 out of harm's way (wwoods)
- move vncpassword handling into anaconda; remove recoverVNCPassword (wwoods)
- Remove misc. references to loader (wwoods)
- remove ancient anaconda-release-notes.txt (wwoods)
- remove scripts/upd-initrd and scripts/upd-bootiso (wwoods)
- Move from loader.service to anaconda.service (wwoods)
- Schedule (no-op) btrfs format create actions. (#799154) (dlehman)
- intelligently choose the window size (#800609) (bcl)
- fix text upgrade bootloader dialog (#742207) (bcl)

* Tue Mar 06 2012 Brian C. Lane <bcl@redhat.com> - 17.12-1
- only allow GPT boot flag on EFI System partition (#746895) (bcl)
- Add dracut args for /usr to bootloader (#787893) (bcl)
- Make sure all kickstart partition reqs get appropriate weight setting.
  (dlehman)
- Fix test for unsupported format type in kickstart. (dlehman)
- Update the fs size limit for ext3/ext4 from 8TB to 16TB. (dlehman)
- Don't allow /boot on logical partition except for grub. (dlehman)
- empty versions shouldn't be upgradable or traceback (#791317) (bcl)
- Don't crash when broken md devices are present. (#731177) (dlehman)
- Add missing definition of BTRFSError. (#796013) (dlehman)

* Tue Feb 21 2012 Brian C. Lane <bcl@redhat.com> - 17.11-1
- import using the right path to iutil (bcl)

* Mon Feb 20 2012 Brian C. Lane <bcl@redhat.com> - 17.10-1
- use a dracut shutdown hook to eject media (#787461) (bcl)
- add dracut shutdown eject hook function (#787461) (bcl)
- The createSuggested methods have changed name (#791204, #795058). (clumens)
- Generate repo= ks command only for repos added by user (#738577) (rvykydal)
- Use libpwquality to check root password strength (#755883) (mgracik)
- Generate connection UUID in inital ifcfg files created by anaconda (#705328)
  (rvykydal)
- Take in change of a binary name (brcm_iscsiuio -> iscsiuio) (#731761)
  (rvykydal)
- Set ONBOOT=yes for FCoE devices (#755147) (rvykydal)
- Fix a typo (#794504). (clumens)
- Add support for network --device=link in stage2 kickstart (#790332)
  (rvykydal)
- Set default lang and create default locale files early (wwoods)
- Add 'traceback' boot option for python-meh and libreport testing (vpodzime)

* Thu Feb 16 2012 Brian C. Lane <bcl@redhat.com> - 17.9-1
- Don't set the pmbr bootable flag on Macs, whether booted via EFI or not (mjg)
- Don't set GPT HFS+ partitions as bootable (mjg)
- Mark HFS+ as fsckable (mjg)
- fix setattr in set_cmdline_bool (pschindl)
- Add _mounttype to HFSPlus (mjg)
- Add support for UEFI Mac installs (mjg)
- Add support for HFS+ partitions (mjg)

* Mon Feb 13 2012 Brian C. Lane <bcl@redhat.com> - 17.8-1
- Clear partitions' metadata when 'clearpart --initlabel' used. (#783841)
  (cherry picked from commit 15307cc091212cc69b599b90c239492c9c9586ec)
  (dlehman)
- Fix support for detecting existing mirrored lvs. (#734128) (dlehman)
- fix potential EFIGRUB infinite loop (bcl)
- finish ROOT_PATH changes in bootloader (#789169) (bcl)
- Be more verbose about upgrade failures (#735060) (bcl)
- Skip setting PMBR boot flag on EFI (#754850) (mjg)
- Updated transifex config for f17-branch (bcl)

* Wed Feb 08 2012 Brian C. Lane <bcl@redhat.com> - 17.7-1
- anaconda_optparse.py: a new OptionParser that also reads boot args (wwoods)
- Add flags.set_cmdline_bool and flags.read_cmdline (wwoods)
- flags.py: add new BootArgs() object for dealing with boot args (wwoods)
- flags.py: rework/cleanup Flags object (wwoods)
- fix serial console option parsing (#767745) (wwoods)
- run convertfs on upgrade (#787893) (bcl)
- check if stdout and stderr are the same in execWithRedirect and open the file
  only once in such cases (mmatsuya)
- Disable ipv6 on target system when using noipv6 option (#735791) (rvykydal)

* Mon Feb 06 2012 Brian C. Lane <bcl@redhat.com> - 17.6-1
- Set the boot flag on the GPT PMBR (#754850) (bcl)
- Add missing _boot_description values for dasd and zfcp (#739620) (dcantrell)
- Select the same device for ksdevice=link in loader and stage2 (#760250)
  (rvykydal)

* Wed Feb 01 2012 Brian C. Lane <bcl@redhat.com> - 17.5-1
- Add a separate function to get an LV's VG name. (dlehman)
- util-linux-ng is now util-linux (bcl)

* Tue Jan 31 2012 Brian C. Lane <bcl@redhat.com> - 17.4-1
- liveinst: canonicalize live-baseloop symlink (bcl)
- Fixup getDeviceBy* methods (bcl)
- Ignore dm devs when scanning for mpath members (#761278) (hamzy)
- Don't set the system's hostname during disk image installs. (dlehman)
- Fix error handling in the case of no live block device. (dlehman)
- Force simple filter for disk image installs. (#784560) (dlehman)
- Check for live install before doing live-specific umounts. (dlehman)
- DM_VG_NAME tells an LV's VG, not the VG a PV belongs to. (#772878) (dlehman)

* Mon Jan 23 2012 Brian C. Lane <bcl@redhat.com> - 17.3-1
- Add missing log import to platform.py (bcl)
- liveinst: Check for live-baseloop LIVE_BLOCK (bcl)
- Add Storage.autoPartType to indicate lvm/btrfs/neither. (dlehman)
- Add full support for btrfs via kickstart's btrfs command. (dlehman)
- Show btrfs vols/subvols but don't allow editing them. (dlehman)
- Add support for btrfs to the devicetree. (dlehman)
- Remove an old hack with action registration. (dlehman)
- Add support for btrfs automatic partitioning. (dlehman)
- Add new field to PartSpec to indicate btrfs reqs. (dlehman)
- Add btrfs convenience methods to Storage. (dlehman)
- Handle device name generation and checking in a more generic way. (dlehman)
- Add btrfs base class along with classes for volume, subvolume. (dlehman)
- btrfs volumes/subvolumes are created by devicelibs.btrfs. (dlehman)
- Scan for btrfs while looking a new devices. (dlehman)
- Add backend module for operating on btrfs volumes. (dlehman)
- Fix default hostname function to never return '(none)'. (dlehman)
- Revert "Put bios boot partitions on all gpt disk on bios systems. (#738964)"
  (dlehman)
- Put NoSuchGroup and DispatchError back, but not in errors.py. (#760786)
  (dlehman)
- Clean up BootLoader.writeKS to account for no bootloader. (dlehman)
- Fix sense of disklabel size check and add some logging. (dlehman)
- Handle v0.90 md metadata in preexisting arrays. (dlehman)
- style cleanups for ppc SMS bios patch (wwoods)
- Update ppc SMS bios after installation (hamzy)
- report more detail about yum failure (bcl)
- Add a script mode that exits instead of looping (bcl)
- Add 'sound-and-video' to Fedora install class for 'Software Development'
  task. (#643786) (notting)
- Unmount the image file (bcl)
- Disable yum log file handling (bcl)
- Setup storage config when kickstart is parsed (bcl)

* Tue Nov 15 2011 Chris Lumens <clumens@redhat.com> - 17.2-1
- ARCHIVE_DEFAULT_BYTES_PER_BLOCK no longer exists in libarchive-3.0.0
  (clumens)
- Don't use the rpmdb to figure out upgrade target arch (#748119). (clumens)
- Remove obsolete error handling left over from the old storage code. (dlehman)
- Update to the FC16_VolGroupData so reserving space works. (dlehman)
- Remove unused import of gzip from task_gui.py (dlehman)
- Cap new /boot/efi partitions at 200MB. (#748274) (dlehman)
- Fix root device specification in zipl.conf. (#740576) (dlehman)
- Add --boot-drive option to kickstart bootloader command. (dlehman)
- Include disklabel type in grub2 device names. (dlehman)
- use 800x600 as minimal mainWindow size (vpodzime) (mgracik)
- Use an atexit handler for shutting down and ejecting media (#750809).
  (clumens)
- Fix a dumb error when canceling previous migration actions (#744034).
  (clumens)
- Document iscsi and multipath implementations. (akozumpl)
- Don't load forcefully load pcspkr.  The kernel doesn't (#750830). (clumens)
- Gray out "Configure Network" button in live installations (#749929)
  (rvykydal)
- Support prefix length in kickstart network --ipv6 option. (rvykydal)
- Support prefix length in ipv6= cmdline option (#679108) (rvykydal)
- Remove snarffont, which is no longer needed. (clumens)
- Change what the third column of lang-table means. (clumens)
- And stop attempting to load our own fonts, since we no longer ship them.
  (clumens)
- Remove our own screen fonts (#742613, #743429). (clumens)
- Don't use GPT disklabels on Lenovo BIOS systems. (#749325) (dlehman)
- Fix typo in call to opt.isdigit (#743787) (pjones)
- Don't allow disks containing the live media as boot disk. (#748587) (dlehman)
- Honor fsprofile argument even for existing devices. (#747417) (dlehman)
- Regenerate tasklist when a repo is removed. (akozumpl)
- Do a better job of remembering if 'review and modify partitioning' was
  checked. (akozumpl)
- Be more convincing in eradicating errant temp vg paths. (#722952) (dlehman)
- Resize: Update format size if aligning partition shrinks it. (#689179)
  (dlehman)
- Copy all of live filesystem to target (#746844) (bcl)
- Fix autopart shrink of existing system. (#746605) (dlehman)
- cryptsetup returns positive nonzero when activating by different than the
  first keyslot (msivak)
- do more logging in findExistingRootDevices() (akozumpl)
- Add 'nogpt' cmdline arg to disable creation of gpt disklabels. (dlehman)
- Show cleardisks gui always to allow selecting a boot disk. (#744088)
  (dlehman)
- mpath: flush more eagerly in filter_gui. (akozumpl)
- debugging: log boot arguments. (akozumpl)

* Tue Oct 11 2011 Chris Lumens <clumens@redhat.com> - 17.1-1
- Pull grub-efi and efibootmgr into the package list as needed. (#742042)
  (pjones)
- analog: properly log user.info where NetworkManager (also) communicates.
  (akozumpl)
- analog: bump the version to rsyslog 5 (akozumpl)
- partitioning.py: reference to list of free regions is shadowed by a double.
  (akozumpl)
- Handle strange lang boot argument values. (akozumpl)
- LANG_DEFAULT lives in lang.c. (akozumpl)
- Include docs/transifex.txt in release dist. (dcantrell)
- fcoe: modprobe the VLAN layer module. (akozumpl)
- Remove some raid error checking pykickstart can do for us. (clumens)
- Set default BOOTPROTO=dhcp for network service (minimal installs) (#741199)
  (rvykydal)
- remove argument ROOT_PATH from getDefaultKeyboard() calls (removed from
  method with 3e8d08cac6aa89f001c5b32dba251a62a45ed7f4) (vpodzime)
- Default to an active network device after reboot on Fedora (ONBOOT) (#498207)
  (rvykydal)
- Fix: Allow EFI slot_ids in hexdecimal (#742141). (fabian.deutsch)
- Move the fedora logo to the left. (akozumpl)
- fcoe: fix detecting FCoE NIC (mcb30)
- Do not show loop devices in the filtering UI. (akozumpl)
- dispatcher: do not request "group-selection" with "tasksel". (akozumpl)
- upgrade: do not insist on running the "bootloader" step. (akozumpl)
- Fix sigsegv in setKickstartNetwork() (strdup() from a NULL). (akozumpl)
- dracut args: "rhgb quiet" should come last. (akozumpl)
- Add nfsiso: handling to parseNfsHostPathOpts (bcl)
- Only check relevant devices for dirty filesystems. (#741206) (dlehman)
- Make sure storage is reset just before partitioning, always. (dlehman)
- Move selection of default boot drive into bootloader. (dlehman)
- Show error dialog instead of traceback on fstab type mismatch. (#649171)
  (dlehman)
- Try a test mount and keep fstab mismatches if it succeeds. (#649171)
  (dlehman)
- Check the return value of get_file_list (#741466) (bcl)
- imount.c: include fcntl.h before ext2fs/ext2fs.h. (akozumpl)
- Write the grub.conf after setting up the new EFI bootloader (#741994)) (bcl)
- botoloader: write 'ip=eth0:dhcp,auto6' instead of 'ip=eth0:dhcp
  ip=eth0:auto6' (akozumpl)
- gitingore: ignore po/*.po.new files. (akozumpl)
- Put bios boot partitions on all gpt disk on bios systems. (#738964) (dlehman)
- Change default bootloader timeout from 20sec to 5sec. (#727831) (dlehman)
- Bootloader stage1_drive is more than a suggestion. (#738964) (dlehman)
- Mark the live device's parent devices protected. (#738964) (dlehman)
- it is anaconda-shell (akozumpl)
- Improve the clarity of the missing bios boot partition error. (#731549)
  (dlehman)
- Remove tmp.mount (systemd handles this for us now) (wwoods)
- Move dependency info into the unit files (wwoods)
- move anaconda-shell.service to the correct filename (wwoods)
- make anaconda-shell.service a template, put it on tty2 & hvc1 (wwoods)
- Return after writing log message, not before. (rvykydal)
- Do not reactivate network device needlessly on s390 (#739846) (rvykydal)
- Start NM in loader on s390 until we have systemd init here too (#733680)
  (rvykydal)
- Revert "Set debug_package to %{nil} so we don't strip our binaries."
  (akozumpl)
- Fix createUser and createGroup to work with kickstart defaults (#739428)
  (bcl)
- Update test for createUser and createGroup (#739428) (bcl)
- fcoe: handle Broadcom fcoe devices correctly. (akozumpl)
- fcoe: the control path in sysfs is now /sys/module/libfcoe (akozumpl)
- fcoe: load bnx2fc if relevant. (akozumpl)
- Fix post-commit lookup of extended partitions. (#737532) (dlehman)
- Don't reboot when closing the live installer via the window decoration.
  (clumens)
- Use the luks format's mapName when creating temp LUKSDevice. (#722952)
  (dlehman)
- Reset device attr after using temp dev. (#722952) (dlehman)
- Make sure there are no tempvg paths even if formatting. (#737916) (dlehman)

* Thu Sep 15 2011 Chris Lumens <clumens@redhat.com> - 17.0-1
- Sort partitioning commmands in anaconda-ks.cfg. (#736527) (dlehman)
- Install grub2 when upgrading on bios x86. (#735730) (dlehman)
- Default to installing a new bootloader on upgrade. (dlehman)
- Add a Reboot button to the congrats screen on live (#705189). (clumens)
- Add support for reserving space in lvm vgs via kickstart. (dlehman)
- iutil: make getArch() return ppc64 on ppc64 (#736721) (wwoods)
- iutil: add 'bits' arg to isPPC (like isX86) (wwoods)
- nfsiso: handle mismatching .iso architecture gracefully. (akozumpl)
- systemd: anaconda.target wants rsyslog.service (akozumpl)
- Improve checking if new biosboot partition is needed. (akozumpl)
- mpath: create /etc/multipath/bindings if we are using friendly names.
  (akozumpl)
- isolate localeInfo and expandLangs() from langauges.py into a separate
  module. (akozumpl)
- Make sure we teardown root candidates in all cases. (#693095) (dlehman)
- Update parted partition by sector, not name, after create. (#733449)
  (dlehman)
- Determine existing md arrays' metadata version. (#731266) (dlehman)
- Don't check mountable before obtaining actual/existing fs size. (#733808)
  (dlehman)
- Fix traceback when installing over a system with broken rpm db. (akozumpl)
- kickstart: use 'bootloader --timeout' even if it is zero. (akozumpl)
- Fix some things using old bootloader/platform stuff. (dlehman)
- Fix traceback when validating unallocated partition requests. (#733670)
  (dlehman)
- Require BIOS boot partition for GPT bootdisk on BIOS systems. (dlehman)
- Prevent grub2 from trying to access floppy drives. (dlehman)
- Limit grub stage2 md members' device type and metadata version. (dlehman)
- Remove unnecessary ROOT_PATH constant passing. (akozumpl)
- Moving anaconda.rootPath to constants.ROOT_PATH. (akozumpl)
- Remove deprecated --rootPath and --test. (akozumpl)
- Tidy warnings.showwarning into anaconda_log.py. (akozumpl)
- cosmetic: remove trailing whitespace in timezone_test.py (akozumpl)
- ut: cleanup after firewall_test.py (akozumpl)
- ut: move tests/fw_test.py to tests/pyanaconda_test/firewall_test.py
  (akozumpl)
- Close out the yum history before running %post scripts (#730857). (clumens)
- Remove unused attribute 'bootable' from DeviceFormat classes. (dlehman)
- Allow btrfs stage2 with grub2. (#732594) (dlehman)
- Clean up return values of GRUB2._gpt_disk_has_bios_boot. (dlehman)
- Force grub2 install to partition's boot block. (#727679) (dlehman)
- Don't crash because we don't have support for linear md. (#646157) (dlehman)
- Clean up obsolete extended partitions if partitioning fails. (#672010)
  (dlehman)
- Convert a None from libiscsi.discover() to an empty list. (akozumpl)
- Honor kickstart 'autopart --nolvm' option (jlaska)
- Allow answering the uninitialized disk question more than once. (akozumpl)

* Thu Aug 18 2011 Chris Lumens <clumens@redhat.com> - 16.15-1
- i18n: Do not include newlines in the reinit dialog's label. (akozumpl)
- Move the trusted_boot setting into AnacondaYum.run (#731260). (clumens)
- Put nolock instead of ,nolock to options if provided options are empty
  (#727522) (msivak)
- Deal with zFCP multipath devices in the filter UI (#618535) (dcantrell)
- matchpathcon doesn't like strings like "//lib64", so remove a slash
  (#730863). (clumens)
- Fix check so we actually disallow use of preexisting root filesystems.
  (dlehman)
- Correctly handle reqs with max size no larger than base size. (#730009)
  (dlehman)
- Set the default grub2 entry to the OS we just installed. (dlehman)
- Create 'console=..' configuration also for grub2. (akozumpl)
- Copy /etc/multipath/wwids to the sysimage. (akozumpl)
- add multiboot support for tboot (gang.wei)
- Fix createUser (bcl)
- raid ui: compute max number of spares based on raid members selected.
  (akozumpl)
- Remove definite articles in the bootloader translation strings. (akozumpl)
- Avoid final hang if no reboot action is specified in kickstart. (akozumpl)
- Check before setting partition label (#729599) (bcl)
- Remove as many of the /selinux path hardcodings as possible (#729563).
  (clumens)
- Raise informative error for ks=bootif, missing BOOTIF case (#681803).
  (rvykydal)
- dispatcher: do not show install steps in upgrade. (akozumpl)
- edd: fix traceback on Xen. (akozumpl)
- ConditionKernelCommandLine is a setting for Unit, not Service. (clumens)
- The script sections should operate on an AnacondaKSScript instance (#728468).
  (clumens)
- Restart NetworkManager to use anaconda's initial ifcfg config (#727951)
  (rvykydal)
- simplify anaconda.target/loader.service requirements (wwoods)
- make anaconda-shell.service more like getty (wwoods)
- ut: fix upgrade_test.py (akozumpl)
- Fix more dispatcher problems. (akozumpl)
- Check if the potential dep is in done, not the leaf. (#728891) (dlehman)
- Don't crash when checking unpartitioned devices for disklabel. (#720070)
  (dlehman)
- Remove "-Alpha" or "-Beta" from yum's $releasever (#728868). (clumens)
- Fix extra quote in grub.conf header string (bcl)
- Set EFI mountpoint when using existing partition (#727933) (bcl)
- Set the boot partition's name (bcl)
- Set boot partition's boot flag, stage2 has priority, fallback to stage1 (bcl)
- exec params need to all be strings (bcl)
- Fix efi_product_path regex (#728007) (bcl)
- Remove unneeded if block (bcl)
- Add some useful logging for partitioning and boot device choices (bcl)
- Add a space to DiskChunk repr string (bcl)
- ssl: 'noverifyssl' kernel boot argument. (akozumpl)
- Cleanup existing formats' device attr after lvm dialog edit. (#723303)
  (dlehman)
- Fix handling of skipped LUKS devices the second time through. (#727814)
  (dlehman)
- booty tests removed in cd66c6bf33cae14e74001349043e585e348e2e9a (#728477)
  (vpodzime)
- gui: translate custom_icon to stock icon name in detailedMessageWindow()
  (akozumpl)
- ut: product_test.py should not fail if executed by itself. (akozumpl)
- Handle rpmdb open errors by throwing out the root candidate (#723167).
  (clumens)
- Don't raise Retry dialog in loader kickstart networking (#722276) (rvykydal)
- Honor linksleep boot option (#713991) (rvykydal)
- Don't write duplicate lines for encrypted block devices. (dlehman)
- Setup default for non_linux_format_types (bcl)
- don't build functions not used on s390(x) (dan)
- variable 'i' ununsed on s390(x) (dan)
- use macro name instead of value (vpodzime)
- Annotate the list of what pylint warnings and errors we ignore. (clumens)
- Locally disable some E1101 "errors" that pylint doesn't understand. (clumens)
- Move out the parts of Device.__str__ that are StorageDevice specific.
  (clumens)
- Fix a udev import to be more explicit.  This shuts up pylint. (clumens)
- Disable error reporting for properties with the .setter syntax. (clumens)
- Disable E1103 (the "some types could not be inferred" message). (clumens)
- Delete the Mocked pyanaconda.product to fix product tests. (clumens)
- Fix import errors in the unit tests. (clumens)
- Remove the booty unit tests. (clumens)
- We also need to catch ValueError on mock.disk.TestFile.__del__. (clumens)
- Only warn when swaps with no UUID are preexisting. (dlehman)
- Fix scan of already-active mdbiosraidarrays before scan of container.
  (dlehman)
- Remove dogtail support.  No one uses it anyway. (clumens)
- Show all disks in text mode cleardisks selector. (#714836) (dlehman)
- Fix a traceback when user makes a partition whose size is out-of-bounds.
  (dlehman)
- Add a warning about the fstab implications of swap devices with no UUID.
  (dlehman)
- Fail gracefully when device name collisions occur in kickstart. (dlehman)
- Don't traceback if disks go missing before/during partitioning. (dlehman)
- dispatcher: allow requesting a step without insisting. (akozumpl)
- edd: fix syntax in situation when two edd directories point to the same
  device. (akozumpl)
- ut: cleanup the taking-over-io mechanism. (akozumpl)
- Fix broken unit tests (cmdline, network). (akozumpl)

* Tue Jul 26 2011 Chris Lumens <clumens@redhat.com> - 16.14-1
- Change IsBeta to IsFinal (mgracik)
- edd: do not traceback with cciss devices. (akozumpl)
- edd: do not traceback when can not find the respective pci device. (akozumpl)
- Use unsigned long long type in doTotalMemory() (dcantrell)
- Do not traceback on mpath errors caused by faulty hardware. (akozumpl)
- Fix a bunch of stupid little errors pylint caught. (clumens)
- There's no more booty module, so don't bother checking it. (clumens)
- Ignore false positives in kickstart.py. (clumens)
- Ignore reimport warnings from pylint. (clumens)
- Handle any amount of whitespace between keyword and rhbz reference.
  (dcantrell)
- dispath -> dispatch in kickstart.py. (clumens)

* Wed Jul 20 2011 Chris Lumens <clumens@redhat.com> - 16.13-1
- progressWindow takes a bunch of new arguments for pulsing (#723345).
  (clumens)
- request_step -> request_steps in anaconda. (clumens)
- Add a writeKS method for encrypted partitions. (clumens)
- Don't associate LVs' formats with their parent VG. (dlehman)
- Use os-prober to generate GRUB2 dual-boot menu entries. (dlehman)
- Fix GRUB2 password handling and GRUB1 kickstart password handling. (dlehman)
- changes needed to have per-connection ifcfg files for wifi connections
  (vpodzime)
- do not care about wifi connections in kickstart (already active from stage1)
  (vpodzime)
- do not take anaconda's netdevices into account while searching for APs
  (vpodzime)
- remove key-files writing in loader (no more needed, NM does it itself)
  (vpodzime)
- do not write default ifcfg files for wireless devices (vpodzime)
- Remove the 11.x history from anaconda.spec. (clumens)

* Mon Jul 11 2011 Chris Lumens <clumens@redhat.com> - 16.12-1
- Remove hasFreeDiskSpace and related code. (dlehman)
- Use protected for pvs of incomplete vgs and get rid of immutable. (dlehman)
- Use mdadm's default metadata format instead of hardcoding 1.1. (dlehman)
- Only show warning about no biosboot on gpt on gpt. (dlehman)
- Plumb the cleanupOnly= option through to Storage.reset(). (clumens)
- i18n: Maintain the translated repo name upon modifying. (akozumpl)
- Log errors during dependency resolution. (clumens)
- Fix a bug where language names aren't translated to native. (clumens)
- Remove things from utils/ that lorax obsoletes. (clumens)
- Remove things from scripts/ that lorax obsoletes. (clumens)
- Handle systems with more than 2147483647 kB of memory (#704593). (dcantrell)
- Remove support for the ext4migrate option (#712195). (dcantrell)
- edd: refactor and enhance the edd module. (akozumpl)
- unit tests: provide 'glob.glob' and 'os.listdir' in the DiskIO class.
  (akozumpl)
- Pulsing progress bar instead of the static popup during device discovery.
  (akozumpl)
- yum: handle PackageSackErrors separately in AnacondaYum._run. (akozumpl)
- We need a later version of pykickstart with the wpakey parameter. (clumens)
- Remove KillMode= from systemd control files. (clumens)
- Add a property to Platform for accessing boot stage1 constraints. (dlehman)
- Simplify lvm growing by using units of pesize instead of MB. (dlehman)
- Move platform-specific boot-related data into Platform. (dlehman)
- Make /home autoreq grow a bit faster in relation to root. (dlehman)
- Update upd-bootiso for F16 (bcl)
- Allow a .iso file to be specified instead of a directory (#707846) (bcl)
- Fix typo from 573ef017. (akozumpl)
- Keep dracut settings in sets instead of many long strings. (akozumpl)

* Wed Jun 22 2011 Chris Lumens <clumens@redhat.com> - 16.11-1
- be more defensive -- check values for nonsenses (vpodzime)
- enable netmask setting for wireless connections (vpodzime)
- enable dns settings of wireless connection (vpodzime)
- enable gateway settings of wireless connection (vpodzime)
- enable wpa in kickstart (vpodzime)
- enable establishing wpa connection in "early networking" (vpodzime)
- ut: remove trailing whitespace in language_test.py (akozumpl)
- 'part' command checks if the disk is partitionable. (akozumpl)
- Correct and simplify handling of "bootable" partition requests. (dlehman)
- Don't check the fstype for /boot req weight. (dlehman)
- Freeze the lvm button when custom partitioning is selected. (dlehman)
- Use the same code for growing lvs that we use for growing partitions.
  (dlehman)
- Fix check for whether new lv size will fit in vg's free space. (dlehman)
- Sun disklabel hacks. (#697100) (dlehman)
- Maximize extended partition even when logical reqs' sizes are capped.
  (dlehman)
- Don't magically adjust fstype when mountpoint is set to "/boot". (dlehman)
- Handle partition allocation failures due to alignment adjustments. (dlehman)
- Include protected attribute in StorageDevice.__str__. (dlehman)
- Log results of protected device spec resolution. (dlehman)
- Implement an option that lets anaconda name mpath devices by the wwid.
  (akozumpl)
- In kickstart, specify multipaths by their wwids. (akozumpl)
- multipath: allow mpath<X> specfifications in kickstart. (akozumpl)
- multipath: do not set any mpath aliases explicitly. (akozumpl)
- Use global proxy setting if no repo proxy is set (#712926) (bcl)
- Remove duplicate code. (rvykydal)
- Fix typo (DispatcherError->DispatchError). (dlehman)
- Allow autopart without lvm. (dlehman)

* Wed Jun 08 2011 Chris Lumens <clumens@redhat.com> - 16.10-1
- Update to the latest pykickstart version. (clumens)
- Fix a typo to make encrypted installs get farther. (clumens)
- Fix the filter UI to sort capacity as numbers, not characters (#614504).
  (clumens)
- Fix up swap unmount logic (#708966) (bcl)
- Use read-only locking for lvm commands in udev rules. (dlehman)
- Check if LVs still fit when removing a PV from a VG. (#682276) (dlehman)
- Don't get tripped by partial fstab option matches. (#699167) (dlehman)
- RAID gui: fix how the "Number of spares" spin button is manipulated.
  (akozumpl)
- imount.c: first wait() for mount then close its stdin/stdout. (akozumpl)
- Fix a couple of action obsoletes bugs. (dlehman)
- Schedule an action when destroying the old format on an encrypted lv.
  (dlehman)
- Revert "Make sure new devices' formats have their device attr set." (dlehman)
- Set formats' device attr when associating the format with a device. (dlehman)
- cosmetic, iscsi: make the 'no credentials' string more general. (akozumpl)

* Mon May 23 2011 Chris Lumens <clumens@redhat.com> - 16.9-1
- Add kickstart support for biosboot. (dlehman)
- Make sure new devices' formats have their device attr set. (dlehman)
- Don't crash if is_valid_foo methods are called with None. (dlehman)
- Unit tests cleanups (akozumpl)
- Remove trailing whitespace in file tests/mock/mock.py. (akozumpl)
- Remove erronious (vestigial?) call to Platform.isEfi (pjones)
- Remove upgrade_swap_gui from POTFILES.in (akozumpl)
- ut: if _isys is not available dispatch_test and indexed_dict_test are
  failing. (akozumpl)
- Cherry-pick from rhel5-branch, by Will Woods. (wwoods)
- Pythonize some code from network.py for pleasure. (rvykydal)
- Honor DEFROUTE=no when inferring system-wide GATEWAY (rvykydal)
- Get rid of overrideDHCPHostname. (rvykydal)
- HOSTNAME is not per-device/ifcfg setting. (rvykydal)
- Do not set hostname in stage 1. (rvykydal)
- Do not write out /etc/sysconfig/network in stage 1. (rvykydal)
- ut: make pyanaconda_test/backed_test.py pass (akozumpl)
- dispatch: break out step initialization into a separate method. (akozumpl)
- dispatch: implement method of saving/restoring all steps scheduling.
  (akozumpl)
- upgrade: there are no "checkdeps" and "dependencies" steps. (akozumpl)
- ut: make upgrade_test pass. (akozumpl)
- cosmetic: dispatch.request_step is dispatch.request_steps. (akozumpl)
- cosmetic: dispatch.skipStep is dispatch.skip_steps (akozumpl)
- cosmetic: move the dir property in dispatch.py with other public methods.
  (akozumpl)
- dispatch: fix remaining places using the old dispatch interface. (akozumpl)
- dispatch: remove "upgradeswapsuggestion" and "addswap" steps. (akozumpl)
- dispatch: Fix rules for running the bootloader and instbootloader steps.
  (akozumpl)
- dispatch: Fix rules for running the partitioning step. (akozumpl)
- dispatch: clean up step skipping manipulations in kickstart. (akozumpl)
- dispatch: All skips are permanent now. (akozumpl)
- Cleanup how an installer interface can declare steps it does not implement.
  (akozumpl)
- Throw away the dispatcher 'skipList' and give Step a state. (akozumpl)
- dispatch: use IndexedDict objects instead of a list of tuples. (akozumpl)
- IndexedDict class for storing the installer steps (akozumpl)
- Add a shortcut for Configure Network (#705022) (mgracik)
- vgreduce now activates some lvs, which I do not understand. (dlehman)
- Audit storage log statements' log levels and clean up some things. (dlehman)
- Convert Device, DeviceFormat __str__ to __repr__ and add __str__. (dlehman)

* Tue May 17 2011 Chris Lumens <clumens@redhat.com> - 16.8-1
- Relabel /var/lock as well (#701575). (clumens)
- filled in hasFreeDiskSpace (#683632) (hamzy)
- Add a python program to record memory usage during installation. (clumens)
- Add a timestamp to every line in install.log/upgrade.log. (clumens)
- storage: add SparseFileDevice (wwoods)
- FileDevice._create: don't alloc memory equal to file size, close fd (wwoods)
- Text mode upgrade should default to upgrade (#704588) (bcl)
- Trim "/dev/" correctly in list-harddrives (#702430). (dcantrell)
- Include missing parentheses in lvm/md device map names. (dlehman)
- Make sure stage1 and stage2 devices are in device.map in case of md,lvm.
  (dlehman)
- Only do redundant mbr installation for mirrored stage2. (dlehman)
- Allow growable md member requests but only for RAID0. (dlehman)
- Let blkid/udev tell us which devices contain disklabels. (dlehman)
- Move selection of new disklabel's type from DiskLabel to Platform. (dlehman)
- Fix an omission from the integration of the new bootloader module. (dlehman)
- Rework bootloader constraint checking routines. (dlehman)
- Include a BIOS boot partition in X86 autopart on GPT. (dlehman)
- Add format class for BIOS boot partition. (dlehman)
- Update dracut kernel args (#702711) (bcl)
- Add btrfs min size of 256 MB. (#702603) (dlehman)
- Update the requirements for memory.. (dlehman)
- fix resuce_test.py (akozumpl)
- remove references to "zfcpconfig". (akozumpl)
- Turn sshd setup, kicstart execution and the rescue mode into dispatch steps.
  (akozumpl)

* Tue May 03 2011 Chris Lumens <clumens@redhat.com> - 16.7-1
- Make grub2 the default bootloader on x86. (dlehman)
- Make sure bootloader stage1 device stays current through partitioning.
  (dlehman)
- Remove unused Platform.validBootLoaderPartSize method. (dlehman)
- Check that there is a stage1 req before validating it otherwise. (dlehman)
- set_preferred_stage2_type -> set_preferred_stage1_type (dlehman)
- Allow unsetting of stage1_device. (dlehman)
- Add a "boot drive" concept to the bootloader since stage1 types vary.
  (dlehman)
- Consistently refer to stage1 and stage2 device as such. (dlehman)
- Fix handling of missing boot device in doPartitioning. (dlehman)
- Finish removing bootloadersetup step. (dlehman)
- Add grub2 class, fix packages for some classes. (dlehman)
- Don't change bootloader names for various configurations. (dlehman)
- Add encrypted attribute to StorageDevice. (dlehman)
- iscsi: disable the 'Login' button with no nodes selected. (akozumpl)
- nuke: InstallControlWindow.busyCursor*() (akozumpl)
- iutil: remove excess imports. (akozumpl)
- Get rid of interface's entryWindow() and EntryWindow. (akozumpl)
- Allow DeviceFormat.cacheMajorminor to fail without an exception. (akozumpl)
- Don't check /boot fs when no bootloader is installed (#698312) (bcl)
- yuminstall.py: self.pulseWindow is not used anywhere. (akozumpl)

* Thu Apr 21 2011 Chris Lumens <clumens@redhat.com> - 16.6-1
- Do not recreate the ssh keys if they exist already. (akozumpl)
- Display a banner when (re)starting Anaconda. (akozumpl)
- Most viewers of tty1 do not care about xrandr stderr output. (akozumpl)
- restart-anaconda: no need to redownload the updates. (akozumpl)
- Write 'edd' instead of 'ethX' for fcoe= dracut parameter. (dcantrell)
- When checking for allowing an upgrade, trim off any "-Alpha" or "-Beta".
  (clumens)
- Make text for failed upgrade dialog clearer (#697193) (bcl)
- Fix a grammar error in the upgrade message (#697244). (clumens)
- If there are no RAID arrays, do not write an mdadm.conf (#696907). (clumens)
- loader: always call klogctl to disable kernel logging in the console.
  (akozumpl)
- Set mainWindow size request to current res reported by xrandr (#694760)
  (dcantrell)
- Fix SIGSEGV for netwowrk --device=<MAC> which is not found (#697432)
  (rvykydal)
- Use correct interface to obtain HwAddress property (#693614) (rvykydal)
- Revert "Don't write HWADDR into ifcfg files (#690589)" (rvykydal)
- analog: turn off another harmful feature of rsyslogd. (akozumpl)
- analog: cleanup whitespace in the file. (akozumpl)
- Fix building with --disable-selinux (mark (clumens)
- Don't include system virtual filesystems in /etc/fstab (#693926). (clumens)
- Set ANACONDA=1 in the udev environment early in anaconda. (clumens)
- findFirstIsoImage needs to return a filename, so fix it. (clumens)
- Fix unmounting in anaconda-cleanup to deal with /mnt/sysimage as well.
  (clumens)
- Remove the second upgrade check from yuminstall.py. (clumens)
- Cache the value of Format.majorminor(). (akozumpl)
- And call anaconda-cleanup from restart-anaconda. (clumens)
- Unmount everything in /mnt/install from anaconda-cleanup. (clumens)
- Move most anaconda mount points to be under /mnt/install. (clumens)
- Fix the initialization of LUKS device, we have to add the first keyslot (also
  add key_file arguments for compatibility) (msivak)
- Add "quiet" to the x86-64 and i386 boot arguments. (clumens)
- Update restart-anaconda to work with systemd. (clumens)
- Remove init.[ch]. (clumens)
- Move debugging features into loader.c. (clumens)
- We no longer need to get the PID of init from loader. (clumens)
- Move serial console handling code out into its own file. (clumens)
- Make reboot/halt/shutdown decisions in anaconda instead of loader. (clumens)
- Remove all the custom shutdown/reboot/halt code in loader and init. (clumens)
- Move syslog starting into loader. (clumens)
- loader doesn't support arguments except from /proc/cmdline. (clumens)
- Don't build our own init anymore. (clumens)
- Remove the duplicate backtrace setup code in init.c. (clumens)
- Remove from init.c/loader.c things that systemd does for us. (clumens)
- Add the unit files necessary to have systemd start loader. (clumens)

* Mon Apr 11 2011 David Lehman <dlehman@redhat.com> - 16.5-1
- Remove maximum limit on EFI partition (#684860) (bcl)
- Changes for NetworkManager API 0.9 (rvykydal)
- Fix network --device=bootif value processing in stage2. (vpodzime)
- Ignore --device=ibft in stage 2 kickstart handling (#638131) (vpodzime)
- Don't write HWADDR into ifcfg files (#690589) (rvykydal)
- Fix network --device=<MAC> for static configurations (#693302) (rvykydal)
- Fix bad indentation from 026dacc3. (akozumpl)
- If we change language during Python, build the new locale files. (clumens)
- If we're not given a language on the command line, set up English. (clumens)
- No longer log that we're resetting the file context. (clumens)
- Do filesystem-specific sync operation after writing configuration. (dlehman)
- Add sync method to force data onto disk and/or journal. (dlehman)
- Update ui screens to use new bootloader module. (dlehman)
- Update remaining parts of anaconda to use new bootloader module. (dlehman)
- Update storage module for new platform and bootloader modules. (dlehman)
- Update platform.py for new bootloader module. (dlehman)
- Update kickstart.py for new bootloader module. (dlehman)
- Replace booty with a new bootloader module. (dlehman)
- Add "disks" attr to StorageDevice to list disks a device depends on.
  (dlehman)
- Prevent debug and kdump kernels from becoming the default (#693702)
  (dcantrell)
- Use znet_cio_free to clear network devices from cio_ignore. (dcantrell)
- Remove deprecated targets from top level Makefile.am (dcantrell)
- Remove languages not available from Transifex. (dcantrell)
- Add Transifex instructions for anaconda developers. (dcantrell)
- Update Makefile.am to work with new translation system. (dcantrell)
- BuildRequires transifex-client (dcantrell)
- Ignore po/*.po files (dcantrell)
- Remove translation files. (dcantrell)
- Add transifex-client configuration file. (dcantrell)
- Fix syntax error from commit 9e696b62. (akozumpl)
- Rewrite nfs url parsing in loader (bcl)
- Fix order of nfs mountOpts in promptForNfs (bcl)
- timeout= in yaboot.conf is in tenths of seconds (#692409) (dcantrell)
- Install dracut-fips package when fips=1 is specified (#692350) (dcantrell)
- unicode-linedraw-chars.txt is no longer useful. (clumens)
- mkctype is no longer useful. (clumens)
- Fix a typo in swap upgrade strings (yurchor (clumens)

* Thu Mar 31 2011 Chris Lumens <clumens@redhat.com> - 16.4-1
- Fix a syntax error from the previous translation commit. (clumens)
- crypttab should not be world-readable (#692254). (clumens)
- Improve the translatability of strings with more than one format specifier.
  (clumens)
- Stop user if we have no /boot and / is an LV (dcantrell)
- Prevent singlePV lv requests from being > the size of any pv (dcantrell)
- Do not print out traceback when localedef is not present (msivak)
- Update our storage/crypto interface to use new cryptsetup API (msivak)
- Fix the logic surrounding use of the filterfunc for get_file_list (#691880).
  (clumens)
- mount needs to be told "nfs" or it assumes any argument is a device
  (#678414). (clumens)
- Fix rebooting after a kickstart error is detected. (akozumpl)

* Mon Mar 28 2011 Chris Lumens <clumens@redhat.com> - 16.3-1
- Use a more general EnvironmentError to catch timezone-file errors. (akozumpl)
- Add shell command to upd-bootiso (bcl)
- Set debug_package to %{nil} so we don't strip our binaries. (pjones)
- Return values, not strings (bcl)
- Use proper store types for DataComboBoxes. (akozumpl)
- Fixup rindex usage (#678086) (bcl)
- Ensure new kernel is default in zipl.conf on upgrade installs (#683891)
  (dcantrell)
- shutdown: kill processes in the anaconda process group. (akozumpl)
- After 17233a16, vncS is no longer a global. (akozumpl)
- shutdown.c: pidof and killall5 are in /sbin on rawhide. (akozumpl)
- Check size limits on pre-existing partitions (bcl)
- gui.py: nuke createRepoWindow() (akozumpl)
- gui.py: nuke titleBar*() (akozumpl)
- Fix --mtu option to kickstart network command (#689081) (icomfort)
- Implement a general version of InstallInterfaceBase.methodstrRepoWindow().
  (akozumpl)
- Update icons and add a new 256x256 version (#689014). (clumens)
- Fix the filesystem migration dialog in text mode (#688314). (clumens)
- Don't fatal_error if required mounts are already mounted (wwoods)
- Don't fatal_error if remounting root read-write fails (wwoods)
- Align lv sizes when adding to vg total space used. (dlehman)
- Clean up display of free space in partitioning gui. (dlehman)
- Fix a syntax error in my last upgrade-related commit. (clumens)
- Remove some more xutils-related code. (clumens)
- Prevent Platform from importing storage stuff until it's necessary. (clumens)
- Restore stats from original mount on livecd (#683682) (bcl)
- Properly filter out new mounts for livecd install (#683682) (bcl)
- Mount livecd filesystems under /mnt (#683682) (bcl)
- Fix order of opts and host when processing kickstart nfs lines. (clumens)
- Rework the upgrade swap suggestion (#684603). (clumens)
- Log running version number as soon as possible (bcl)
- Collect LUKS passphrases to avoid making users enter them repeatedly.
  (dlehman)
- Don't include incomplete md arrays in the devicetree. (dlehman)
- Detect live environment if no args passed to anaconda-cleanup. (dlehman)

* Mon Mar 14 2011 Chris Lumens <clumens@redhat.com> - 16.2-1
- iscsi: use the --target parameter from the iscsi kickstart command.
  (akozumpl)
- Make the "comps" translation domain dynamic. (akozumpl)
- Add a missing include to fix the build. (clumens)
- Remove the last of the xutils module. (clumens)
- Fix a missing exception variable. (akozumpl)
- Add cmdline options and f15 support to upd-bootiso (bcl)
- Use yum's new callback mode when available (pmatilai)
- Pressing enter on the keyboard screen should go to the next screen (#683448).
  (clumens)
- Do not allow use of preexisting root filesystem. (#629311) (dlehman)
- Stop using --update=super-minor when starting md arrays. (dlehman)
- Fix kickstart handling of md spares. (#683605) (dlehman)
- Fix sensitivity of options in text network config UI (#681580) (jlaska)
- Consolidate ip address checking into functions. (rvykydal)
- Add support for ipv6 to gateway boot option (#677609) (rvykydal)
- Fix parsing of ipv6 --gateway in kickstart (#677609) (rvykydal)
- Remove 'Back' button on depsolving exception for ks installs (#673170)
  (dcantrell)
- Shorten the anaconda repo names (#679434). (clumens)
- fix mnemonics in the 'Add Repository' dialog (akozumpl)
- Create the virtio-ports on time. (akozumpl)
- Do not pass --sshd to stage2. (akozumpl)
- Handle boot loader upgrades on s390 (#682783) (dcantrell)
- Don't assume BOOTIF present for ksdevice=bootif. (rvykydal)
- syntax errors correcting (vpodzime)
- Apply one more fix for "logvol --label=" (#673584) (clumens)
- Fix test for resized LV to ensure we schedule the format resize action.
  (dlehman)
- Make sure a bootloader device is selected (#595951) (bcl)
- Another fix for the loader translations. (akozumpl)
- /var/log/dmesg doesn't exist in a live install. messages does, though.
  (dlehman)
- Don't try to unlink a config file that isn't there. (dlehman)
- Handle md name-mangling based on hostname/homehost WRT exclusiveDisks.
  (dlehman)
- Adjust DeviceTree.isIgnored's handling of loop, ram, and live devices.
  (dlehman)
- Allow scanning of already-active md devices. (#680226) (dlehman)
- Don't clobber exclusiveDisks unless there are disk images. (dlehman)
- Do on-demand scanning of md container if needed. (#678877) (dlehman)
- Fix md array spares test. (dlehman)
- Fix udev_device_is_md. (dlehman)
- Add /var/lib/yum to the list of directories we set context on (#681494).
  (clumens)
- Pass createUser and createGroup an arguments dict. (clumens)
- Check all PV ancestor devices for growable partitions. (dlehman)
- Enable network if sshd boot option is used (#643738) (rvykydal)
- Fix setting of loaderData->method from repo= cmdline option. (rvykydal)
- Gotta catch 'em all parted exceptions. (akozumpl)
- Give an indication how many packages are left in cmdline mode (#681614).
  (clumens)
- Dynamic strings make gettext translations fail. (akozumpl)
- devt.h is no longer useful, remove it. (clumens)
- Remove 'Back' button on depsolving exception for ks installs (#673170)
  (dcantrell)
- Ensure remount requests go through isys.mount() (#678520) (dcantrell)
- Check repo instead of method type when enabling network in loader (#673824)
  (rvykydal)
- Fix setting of some network values in loader kickstart (#679825). (rvykydal)
- Loader should activate, stage 2 configure network devices. (rvykydal)
- Do not activate first ks network device automatically in non-network
  installs. (rvykydal)
- Always activate first kickstart network device (rvykydal)
- Make kickstart network command reconfigure active device in loader (rvykydal)
- Use NM for ibft configuration (rvykydal)
- Reset only ifcfg file of device we failed to activate (rvykydal)
- Initialize iface structure properly (rvykydal)
- Add kickstart network --nodefroute option (rvykydal)
- Add support for ks network --bootproto=ibft (rvykydal)
- Wait for activation of specific devices instead of NM (rvykydal)
- Parse all kickstart network commands in loader too (rvykydal)
- Activate all devices set by kickstart network --activate command (rvykydal)
- Parse new kickstart options network --activate and --nodefroute. (rvykydal)
- Fixup upgrade test for findExistingRoots change (#681267) (bcl)
- Change upgrade to use findExistingRootDevices (#681267) (bcl)
- Initialize locale before the kickstart/virtio check (#679702) (msivak)

* Tue Mar 01 2011 Chris Lumens <clumens@redhat.com> - 16.1-1
- Fix another unused return value error message. (clumens)

* Tue Mar 01 2011 Chris Lumens <clumens@redhat.com> - 16.0-1
- Pass correct class to super in SELinuxFS.mountable. (#677450) (dlehman)
- Clarify that loader method entries are looking for a tree. (clumens)
- Fix up remaining anaconda.id references (#680296) (bcl)
- Wipe out pre-existing problems before running transaction (#678201, pmatilai). (clumens)
- Attempt at fixing reboot behavior in kickstart (#676968). (clumens)
- brcm_iscsiuio is not in Fedora yet, handle that you can't find it. (akozumpl)
- Fix downloading .treeinfo files for --noverifyssl repos. (akozumpl)
- Fix syntax error from 0bf0cf13. (akozumpl)
- Pass --force when calling vgreduce --removemissing. (#679206) (dlehman)
- Only apply global passphrase to devices with no passphrase. (#679223) (dlehman)
- Perform terminations before unmounting filesystems on shutdown. (dlehman)
- Get size + summary from yum package object instead of callback key (pmatilai)
- Test for stringiness instead of explicit rpm.hdr class in install callback (pmatilai)
- Remove unused doneFiles counting from transaction callback (pmatilai)
- Handle nfsiso in promptForNfs as well (#678413). (clumens)
- If the umount in getFileFromNfs fails, log it. (clumens)
- Correct the return values of some backend base class methods. (#679107) (dlehman)
- Change xhost auth when doing a liveinst (#663294) (bcl)
- Override kernel cmdline updates (bcl)
- Write --noverifyssl to repos and urls in kickstart where fit. (akozumpl)
- Do all dm handling inside addUdevDMDevice. (#672030) (dlehman)
- Remove storage/miscutils.py, it is not used. (akozumpl)
- Be better at handling killed metacity. (akozumpl)
- Remove Dispatcher.firstStep. (akozumpl)
- remove InstallerControllerWindow.setup_theme() (akozumpl)
- Make the dispatcher call the shots. (akozumpl)
- icw._doExit is now icw.close() (akozumpl)
- remove trailing whitespace from gui.py and installclass.py (akozumpl)
- gui: remove ics.setScreenNext() and ics.getScreenNext(). (akozumpl)
- Clean up vg name generator and default to "vg_image" in image installs. (dlehman)
- Fix calculation of md array spare count. (dlehman)
- createSuggestedVGName takes a hostname, not a Network instance. (dlehman)
- Show correct device path in PV create progress window. (dlehman)
- VNC does not support runtime SecurityTypes changes (#678150) (mgracik)
- Support cciss devices in get_sysfs_path_by_name(). (akozumpl)
- Don't clear partition 1 from mac disks even if it has no name. (#674105) (dlehman)
- Handle quotes around labels and UUIDs in /etc/fstab. (#670496) (dlehman)
- Clean up a bunch of exception handling code. (dlehman)
- Don't show loaderSegvHandler or its glibc entry point in tracebacks. (pjones)
- The default kickstart UI is graphical, specify other if you want it (#678095). (clumens)
- Only check for the addons of enabled repos (#677773). (clumens)
- Fix build - add Makefiles for new unittests to configure.ac (wwoods)
- Fix a thinko when setting up the base repo for NFSISO (#676821). (clumens)
- Take out the part about anaconda being of little use (#677522). (clumens)
- Fix loading translations in loader (#677648). (clumens)
- Don't always attempt to load updates on kickstart installs (#677131). (clumens)
- s390x has firstboot now (dcantrell)
- Don't fail on missing %includes during loader kickstart processing (#676940). (clumens)
- Prompt for media check on DVD installs (#676551). (clumens)
- Tighten the focus of the dogtail and X try/except blocks. (dlehman)
- Stop overriding ext[234] filesystem defaults. (dlehman)
- Make Storage function in the absence of an Anaconda instance. (dlehman)
- Fix DeviceTree to function in the absence of an InstallInterface. (dlehman)
- Remove some udev hackery that was only needed for two-stage env. (dlehman)
- Move large anaconda.__main__ tasks into functions. (dlehman)
- Generate locale files on request (msivak)
- Fix up tests for changes in split media handling (wwoods)
- Update unit testing targets in Makefile.am (tmlcoch)
- Add new tests from the unittests branch (tmlcoch)
- Fix open method in mock/disk.py. (tmlcoch)
- Improve of mock/disk.py. (tmlcoch)
- Remove the old suite() crud from kickstart testing, python-nose work differenlty (msivak)
- Tag tests as slow or acceptance tests and split full testing from devel unit testing (msivak)
- Mock _isys and block modules in fw test. They are not needed. (msivak)
- In text mode we have to treat strings and lists separately while printing them (#676942) (msivak)
- Fix some whitespace errors in iscsi kickstart code. (pjones)

* Thu Feb 10 2011 Chris Lumens <clumens@redhat.com> - 15.20-1
- Check for valid mountpoint before unmounting image. (#671922) (dlehman)
- Fix mis-management of luks dict when renaming encrypted lvs. (dlehman)
- Don't raise NotImplementedError from  non-essential backend methods.
  (dlehman)
- Remove upgrade.findExistingRoots since it does nothing. (dlehman)
- tui: add reinitializeWindow() to the text interface. (akozumpl)
- typo: missing dot in the reinitialization dialog glade file. (akozumpl)
- gui: remove an unneeded parameter from questionInitializeDisk() (akozumpl)
- Remove quotes from udisks command in liveinst (#672022) (bcl)
- Fix iutil import in bootloader config screen (#676032). (clumens)

* Mon Feb 07 2011 Chris Lumens <clumens@redhat.com> - 15.19-1
- Fix a typo. (clumens)
- Don't write our own udev persistent net rules; use udev's generator.
  (notting)
- Add upd-bootiso script (bcl)
- Fix typo in GPT warning (#675242) (bcl)
- remove unused variables (mschmidt)
- Fix support for "logvol --label=" (#673584). (clumens)
- Fix the taint flag check. (clumens)
- Set default resolution of anaconda.glade to 800x600 (dcantrell)
- Make singlePV a more useful boolean, clean up _getSinglePV() (dcantrell)
- Remove width and height parameters from gui.readImageFromFile() (dcantrell)
- Sort singlePV=True requests so they come first. (dcantrell)
- Move reipl step to be after instbootloader step. (dcantrell)
- Remove 'Change device' button from bootloader screen on EFI systems (#582143)
  (wwoods)
- Add anaconda --version support (#673150). (clumens)
- Remove forced 800x600 geometry switch for Xvnc (dcantrell)
- writeMtab -> makeMtab (#673158). (clumens)
- Let dm_node_from_name admit it's defeated. (akozumpl)
- Disable partition resize support for DASD labels (#605912) (dcantrell)

* Tue Jan 25 2011 Chris Lumens <clumens@redhat.com> - 15.18-1
- GCC seriously needs to be less picky. (clumens)

* Tue Jan 25 2011 Chris Lumens <clumens@redhat.com> - 15.17-1
- Don't call preprocessKickstart from within anaconda as well. (clumens)
- We don't need the command names anymore. (clumens)
- Convert kickstart functions to use Python. (clumens)
- Move all kickstart functions into kickstart.c. (clumens)
- Get rid of the kickstart command codes, and alphabetize the command table.
  (clumens)
- Add the flags required to link against python. (clumens)
- Remove ksReadCommands, convert to using pykickstart for parsing. (clumens)
- Add functions to support interfacing loader with pykickstart. (clumens)
- Fix syntax error from fdd06a4053e2965bdc1719425b6d99fe80ab1e18. (akozumpl)
- Only remove /tmp/updates and /tmp/updates.img if they exist. (clumens)
- YumBackend doesn't inherit from YumBase. AnacondaYum does. (#671577)
  (dlehman)
- After copying live rootfs to root device, grow it to fill the device.
  (dlehman)
- Make sure /boot is mapped to a single LVM PV on s390x (dcantrell)
- Unmount filesystems before shutdown or reboot on s390x (#605577) (dcantrell)
- And update to the latest version of the RAID command. (clumens)
- Make the advanced storage dialogs stay in the foreground. (akozumpl)

* Thu Jan 20 2011 Chris Lumens <clumens@redhat.com> - 15.16-1
- Support passing updates= to liveinst via the boot command line. (clumens)
- Make lighter-weight versions of dm map name/node resolution functions.
  (dlehman)
- Make /etc/mtab a symlink to /proc/self/mounts. (#670381) (dlehman)
- Require the pykickstart version with "raid --label=" support. (clumens)
- No longer run hal-lock on live installs (#670312). (clumens)
- Add support for "raid --label=" (#670643). (clumens)
- self.storage -> storage in kickstart execute methods. (clumens)
- Don't prompt on broken lvm or uninitialized disks in cleanup mode. (dlehman)

* Wed Jan 19 2011 Chris Lumens <clumens@redhat.com> - 15.15-1
- Fix booty error on s390 when /boot is not on LVM. (dcantrell)
- Don't offer minors of ignored md devices when creating new md devices.
  (dlehman)
- Make sure devices ignored by the devicetree are in _ignoredDisks. (dlehman)
- Don't try to add spares to active md arrays. (#652874) (dlehman)
- Fix the traceback from c6228535b26a63b0544f4a558a69076581b2a69f. (akozumpl)
- Those missing mnemonicks will not stand. (akozumpl)
- Provide a new mpath devicelib interface that does not reorder the devices.
  (akozumpl)
- Enable support for static ipv6= cmdline option. (rvykydal)
- mpath: create /etc/multipath/bindings file. (akozumpl)
- Fix DMLinearDevice._postSetup to not take or pass an 'orig' arg. (dlehman)
- There's no more MainframeDiskDevice, so don't call its __str__. (clumens)
- We have to pass a blank argument list to execWithCapture. (clumens)
- We have to mount /boot/efi when we find an old one. (pjones)
- Only allow one EFI System Partition to exist at a time. (pjones)
- Conditionalize use of UEFI on boot.iso (pjones)
- Check fstab entries against fmt.mountType not fmt.type (pjones)
- Fix nfsiso install with options (#667839) (mgracik)
- Split out common code from device setup/teardown/create/destroy for reuse.
  (dlehman)
- Remove createParents methods. They don't do anything. (dlehman)
- Add status/progress ui abstraction to device classes. (dlehman)
- Remove unused code related to device probe methods. (dlehman)
- Suddenly, we need gnome-themes-standard. (akozumpl)
- Bold the warning for GPT on non-EFI (#614585) (bcl)
- Warn the user when using a GPT bootdisk on non-EFI systems (#614585) (bcl)
- Support /boot on logical volume on s390x (#618376) (dcantrell)
- Update example ssh command in linuxrc.s390 (dcantrell)
- Start rsyslogd from linuxrc.s390 (#601337) (dcantrell)
- Update spinbutton value in dialogs (#621490) (bcl)
- Convert livecd.py to use the storage module where appropriate. (dlehman)
- Don't try to teardown the live device or associated loop devices. (dlehman)
- Add flag indicating whether a device can be activated/deactivated. (dlehman)
- Include the livecd OS image devices in the device tree. (dlehman)
- Include file-backed loop devices in the device tree. (dlehman)
- Use sysfs instead of losetup to find loop devs' backing files. (dlehman)
- Clean up and close yum/rpm files once we're done with them. (dlehman)
- logging: log_method_return() for devicetree.getDeviceByName() (akozumpl)
- logging: get rid of storage_log.py (akozumpl)
- mpath: filter out the slave devices and their partitions. (akozumpl)
- mpath: use both 'multipath -d' and 'multipath -ll' to get the topology.
  (akozumpl)
- mpath: remove a harmful udev_trigger() in filter_gui (akozumpl)
- Support enabling repos listed but disabled in /etc/yum.repos.d (#663992).
  (clumens)
- Add /sbin to the $PATH for the shell on tty2. (clumens)
- Make sure to set a self.anaconda reference on data objects too. (clumens)

* Thu Jan 06 2011 Chris Lumens <clumens@redhat.com> - 15.14-1
- Adjust main window size based on install type (#667566) (bcl)
- Remove mknod-stub.  We have the full one around now. (clumens)
- Use a different method to get the sysfs_path for device-mapper devices
  (#665643). (clumens)
- Allow existing /var/log (bcl)

* Wed Dec 22 2010 Chris Lumens <clumens@redhat.com> - 15.13-1
- Fix a syntax error in f16a565aa3a879a94862f4c3e5b2ede792ed05ef. (clumens)
- Pass --noeject to anaconda (#477887) (bcl)

* Wed Dec 22 2010 Chris Lumens <clumens@redhat.com> - 15.12-1
- Use cio_ignore and *_cio_free commands in linuxrc.s390 (#633469) (dcantrell)
- Add /sbin/cio_ignore to the KEEPFILE list on s390x (dcantrell)
- Remove MainframeDiskDevice class, use description property. (dcantrell)
- Focus the dialog after a message window is closed (mgracik)
- Change the device reinitialization dialog (mgracik)
- Rename anaconda-image-cleanup and use it for all cleanup in liveinst.
  (dlehman)
- Add handling for cleanup of luks devices with unexpected map names. (dlehman)
- Add ability to clean up prior to live install. (dlehman)
- Fix looking up storage device IDs when writing out anaconda-ks.cfg (#591713).
  (clumens)
- Don't write out a duplicate mtab to /mnt/sysimage (#568539). (clumens)
- Raise an exception if X*Display functions fail (#663294). (clumens)
- mpath: make sure /var/log exists exists early. (akozumpl)
- mpath: log the /etc/multipath.conf contents (akozumpl)

* Tue Dec 14 2010 Chris Lumens <clumens@redhat.com> - 15.11-1
- Don't crash if losetup doesn't know anything about a device. (#662513)
  (dlehman)
- Set up disk images earlier so kickstart device filtering works on them.
  (dlehman)
- Don't try to parse network device info when doing disk image installs.
  (dlehman)
- Fix DeviceTree cleanup w/ inactive luks devs in cmdline mode. (dlehman)
- Add losetup to the install image, re-remove it from isys (#662183). (clumens)
- "anaconda" -> "self.anaconda" in kickstart execute methods. (clumens)
- Override the BaseHandler.dispatcher method. (clumens)
- Use chreipl to set the IPL device on s390x (#632325) (dcantrell)
- Add /usr/sbin/chreipl to KEEPFILE. (dcantrell)
- Create a MainframeDiskDevice class for common s390 attributes. (dcantrell)
- Do not shut down zFCP storage in Storage.shutdown() (#612626) (dcantrell)
- Clarify the ssh modes for installation on s390x (#621590). (dcantrell)
- devicelibs/mpath.py: do not rely on other modules to import logging.
  (akozumpl)
- filter_gui: device discovery configuration is under anaconda.storage.config.
  (akozumpl)

* Wed Dec 08 2010 Chris Lumens <clumens@redhat.com> - 15.10-1
- Fix the build. (clumens)

* Wed Dec 08 2010 Chris Lumens <clumens@redhat.com> - 15.9-1
- Set installer environment hostname for sw raid LABELs (#640743) (rvykydal)
- Device destroy actions can only require other destroy actions. (#651589)
  (dlehman)
- Use wipefs from util-linux-ng instead of dd to wipe old sigs. (dlehman)
- Add cleanup-only mode to DeviceTree.populate. (dlehman)
- Add unit tests for storage.partitioning.getNextPartitionType. (dlehman)
- Only try logging to tty3 if we have permission to do so. (dlehman)
- Enable network when getting .treeinfo (#632526) (rvykydal)
- Fix default of network --device option to match rhel5 (#647462). (rvykydal)
- Do not backtrace if repo is specified through kickstart only (#659781).
  (akozumpl)
- Restore list-harddrives output to what users expect (#654436) (dcantrell)
- Permit ext4 and ext2 for /boot on s390x (#638734) (dcantrell)
- Check for ARPHRD_ETHER and ARPHRD_SLIP types in getDevices (#596826)
  (dcantrell)
- Preserve and otherwise ignore noauto fstab entries. (#660017) (dlehman)
- Fix "logvol --percent=" (#651445, jruemker). (clumens)
- Add chroot command to bash_history. (pjones)
- support for partial offload in udev_*_iscsi() functions. (akozumpl)
- iscsi: partial offload drivers. (akozumpl)
- analog: put it under /usr/bin so it's on the path in an installed system.
  (akozumpl)
- Remove commented out broken code from LoopDevice.status. (dlehman)
- Don't traceback when the action list is empty. (#657891) (dlehman)
- Remove unused udev_device_is_{multipath,dmraid}_partition functions.
  (dlehman)
- Set dm-uuid for anaconda disk image devices from devicetree. (dlehman)
- Remove some unnecessarily hard-coded "/dev/mapper" strings. (dlehman)
- Put the backend logger's config file in /tmp. (dlehman)
- Move handling of /proc/bus/usb and /selinux into storage. (dlehman)
- swapoff -a is only needed for livecd, so only do it for livecd. (dlehman)
- Unlink backend logger config file when stopping logger. (dlehman)
- Make FileDevice.path more consistent. (dlehman)
- Add support for detecting already-active lvm. (dlehman)
- Fix addUdevDevice so we can actually handle already-in-tree devices.
  (dlehman)
- Make it possible to ignore md-fwraid member disks. (dlehman)
- Revert rpmdb symlink hack. (dlehman)
- Remove some unused code from storage.devicelibs.dm. (dlehman)
- Add support for installing onto block device image files. (dlehman)
- Generalize some of the device-mapper partition handling. (dlehman)
- Add support for loop devices. (dlehman)
- Add support for linear device-mapper devices. (dlehman)
- Fix PartitionDevice.path to work with device-mapper disks. (dlehman)
- There's no need to pass exclusiveDisks to doPartitioning separately.
  (dlehman)
- Move storage device scanning parameters into a separate class. (dlehman)
- Don't ignore %packages if --default is given (#621349, dcantrell). (clumens)
- Don't traceback when displaying %post error messages (#654074). (clumens)
- Display a warning message on TAINT_HARDWARE_UNSUPPORTED (#623140). (clumens)
- If getting .treeinfo fails, try treeinfo (#635065). (clumens)
- instPath -> rootPath (clumens)
- Add rdate, tty, which to install image (mgracik)
- Don't add --enablefingerprint unless fprintd-pam is installed (#656434).
  (clumens)

* Tue Nov 30 2010 Chris Lumens <clumens@redhat.com> - 15.8-1
- Ignore immutable disks in clearPartitions (#657115) (bcl)
- Add biosdevname to installer environment (Matt_Domsch)
- Add ntpdate to install.img (#614399) (mgracik)
- It's /usr/bin/gdbserver. (akozumpl)
- Handle dm-N devices pointed to by /dev/disk/ paths (#605312) (bcl)
- Resolve /dev/disk/ devices during rescue (#605312) (bcl)
- Do not auto-check all drives when creating a RAID partition (#641910).
  (akozumpl)
- (Un)select all button in Partition Editor. (akozumpl)
- Show the total amount of space used by snapshots in the VG editor dialog.
  (dlehman)
- Add support for detecting lvm vorigin snapshot volumes. (#633038) (dlehman)
- Don't display free space at end of extended unless > 1MB. (#626025) (dlehman)
- Set SELinux context on /etc/localtime (#653867). (clumens)
- Get a little more output from the unittest runner. (clumens)
- Remove writeRpmPlatform, adjust callers. (#651132, #650490) (notting)
- Import as "pyanaconda.anaconda_log", not "anaconda_log". (clumens)
- A little too much got deleted from imount.c. (clumens)
- Remove the popping portion of kickstart %pre script notification. (clumens)
- Add pyanaconda/.libs to the PYTHONPATH for pylint. (clumens)
- Ignore several false positives and import errors while running pylint.
  (clumens)
- Remove the parts required to make "make tests" work. (clumens)
- nosetests will only run tests if they are not executable and end in _test.py.
  (clumens)
- Set up the PYTHONPATH for running nosetests. (clumens)
- tsort_dict -> tsort in the test case. (clumens)
- Return mount's actual error codes instead of obfuscating them. (dlehman)
- Remove log message saying we don't know how to sanity check storage.
  (dlehman)
- Move check for ext2 filesystem journal from FS to Ext2FS. (dlehman)
- Remove mkdirChain() from isys, use g_mkdir_with_parents() (dcantrell)
- Do not force -O2 in CFLAGS. (dcantrell)
- Remove unused unpackCpioBall() function. (dcantrell)
- Use unpack_archive_file() instead of unpackCpioBall() (dcantrell)
- Use libarchive helper functions in explodeRPM() (dcantrell)
- Add libarchive helper functions for loader in unpack.c (dcantrell)
- Remove include lines for stubs.h from isys. (dcantrell)
- Remove isys cpio extraction code. (dcantrell)

* Tue Nov 09 2010 Chris Lumens <clumens@redhat.com> - 15.7-1
- Unset bootloader password checkbox (#650865) (bcl)
- Fix typo in my ctc commit (#648858) (bcl)
- Fix ctc check logic (#648858) (bcl)
- timezones: fix a scrolling problem with the scdate's GUI TreeView. (akozumpl)
- timezones: remove unneeded imports (akozumpl)
- Fix variable substitution in kickstart files (bcl)
- Don't show the cleardisk dialog on upgrades (#649865). (clumens)
- Use a stronger RNG for password salt (mitr)
- Use SHA-512 for bootloader password encryption (mitr)
- Support grub --encrypted when set from kickstart (mitr, #554874). (clumens)
- use different approach to tweak gconf settings in the image (#642358).
  (akozumpl)
- Allow loader to re-prompt for networking when network activation fails
  (jlaska)
- Support devices larger than 1.5TB (#649095, rspanton AT zepler DOT net).
  (clumens)
- Fix test for CTC devices from yesterday. (clumens)
- iscsi, logging: reuse the global ISCSID in has_iscsi(). (akozumpl)
- iscsi: refactor the kickstart processing to use the new iscsi methods.
  (akozumpl)
- Do not rely on presence of DEVICE setting in ifcfg files. (rvykydal)
- Do not sort settings in ifcfg file. (rvykydal)
- Remove obsolete networking code. (rvykydal)
- Support installation to CTC devices in loader (#648858, karsten). (clumens)
- Add more modules to the list of things liveinst must load. (clumens)
- Don't look for a CD number in readStampFileFromIso. (clumens)
- mediaCheckCdrom now supports checking only one piece of media. (clumens)
- Remove support for writing disc number info to .treeinfo and .discinfo.
  (clumens)
- Remove support for split media transactions from yuminstall.py. (clumens)
- Remove unused currentMedia parameter. (clumens)
- mediaHandler no longer needs to worry about mounting anything. (clumens)
- Rework _switchCD and _switchMedia for a one-image world. (clumens)
- umountImage shouldn't care about currentMedia. (clumens)
- Remove presentRequiredMediaMessage and related code. (clumens)
- Rename findIsoImages to findFirstIsoImage. (clumens)
- verifyMedia no longer looks at the disc number. (clumens)

* Fri Oct 29 2010 Chris Lumens <clumens@redhat.com> - 15.6-1
- We now need to BuildRequire dbus-python. (clumens)

* Fri Oct 29 2010 Chris Lumens <clumens@redhat.com> - 15.5-1
- ui: mnemonics for autopartitioning type. (akozumpl)
- hwclock lives in /sbin now. (akozumpl)
- timezone_text.py: remove the commented out parts and never called methods.
  (akozumpl)
- gui: remove "swapped" attribute from anaconda.glade (akozumpl)
- Errors downloading .treeinfo files should not be logged as errors. (clumens)
- When we can't fetch group metadata, log why. (clumens)
- Log which step we're on in doLoaderMain. (clumens)
- On upgrades, inform the user what action is taking place (#493249). (clumens)
- Fix import to not drag in a conflicting ConfigParser. (clumens)
- If there are any troubles reading the treeinfo file, return no addons.
  (clumens)
- Only build EFI images on x86_64 (jlaska, #646869). (clumens)
- restart-anaconda: full path to iscsiadm (akozumpl)
- iscsi: ISCSID needs to be declared global in has_iscsi() (akozumpl)
- Fix two problems with initrds for multipla kernels during a pungi compose.
  (akozumpl)
- Fix the locale value for Bengali (India) (mgracik)
- specfile: anaconda requires GConf2 during runtime. (akozumpl)
- timezones: use more of s-c-date (#520631). (akozumpl)
- Don't hardcode the sshd location, either. (clumens)
- Move StorageTestCase into its own file for use by other tests. (dlehman)
- Actions' devices must be in the tree except for ActionCreateDevice. (dlehman)
- Fix StorageDevice.resizable to check self.format.type, not self.format.
  (dlehman)
- Cleanup some preconditions in DeviceAction constructors. (dlehman)
- Add device action test suite. (dlehman)
- Fix test environment python path. (dlehman)
- Reimplement action pruning and sorting using tsort and action deps. (dlehman)
- Add requires and obsoletes methods to DeviceAction classes. (dlehman)
- Add a topological sort implementation for use in sorting device actions.
  (dlehman)
- Only log storage to tty3 if we have permission to do so. (dlehman)
- Remove PartitionDevice.path hack. (dlehman)
- Use 'name' instead of 'device' for device name ctor arg in all Device
  classes. (dlehman)
- Qualify devicelibs.lvm instead of relying on namespace clutter. (dlehman)
- Make the various DeviceAction.isFoo methods into properties. (dlehman)
- Establish a unique id for each DeviceAction instance. (dlehman)
- Add logpicker to keepfile list in upd-instroot. (tmlcoch)

* Thu Oct 21 2010 Chris Lumens <clumens@redhat.com> - 15.4-1
- Allow importing product.py in places where you won't have a .buildstamp.
  (clumens)
- Search for iscsid in the $PATH, not in a hardcoded list of places (#645523).
  (clumens)
- Use glib for getPartitionsList() (dcantrell)
- Include the SELinux policy file, not just the directory. (clumens)
- Remove the last references to install.img. (clumens)
- Properly identify device-mapper partitions set up by kpartx. (#644616)
  (dlehman)
- Don't ever try to mount ntfs filesystems. (#637319) (dlehman)
- We don't need to worry about 2.4 -> 2.6 updates anymore. (clumens)
- scsiWindow is unused.  Kill it. (clumens)

* Mon Oct 18 2010 Chris Lumens <clumens@redhat.com> - 15.3-1
- Don't recommend /usr as a mount point anymore (#643640). (clumens)
- Add some debugging prints. (clumens)
- Don't prompt for kbd, lang, or network on CD/DVD installs. (clumens)
- We no longer need to copy the install.img over and lochangefd to it.
  (clumens)
- Also rework image loading for CD/DVD installs. (clumens)
- Remove a bunch of unused support functions. (clumens)
- Use parseDeviceAndDir instead of reimplementing the same things two more
  times. (clumens)
- Rework how image loading works for HD installs. (clumens)
- Remove the unused mountNfsImage and all code that was only called by it.
  (clumens)
- Rework how image loading works for NFS installs. (clumens)
- Remove the unused iurlinfo, urlInstallData, and fix up URL kickstarts.
  (clumens)
- Initialize loaderData->method. (clumens)
- Remove the unused mountUrlImage function. (clumens)
- Rework how loading images works for URL installs. (clumens)
- urlinstTransfer and support functions do not operate on iurlinfo anymore.
  (clumens)
- urlMainSetupPanel no longer takes an iurlinfo. (clumens)
- Deprecate stage2=, keep method= as it's been for a long time now. (clumens)
- migrate_runtime_directory no longer does anything useful. (clumens)
- Remove the method selection block from the beginning of doLoaderMain.
  (clumens)
- Fix up copying of firmware. (clumens)
- Correct paths of things started by loader/init that have moved. (clumens)
- Step 3 of merging installer images:  No longer create install.img. (clumens)
- makeinstimage is no longer used. (clumens)
- instbin is no longer used. (clumens)
- A couple minor changes to mk-images. (clumens)
- Step 2 of merging installer images:  Move most everything out of makeinitrd.
  (clumens)
- Step 1 of merging installer images:  Don't copy files into a new root.
  (clumens)
- No longer do the bin -> usr/bin copy song and dance. (clumens)
- Fix typo in examine_gui.py (bcl)
- Clean up tabs in examine_gui.py (bcl)
- Rework proxy handling so that .treeinfo also uses proxy (#634655) (bcl)
- Translate task and repo names based on the product.img (#622064). (clumens)
- Use baseurl instead of methodstr to get .treeinfo (#604246) (rvykydal)
- Be more resilient to config files missing sections and options (#590591).
  (clumens)
- Add repos for all addons in all enabled repositories (#580697). (clumens)
- Add a method that fetches and returns the .treeinfo file. (clumens)
- All uses of perl must die. (clumens)

* Thu Oct 14 2010 Chris Lumens <clumens@redhat.com> - 15.2-1
- And remove welcome_{gui,text}.py from the translations too. (clumens)
- A block quote in the middle of a python file does nothing. (clumens)
- Fix traceback after Delete in nm-c-e (#642370) (rvykydal)
- Fix ifcfg logging message. (rvykydal)
- Fix porting of ifcfg logging. (rvykydal)
- Rescan disks when moving back through upgrade check (#635778) (bcl)
- anaconda: Disable X server regenerations (#609245) (ajax)
- Attempt to bring the network up before saving a bug report (#635821).
  (clumens)
- No one likes the welcome step anymore, so remove it. (clumens)
- iscsi, cosmetic: fix grammar in the iscsi dialogs. (akozumpl)
- iscsi: call iscsi.stabilize() at the end of the iscsi configuration.
  (akozumpl)
- iscsi: consolidate logging in the UI (akozumpl)
- iscsi: allow separate discovery/login credentials in TUI. (akozumpl)
- iscsi: migrate the CRED_ constants and parse_ip() to partIntfHelpers.
  (akozumpl)
- iscsi gui: use abstract methods in the iSCSIWizard interface. (akozumpl)
- iscsi gui: factor out the drive adding code. (akozumpl)
- iscsi gui: make the iSCSI wizard never return gtk constants. (akozumpl)
- isci: typo in a GUI checkbox (akozumpl)
- Add logpicker support into Makefiles, anaconda.spec.in, configure.ac and upd-
  instroot. (tmlcoch)
- Add logpicker tool into utils (tmlcoch)
- gui: hide text in the proxy password field (#611825). (akozumpl)
- logging: be smarter logging UI module import errors. (akozumpl)
- text.messageWindow(): make it more resilient to the input. (akozumpl)
- Log that we are running %pre scripts to the console (#640256). (clumens)
- Preset default config for immediate Close in nm-c-e enablement (#636526)
  (rvykydal)
- Fix non-dhcp network enablement in stage 2 (#640951) (rvykydal)
- Set focus after error message (#611430) (tmlcoch)
- When upgrading a package instead of installing, say so (#636520, jlaska).
  (clumens)
- Do a better job of explaining how much memory is required to install
  (#639056). (clumens)
- Get rid of mountLoopback and umountLoopback. (clumens)
- copyright notice in add_drive_text.py (akozumpl)
- restart-anaconda: log out of all iscsi nodes (akozumpl)
- remove EXN_ constants from constants.py (akozumpl)
- Honor selected hostname on Live CD (#638634) (rvykydal)
- Do not try to prompt for network for escrow in kickstart (#636533) (rvykydal)
- Sync up list of languages with contents of po/ directory. (clumens)
- Fix a storage logging import (#636621). (clumens)
- Fix a couple pylint-found errors. (clumens)
- Copy ifcfg.log into traceback and target system. (rvykydal)
- Improve logging of ifcfg stuff. (rvykydal)
- Refactor DNS resolver reset. (rvykydal)
- Add placeholders to ambiguous python strings (#634385). (clumens)
- Dynamically initialize MALLOC_PERTURB_ when loader starts. (pjones)
- btrfs will be a supported filesystem in F15 (josef). (clumens)
- Fix setting of $HOME (pjones)
- Limit progress bar amount to 1.0 (bcl)

* Fri Sep 24 2010 Chris Lumens <clumens@redhat.com> - 15.1-1
- Properly rescan storage with Reset in partition GUI (#635778) (bcl)
- Save the partition type selection when moving back (#635778) (bcl)
- Properly rescan disks when moving back (#635778) (bcl)
- Reset resolver after network device activation (#632489) (rvykydal)
- Don't include the product name in the translation (#636415). (clumens)
- Clarify loopback mount log message (#633444). (clumens)
- pykickstart now raises KickstartError instead of IOError. (clumens)
- Fix EFI bootloader install problems (#635873, #635887) (bcl)
- Re-add cleardiskssel step when autopart is chosen. (#635332) (dlehman)
- Pull boot splash image from correct location (#635330) (bcl)
- Add files for polkit to initrd.img (#633315) (rvykydal)
- Remove old kernels with new bootloader (#633234) (bcl)
- Both the inittab and systemd sections can return. Move this part earlier.
  (notting)
- iscsi: discovery and node login wizard. (akozumpl)
- Pass xdriver to anaconda in liveinst (#633827) (bcl)
- Add test cases for the new Size class. (dcantrell)
- Add exceptions specific to the new Size class. (dcantrell)
- Create Size class for specifying device and fs sizes. (dcantrell)
- Fix importing the netconfig UI in rescue mode (#632510). (clumens)
- Add noeject support to cdrom eject handling (#477887) (bcl)
- Cleanup tabs in flags.py (bcl)
- Add noeject support to loader (#477887) (bcl)
- Remove BETANAG, instead reading it from .buildstamp (#628688). (clumens)
- Convert .buildstamp into a .ini-style file. (clumens)
- Remove productPath. (clumens)
- Remove any /tmp/yum.log that may be present on the installed system
  (#630327). (clumens)
- If the filesystem doesn't support resize, there's no resizesb (#627153).
  (clumens)
- Run anaconda in fullscreen mode. (clumens)
- minor: gtk.CellRendererText has no property 'active'. (akozumpl)
- restart-anaconda: kill iscsid too (akozumpl)
- ui: fix the default choice in the 'advanced storage options' dialog.
  (akozumpl)
- iscsi: rename variable in addIscsiDrive. (akozumpl)
- ui: a couple of storage mnemonics. (akozumpl)
- updates: .glade files are in data/ui now. (akozumpl)
- Re-fix systemd default link (#627401, mschmidt). (clumens)
- Remove losetup and unlosetup from isys (bcl)
- Remove losetup usage (bcl)
- Various upd-instroot cleanups, most importantly for firstaidkit (#627758).
  (clumens)
- Shrink locale-archive down to just what we support. (clumens)
- Remove the icon-theme.cache file from the initrd. (clumens)
- Remove /etc/selinux/targeted/modules/active from the initrd (clumens)
- Remove the DRI modules from the initrd. (clumens)
- i18n: do not build translatable sentences from parts (#622545). (akozumpl)
- memory: install.img is now >150 MB so count 192 MB extra for it. (akozumpl)
- memory: check_memory() displays GUI dialog on livecd (#624534). (akozumpl)
- readvars should split variables into at most 2 pieces (bcl)
- Adding output to method selection process (bcl)

* Fri Aug 27 2010 Chris Lumens <clumens@redhat.com> - 15.0-1
- systemd symlinks now reside in /lib (#627401). (clumens)
- filtering UI: don't be picky about udev wwid length. (akozumpl)
- mpath: put quotes around the wwids, they can have spaces. (akozumpl)
- Use blacklist_exceptions for mpath devices (#612399) (mfuruta)
- typo: repeated line in lvm.py (akozumpl)
- mpath: do not deactivate mpath device upon its teardown. (akozumpl)
- mpath: teardown format from MultipathDevice.teardown() (#616273). (akozumpl)
- And change the tigervnc requires in the spec file too. (clumens)
- Kill joe. (pjones)
- Require tigervnc-server-minimal to remove perl from livecd (#627280).
  (clumens)
- Use ID_SERIAL_RAW for multipath, if available (#626842). (clumens)
- mpath: filter member partitions wiser in lvm. (dcantrell)
- mpath: do not deactivate mpath partitions in teardown(). (akozumpl)
- Fix comparison between /dev/disk/* paths and udev symlinks (#621515).
  (clumens)
- Remove telnetd.h from POTFILES.in so make works again. (clumens)
- Reset labels on /var/cache/yum as well (#623434). (clumens)
- NetworkManager uses a different config file now (#623937). (clumens)
- Don't touch resolv.conf which is handled by NM (#622927) (rvykydal)
- logging: turn the loglevels into proper enum. (akozumpl)
- loader: parseCmdLineIp* takes just the value as an argument now. (akozumpl)
- logging: refactor printLogHeader (akozumpl)
- Remove the nousbstorage command line option (#624556). (clumens)
- Remove telnet support. (dlehman)
- Allow omission of --size for partitions, use default size. (dlehman)
- Fix the provides we look for when installing DUD (#618862) (msivak)
- Fix the paths for DD in postinstall phase Related: rhbz#619745 (msivak)
- Remove the final use of $LOADERBIN from scripts. (clumens)
- Only set noverifyssl on URL installs (#621469). (clumens)
- Base install/upgrade default on whether any candidates were found (#590505).
  (clumens)
- fix 899f401611da021b3ec3882577ad860eae47f265 (akozumpl)
- Do not use autoconfiguration for DHCPv6 (#623216) (rvykydal)
- Add scripts/githooks/ with commit-msg script. (dcantrell)
- I don't need to pass "nomodeset" to stage2 after all. (clumens)
- After cancelled stage 2 network enablement remove temporary repo (#623639)
  (rvykydal)
- Fix traceback when using duplicate name for added/edited repo (#623080)
  (rvykydal)
- Fix traceback after Cancel in stage 2 network enablement dialog (#623017)
  (rvykydal)
- Make sure "nomodeset" and "xdriver=" get passed on to stage2 (#623129).
  (clumens)
- We checked for updated driver with wrong path prefix (#619745) (msivak)
- Proper detection of successful module update (#618862) (msivak)
- LVM and LUKS now align everything to 1MB boundaries. (#623458) (dlehman)
- Clearing of formatting from unpartitioned disks belongs in clearPartitions.
  (dlehman)
- Do disklabel handling for whole disk formats unknown to anaconda (#619721)
  (hdegoede)
- Do not support "part --grow raid.XX" (#577432). (clumens)
- Update systemd's default.target for the desired runlevel (#623102, mschmidt).
  (clumens)
- Skip cleardiskssel on custom partitioning (#620647). (clumens)
- logging: typo in analog (akozumpl)
- logging: fix logic in getSyslog(). (akozumpl)
- Use full EFI path to map drives for grub (#598572) (bcl)
- Don't complain about upgrading the same release (#620953) (bcl)
- Don't crash on unnamed installs (#621685) (bcl)
- mpath: add MultipathDevices first, before their partitions. (akozumpl)
- ibft: always configure network devices if there's ibft available (#617860).
  (akozumpl)
- Log exclusiveDisks, ignoredDisks, and reasons for ignoring devices. (dlehman)
- Include mpath/fwraid member devices in exclusiveDisks. (dlehman)
- Use part instead of device in PartitionWindow.populate() (#575749)
  (dcantrell)
- Add support for ipv6 to text UI network enablement (#612476) (rvykydal)
- Remember user's choice when going back in Configure TCP/IP (#609570)
  (rvykydal)
- Update generating of anaconda-ks.cfg for ipv6. (rvykydal)
- Update ks network command for ipv6 in anaconda. (rvykydal)
- Fix typo and set mpaths' sysfs path before querying udevdb. (#620712)
  (dlehman)
- The --loaderbin parameter to makeinitrd is unused.  Kill it. (clumens)
- services is a set, not a list (#620900, akozumpl). (clumens)
- Set AUTO_VLAN=yes in fcoe config files (#618875) (dcantrell)
- The --initrdsize parameter to makeinitrd is unused.  Kill it. (clumens)
- Honor bootdrive selection when autopartitioning (#620442) (hdegoede)
- shutdown: Use lstat to test for /lib64 (hdegoede)
- shutdown: don't unmount /sys and /proc (hdegoede)

* Mon Aug 02 2010 Chris Lumens <clumens@redhat.com> - 14.14-1
- Write out correct nfs url for repo= in /root/anaconda-ks.cfg (#584580)
  (rvykydal)
- mdadm -I no longer accepts --no-degraded (#620359) (hdegoede)
- Update buildinstall because of new man package name (mgracik)
- Clarify name of function that identifies biosraid member devices. (dlehman)
- Use dm subsystem functions to identify dmraid,mpath partitions. (dlehman)
- Move disk enumeration to a method of FilterWindow. (dlehman)
- Check if an mpath should be ignored before adding it to the devicetree.
  (dlehman)
- Add handling for mpath and fwraid devices in exclusiveDisks. (dlehman)
- Add functions to identify specific types of device-mapper devices. (dlehman)
- Ignore active fwraids and mpaths when setting up the filter ui. (dlehman)
- Include pyconfig*.h so that we can actually run python2.7 . (pjones)
- Remove translation of error strings in uncpio.c (bcl)
- Clean up tabs in uncpio.c (bcl)
- Redirect uncpio errors to syslog (#618181) (bcl)
- Make sure multipathd starts on systems using mpath storage (#615040)
  (dcantrell)
- Handle systems where all disks have a whole disk format (#617554) (dcantrell)
- Include modprobe file for Mellanox 10GB driver (#611997) (dcantrell)
- Remove some more kickstart duplication (#617512). (clumens)
- Fix setup of LVs (bcl)
- Include the kickstart file in the traceback (bcl)

* Tue Jul 27 2010 Ales Kozumplik <akozumpl@redhat.com> - 14.13-1
- Use readvars_parse_file in loader/init.c (dcantrell)
- Use readvars_parse_*() in loader/loader.c (dcantrell)
- Use readvars_parse_file() in loader/modules.c (dcantrell)
- Add readvars.c for parsing command line args and shell vars. (dcantrell)
- Check return value of chdir() (dcantrell)
- Remove handling for the "vesa" boot argument. (dcantrell)
- Remove USE_MINILIBC cruft from loader/init.c (dcantrell)
- Whitespace cleanup in loader/Makefile.am (dcantrell)
- logging: remote logging for traceback dumps. (akozumpl)
- logging: also log X.log remotely (akozumpl)
- logging: autodetect the virtio-serial port. (akozumpl)
- does not properly recognize hpt45x_raid_member (#617438) (hdegoede)
- Show allowable prepboot size range in exception (#603188) (dcantrell)
- Remove storage init duplication (#6176512). (clumens)
- Skip the Filter UI in Basic Storage mode (#598420) (hdegoede)
- Make the shell in tty2 and ssh all go to /root like on a real system.
  (pjones)

* Thu Jul 22 2010 Ales Kozumplik <akozumpl@redhat.com> - 14.12-1
- Only write changed DASD attributes to rd_DASD params (#606783) (dcantrell)
- Propagate MACADDR from loaderData to iface (#595388) (dcantrell)
- Deal with media only for media repo package failures (#573492) (rvykydal)
- Support for ks: --ipv6 command, and ipv6 values for --gateway (#490794)
  (rvykydal)
- analog: support reading the installation logs from a unix socket. (akozumpl)
- logging: support logging through virtio-serial (#576439). (akozumpl)
- modules.c: only log from _doLoadModule() if logging has been initialized.
  (akozumpl)
- break the dependency of modules.c on loader.h (akozumpl)
- Enforce limits on partition start/end sectors. (dlehman)
- Fix up import to make rescue mode work again (#616090). (clumens)
- Init g_type in is_wireless_device. (rvykydal)
- Add resolver reset to some network enablement places (#614001) (rvykydal)
- Fix config of ipv6 and ipv4 (auto + manual) in loader (#609576) (rvykydal)
- text: remove the needless complexity in the screen switching loop. (akozumpl)
- text.py: do not traceback when can't go back (#598493). (akozumpl)
- remove doShutdownX11Actions(). (akozumpl)
- Add uname to initrd.img (#614770) (dcantrell)
- Some people like to specify MAC addresses in lower case. (clumens)
- Remove support for interactive kickstart installs. (clumens)
- Improve parsing and pass the devel flag to loader through the command line
  (msivak)
- When in devel mode, do not catch tracebacks, we want the core file (msivak)
- Add better debugging capabilities to loader (msivak)
- Add confirmation dialog when loading dlabel DDs (#570053) (msivak)

* Wed Jul 14 2010 Chris Lumens <clumens@redhat.com> - 14.11-1
- Add the gobject-introspection package (#613695) (mgracik)
- Update pylint test for pylint 0.20.1 (bcl)
- Use long ints for comparisons, not floats (#608172) (bcl)
- Enforce the same logic on autopart shrink as on resize (#608172) (bcl)
- Don't crash when putting mpath devices into the filter name cache (#597223).
  (clumens)
- Handle serial = None in the right place (#613623). (clumens)
- There's still no instdata on master (#613075). (clumens)

* Thu Jul 08 2010 Chris Lumens <clumens@redhat.com> - 14.10-1
- Handle 16 digit hex strings for ID_SERIAL_SHORT (#611554) (dcantrell)
- Focus default advanced storage type in add dialog (#603726) (dcantrell)
- Add multipath member with addUdevDiskDevice instead of DiskDevice (#582254)
  (dcantrell)
- add mime.cache to the stage2 image (#609596). (akozumpl)
- makeupdates: treat files under pyanaconda/ individually. (akozumpl)
- ssl: propagate 'url --noverifyssl' into yum repo configuration (#599040).
  (akozumpl)
- ssl: support for 'url --noverifyssl' in loader. (akozumpl)
- ssl: support --noverifyssl in the repo kickstart command. (akozumpl)
- Fix a file descriptor leak in getDevices (#612153, mganisin). (clumens)
- Pass size of structure not a size of pointer to calloc (#592227) (msivak)
- Properly iterate over the netdevices list (#610769). (clumens)
- Require the static package instead of the devel one (#610797). (clumens)
- ui: C_reate mnemonics in Create Storage dialog. (akozumpl)
- fix insensitivities of 0783c488 (akozumpl)
- During an update don't erase old kernels (#594411) (bcl)
- booty and isys have moved, so update runpylint.sh. (clumens)
- Translate MAC addresses to devices in the second stage, too. (clumens)
- Fix prototype of getIPAddresses (#605659) (rvykydal)
- Account for ipv6 addresses too (#605659) (rvykydal)
- Use progressbar instead of waitwindow for repo setup (#584996) (rvykydal)
- Don't deactivate active device before running nm-c-e (#608773) (rvykydal)
- Control all devs by NM by default + filtering (iSCSI, FCoE) (#606745)
  (rvykydal)
- anaconda's lvm vgreduce invocation is not filtering out disks (609479)
  (hdegoede)
- Clean up proxy handling in yuminstall.py (#604137) (bcl)
- Write out missing space on 'part' lines in ks file (#605938) (dcantrell)
- Make sure swap devices are included in dracut args (#607646) (dcantrell)
- Catch DeviceNotFoundError in cleardisks (#607661) (dcantrell)
- Do not proceed after partitioning errors in text mode (#599484) (bcl)
- fixup exclude/excludepkgs usage (#607664) (bcl)
- yum calls it "exclude" instead of "excludepkgs" (#607664). (clumens)
- Add full proxy URL to writeKS (#602705) (bcl)
- Fix repo --includepkgs=, and add more to anaconda-ks.cfg's repo line
  (#602705). (clumens)
- Add a slash to the path pointing to hdinstall dir (#592154) (msivak)
- Don't resize lv's formatting unless also resizing the lv. (#575046) (dlehman)
- Show sane non-removable drives too in the DD dialog (#594548) (msivak)

* Mon Jun 28 2010 Chris Lumens <clumens@redhat.com> - 14.9-1
- Update to use the latest pykickstart. (clumens)
- Import anaconda_log correctly to avoid the double import problem. (clumens)
- Move isys and booty into the pyanaconda/ directory, adjust paths to match.
  (clumens)
- network.dracutSetupstring: properly handle ipv6 (#605232) (hdegoede)
- Support for converged traffic during install to FCoE LUN (#604763) (hdegoede)
- Take into account the fact that some formats have no min/max size. (dlehman)
- Put dhcp configuration files in /etc/dhcp (#468436) (dcantrell)
- Autopart PVs require enough space for a default-sized partition. (dlehman)
- Enforce format min/max size for fixed-size requests. (dlehman)
- Fix min/max size definitions for PReP Boot format class. (dlehman)
- Constrain lvmpv, mdmember, and swap partitions to a single disk. (#605756)
  (dlehman)
- Enforce maximum start sector for partitions. (#604059) (dlehman)
- Handle nm-c-e using prefix instead of netmask (#607762) (hdegoede)
- Handle "(#BUGNUM, author)" in git log summary lines. (dcantrell)
- Allow running an alternate program from liveinst. (clumens)
- fix network.py syntax error. (akozumpl)
- modules: make iscsi and similar imports look less ridiculous (akozumpl)
- modules: fix getlangnames. (akozumpl)
- updates: link files in also on lower directory levels. (akozumpl)
- modules: dont treat booty special. (akozumpl)
- modules: dont treat isys special. (akozumpl)
- modules: necessary changes to the import statements under pyanaconda/textw
  (akozumpl)
- modules: a change to an import statements in isys/ (akozumpl)
- modules: necessary changes to the import statements under pyanaconda/iw
  (akozumpl)
- modules: changes to the import statements directly under pyanaconda/
  (akozumpl)
- modules: necessary changes to the installclasses import statements.
  (akozumpl)
- modules: necessary changes to the import statements under booty/ (akozumpl)
- modules: necessary changes to the import statements under storage/ (akozumpl)
- modules: pyanaconda.textw and pyanaconda.iw are now regular modules.
  (akozumpl)
- modules: remove the hacks in setupPythonPath(). (akozumpl)
- Be specific when telling lvm to ignore devices. (dlehman)
- analog: fix options.output traceback (akozumpl)
- Handle questionInitializeDASD in cmdline mode (#605846) (dcantrell)
- Set SELinux context on dasd.conf and zfcp.conf (#605597) (dcantrell)
- Add --fsprofile= to the anaconda-ks.cfg (#605944). (clumens)
- Add the proxy tests to the top-level test framework. (clumens)
- Fix pyanaconda.kickstart import, and init logging before doing anything else.
  (clumens)
- Do not assume /dev/loop0 and /dev/loop1 are available. (clumens)
- tearDown -> tearDownModules. (clumens)
- Fix test suite Makefile.am files. (clumens)
- Check before running post scripts on kickstart rescue (#605754, atodorov).
  (clumens)
- Make sure lvm ignores unknown devicemapper devices (hdegoede)
- Put [] around ipv6 addr on the dracut cmdline (#605300) (hdegoede)
- Revert "Select default and mandatory packages when enabling repos."
  (#605289). (clumens)
- Fix the build. (clumens)
- Set repo.proxy only after fully assembled (#602712) (bcl)
- Change proxy regex in loader to match python proxy regex (#602712) (bcl)
- Add test cases for proxy regex (#602712) (bcl)
- Replace POSIX regex classes with character ranges (#602712) (bcl)
- Set wireless devices to NM_CONTROLLED by default (#594881) (rvykydal)
- Add iSCSI radio button to button group (#603726) (dcantrell)
- Fall back on regular device name (#604776) (dcantrell)
- Honor --timeout=NUM from kickstart files on s390 (#603032) (dcantrell)
- Use Decimal instead of float for label calculations (#604639) (bcl)
- Check for proper Proxy URL in loader (#604126) (bcl)
- fix: syntax error in network.py (akozumpl)
- fix: zfcp.startup() survives without an interface (#604542). (akozumpl)
- Fix a typo (#604628) (rvykydal)
- Revert "Retain user's UTC checkbox setting (#591125)" (bcl)
- Use method from isys for wireless devs checking (#473803) (rvykydal)
- Do not ask for interface twice in stage 1 (#594802) (rvykydal)
- Fix parsing of ifcfg OPTIONS parameter (#597205) (rvykydal)
- Don't overwrite 70-persistent-net.rules (#597625) (rvykydal)
- Wait only for activation of devices controlled by NM (#598432) (rvykydal)
- Show zFCP errors in dialog boxes rather than tracebacks (#598087) (maier)
- Show by-path names for DASD and zFCP, WWID for mpath (#580507) (maier)
- Remember autopart UI choice when going back (#596146) (dcantrell)
- Make parent directories for ks scriptlet log files (#597279) (dcantrell)
- Adjust the paths used for updates (bcl)
- Raise an error when an md dev is not in the tree after scanning all slaves
  (hdegoede)
- Raise an exception when an md dev is in the tree under the wrong name
  (hdegoede)

* Fri Jun 11 2010 Chris Lumens <clumens@redhat.com> - 14.8-1
- Rebind hybrid lcs/ctc network devices to correct driver if necessary
  (#596826) (maier)
- Get netdev name without CONFIG_SYSFS_DEPRECATED_V2 in linuxrc.s390 (#596826)
  (maier)
- Replace rd_CCW with final dracut option rd_ZNET for network-rootfs on s390
  (maier)
- Do parse DOMAIN for DNS search suffixes in loader (#595388) (maier)
- Allow loader to parse DNS and write DNS1, DNS2, ... itself (again). (#595388)
  (maier)
- GATEWAY in linuxrc.s390's ifcfg is really IPv4 only (#595388) (maier)
- Handle OPTIONS in ifcfg files transparently in loader (#595388) (maier)
- If only (clumens)
- Catch and display KickstartErrors coming from execute() cleanly (#603059).
  (clumens)
- Forcibly remove packages from deselected groups (#495621). (clumens)
- Default to aes-xts-plain64 for new luks devices. (#600295) (dlehman)
- Put another '/' in the rhinstall-install.img path (#601838). (clumens)
- Fix driver disc repo baseurl (#602343) (msivak)
- or -> and (clumens)
- fix: do not check root devices from hasWindows (#592860). (akozumpl)
- fix: kickstart sshpw command dysfunctional (#602308). (akozumpl)
- Include /sbin/blkid in the initrd.img (dcantrell)
- Correct initrd.img load address on s390 (dcantrell)
- Remove duplicate md handling code from 70-anaconda.rules (#599197)
  (dcantrell)
- Add md arrays to the devicetree with a md# name rather then md/# (hdegoede)
- "Finding" -> "Examining" storage devices (#594804). (clumens)
- In the filter UI, also ignore devices that do not report a size (#594803).
  (clumens)
- translations: scdate can translate timezones better then us. (akozumpl)
- fix: the po path has to be bound for gtk.glade too. (akozumpl)
- translations: don't say context=yes if you don't mean it. (akozumpl)
- translations: loader header files strings missing in anaconda.pot. (akozumpl)
- fix error saving screenshots during package install (#594826). (akozumpl)
- Re-get partedPartition after re-adding failed-to-remove partition. (dlehman)
- Select default and mandatory packages when enabling repos. (dlehman)
- do not import block from isys. not needed. (#601291). (akozumpl)
- removal: gui.InstallKeyWindow. (akozumpl)
- Make minimum shrink size 1 not 0 (#602442) (bcl)
- Initialize Decimal for partition slices (#602376) (bcl)
- Make sure lvm2 gets installed when we are using lvm (#601644) (hdegoede)
- Handle FCoE over vlan properly (#486244) (hdegoede)
- Tell user when nothing can be upgraded (#592605) (bcl)
- netork -> network (clumens)
- Redownload and extract updates.img during anaconda restart. (akozumpl)
- Restarting anaconda. (akozumpl)
- New version. (clumens)

* Fri Jun 04 2010 Chris Lumens <clumens@redhat.com> - 14.7-1
- Assign the trimmed identifier so it gets used in the UI. (clumens)
- Remember disk selections when going back to the text partition UI (#596113).
  (clumens)
- Fix typo in libblkid requires (#599821). (clumens)
- Fix green strips showing up (#582744) (bcl)
- Remember when IPv4 IPADDR has been read from ifcfg file in loader (#595388)
  (maier)
- Don't let loader write HWADDR to ifcfg file on s390. (#595388) (maier)
- Tell which stacks to configure in /etc/sysconfig/network on s390 (#595388)
  (maier)
- Really ignore deprecated parm/conf file options in linuxrc.s390 (#595388)
  (maier)
- Correctly pass netdev name from linuxrc.s390 to loader (#595382) (maier)
- Re-enable usable pdb with vnc on s390x (maier)
- Fix most of what is necessary for install over IPv6 on s390 (#594090)
  (dcantrell)
- Remove long deprecated writing of alias for network in linuxrc.s390 (maier)
- Fix backtrace when a vg starts with freespace (#597925) (hdegoede)
- Only kill init for reboot/halt and then exit linuxrc.s390 (maier)
- Fix a couple small errors found by checkbot. (clumens)
- Retain user's UTC checkbox setting (#591125) (bcl)
- Fix up pylint to work with the new source layout. (clumens)
- Replace the Serial Number column with an Identifier column (#560666).
  (clumens)
- Adjust mdraid size estimates (#587442) (bcl)
- Extra debugging output (#587442) (bcl)
- Set NM_CONTROLLED=no iscsi for storage devices only on system (#598070)
  (rvykydal)
- Improve handling of auto and unknown types in fstab. (#577260) (dlehman)
- Give blkid the final word on device format detection. (#593637) (dlehman)
- Allow ignoredisk to be interactive without the rest of the UI (#596804)
  (pjones)
- memory: check for URL install in loader too (#596993). (akozumpl)
- spec: python-pyblock has to be in BuildRequires too. (akozumpl)
- Ignore errors upon restoring /lib and /usr after unmounting filesystems
  (hdegoede)
- Make sure we still have an elf interpreter after unmounting fs (#598222)
  (hdegoede)
- booty: remove hack city hack (hdegoede)
- Remove booty/checkbootloader hacky raid set handling (hdegoede)
- booty: make getDiskPart deal with devices instead of names (hdegoede)
- booty: move grub specific mangling of partition number to the grub code
  (hdegoede)
- booty make getDiskPart use the devicetree (hdegoede)
- booty: make grubbyPartitionName and grubbydiskName take a device (hdegoede)
- booty: make matchingBootTargets and addMemberMbrs deal with devices instead
  of names (hdegoede)
- booty: make getPhysicalDevices take and return Devices rather then device
  names (hdegoede)
- booty: Make getPhysicalDevices only return physical devices (#593718)
  (hdegoede)
- booty: Don't create device.map entries for devices backing / (hdegoede)
- Add simple firewall unit test (msivak)
- Improve module cleanup in our TestCase class and fix issues in FS mock class.
  (msivak)
- Find tests using python-nose and create make unittest target (msivak)
- Update .gitignore file to account for new directory structure. (dcantrell)
- Update po/Rules-* files to account for new directory structure. (dcantrell)
- Structure the repo layout so it matches final structure better and make isys
  a real Python package. (msivak)
- Add more sanity checks to the mountpoint (#592185) (bcl)
- Make sure the product.img directory is mounted before copying (#587696).
  (clumens)
- Put a missing close brace back into isys.c. (clumens)
- refactoring: put totalMemory() into isys. (akozumpl)

* Wed May 26 2010 Chris Lumens <clumens@redhat.com> - 14.6-1
- Set repository in kickstart harddrive command (#592239) (rvykydal)
- nm-c-e integration: fix some leftovers from patch porting. (rvykydal)
- Add missing logging import to installinterfacebase (hdegoede)
- Give pre-existing mdraid arrays the proper name in the UI (#596227)
  (hdegoede)
- Add nm-c-e translations to stage 2 (#594982) (rvykydal)
- set the resolution with resolution= from the cmdline (#594918). (akozumpl)
- cleanup: gui.py never uses runres for anything, off it goes. (akozumpl)
- Skip the bootloader placement window if we're on UEFI (#582143) (pjones)
- Add some more stuff to .bash_history (pjones)
- Support cio_ignore functionality for zFCP devices (#533492) (dcantrell)
- Add missing newline for 'nfs' line in ks file (#591479) (dcantrell)
- Correct problem with initrd.addrsize generation (#546422) (dcantrell)
- Fix rescue mode startup with kickstart file and without (#515896) (msivak)
- More checkbot fixes. (clumens)
- fix: traceback in check_memory() (#595284). (akozumpl)
- Drop init questions from cmdline.py (hdegoede)
- Move init questions to InstallInterfaceBase (hdegoede)
- Make re-init all inconsistent lvm mean re-init all instead of ignore all
  (hdegoede)
- Read cciss devices correctly from 'multipath -d' output (#559507) (dcantrell)
- On NFS installs, look for product.img and updates.img under images/
  (#594811). (clumens)
- Remove yum cache for anaconda's temporary repos (#593649). (clumens)
- Use correct NM dbus interfaces (#594716) (rvykydal)
- Change the configuration of depmod and link modules to better place (#593941)
  (msivak)
- Make ssid and wepkey in boot params and stage 1 kickstart work (#473803)
  (rvykydal)
- logging: remove addLogger() (akozumpl)
- iutil: execWithCallback() and execWithPulseProgress() return an object.
  (akozumpl)
- logging: simplify stdout logging in execWithCallback(). (akozumpl)
- logging: use stderr parameter in execWithCallback(). (akozumpl)
- logging: remove addSysLogHandler() (akozumpl)
- analog: handle a config file we can't open. (akozumpl)
- clearer error messages for missing iscsi initiator name (hdegoede)
- fedora is part of iSCSI initiator name (#594659) (hdegoede)
- Add default iSCSI initiator name in rescue mode (#594434) (hdegoede)
- Do not allow editing of extended partitions (#593754) (hdegoede)
- Check for sane mountpoint in raid dialog (#592185) (bcl)
- Check for sane mountpoint in lvm dialog (#592185) (bcl)
- Check for sane mountpoint in partition dialog (#592185) (bcl)
- Cleaned up sanityCheckMountPoint (bcl)
- Don't autostep past the end of the install screens (#593556) (bcl)
- Add missing rpm macros file to get rid of the rpm warnings (msivak)
- Add the rpmrc file to the initrd.img (#508242) (mgracik)
- fix: syntax error in gui.py from 9e69c5f36f79410d9df1502fe69f02f4d06173ab.
  (akozumpl)
- Keep track of pvcount for non existing vgs (#593871) (hdegoede)
- Improve module cleanup in our TestCase class and fix issues in FS mock class.
  (msivak)
- Don't drop encryption when re-editing new encrypted partitions. (#582888)
  (dlehman)
- Return disk to prior state following failed partition removal. (#580088)
  (dlehman)
- Display unpartitioned disks in main partitioning gui. (#588637) (dlehman)
- Pick up mountpoint for existing formats on encrypted LVs. (#587002) (dlehman)
- Automatic partitioning should yield no more than one PReP partition.
  (dlehman)
- Pass short type names for PartSpec ctor. (dlehman)
- Setting up lvs should never fail (hdegoede)
- We no longer need to handle lvs which are part of an incomplete vg (hdegoede)
- Don't clear immutable devices (#593642) (hdegoede)
- Store immutable info into the device for easier access (hdegoede)
- Reset vg blacklist when initializing storage (hdegoede)
- Handle vgs with duplicate names (#591469) (hdegoede)
- Delay setting up lvs until other devices are scanned (hdegoede)
- anaconda udev rules should not get lvm info based in volgroup name (hdegoede)
- Move creation of lv devices into its own function (hdegoede)
- livecd: window icon (#583333). (akozumpl)
- FcoeDiskDevice.dracutSetupString(): use the right dracut syntax (#486244)
  (hdegoede)
- improve the memory checking so it reflects better the hungry architectures.
  (akozumpl)
- logging: fix SIGSEGV when trying to log after closeLog() is called.
  (akozumpl)
- Updates to scripts/makebumpver. (dcantrell)
- Suppress failures to tear down /dev/loop devices (#591829) (bcl)
- Fix the order of arguments in archive read callback and archive closing.
  (msivak)
- Use "kernel-modules = version" style for locating rpms providing driver
  updates (msivak)
- Move depmod configuration into new directory structure to get rid of depmod
  warning (#508242) (msivak)
- Fix descriptor leak and iteration progress in driverdisc code (#592225)
  (msivak)
- Add lsof command to initrd.img (mgracik)
- Add hmac file for sshd (#592186) (mgracik)
- Enable fips mode after fips mode installation (#592188) (mgracik)
- Add nslookup to the install.img (#591064) (mgracik)
- Add the chk files for libraries to the install.img (#590701) (mgracik)
- Add the eject command to the install.img (#591070) (mgracik)
- Add hmac file for libgcrypt to install.img (#590701) (mgracik)
- Don't remove *.hmac files when creating install images (mgracik)
- Added clear command to the install.img (#586499) (mgracik)
- Added chvt to the install.img (#575844) (mgracik)
- Only install non-branded anaconda icon on liveinst arches (dcantrell)
- Fix of typo. (rvykydal)
- Fix two minor errors found by checkbot. (clumens)
- Fix bad patches reordering (#473803) (rvykydal)
- scripts/analog: normalize paths before generating the config. (akozumpl)
- gui: "_use anyway" mnemonic. (akozumpl)
- logging: give loglevels for the shortened names. (akozumpl)
- logging: remove references to the 'bootloaderadvanced' step. (akozumpl)
- logging: remove references to some more steps. (akozumpl)
- Move importing of tested modules into setUp methods (msivak)
- Add Mock classes (msivak)
- gui, autopart: don't let a too verbose translation ruin all teh fun
  (#591955). (akozumpl)
- Update po/POTFILES.in for nm-connection-editor integration. (dcantrell)
- Fix typo in loader/nfsinstall.c (dcantrell)
- Add the best package for this arch to the optional package selector
  (#591653). (clumens)
- Swap server and opts on the split() call (#591479) (dcantrell)
- Handle devices that don't have a /dev/disk/by-path/ symlink (#563242)
  (pjones)
- Make sure we write out multipath.conf before discovery (#563242) (pjones)
- Handle >2 way /sbin/multipath output better (#563242) (pjones)
- Look for updates.img and product.img on NFS installs. (clumens)
- And add a menu to the right hand side so you can see the new column.
  (clumens)
- Don't ask if we have ESSID specified by kickstart or stage 1 (#473803)
  (rvykydal)
- Make ks option network --wepkey work in stage 2 (#473803) (rvykydal)
- Add support for wireless configuration using nm-c-e in stage 2 (#473803)
  (rvykydal)
- Write out ifcfg files only when necessary (#520146) (rvykydal)
- Use separate method for copying network configuration to system (#520146).
  (rvykydal)
- Network: remove functions that are not used anymore (#520146) (rvykydal)
- Wait for specific activated network devices (#520146). (rvykydal)
- Set network devices configured in ks to be nm-controlled (#520146).
  (rvykydal)
- Remove no longer needed devices argument from Network.write() (#520146)
  (rvykydal)
- Actually generate contents of 70-persistent-net.rules (#520146) (rvykydal)
- Disable [Configure Network] button if there are no net devs (#520146)
  (rvykydal)
- Add net device description into selection dialog (#520146) (rvykydal)
- Check preselected install network device as nm-controlled (#520146)
  (rvykydal)
- Don't ask when configuring net if we have only one network device (#520146)
  (rvykydal)
- Do not mess value change with line formatting (#520146) (rvykydal)
- Log change of ifcfg files by nm-c-e (#520146) (rvykydal)
- Enable networking in stage 2 using nm-c-e (#520146) (rvykydal)
- Write ifcfg files via NetworkDevice in Network.write() method (#520146)
  (rvykydal)
- Use ifcfg files via NetworkDevice in Network class (#520146) (rvykydal)
- Use proper attribute instead of NetworkDevice 'DESC' hack (#520146)
  (rvykydal)
- Quote values when writing out to ifcfg files (#520146) (rvykydal)
- Network.__str__() little cleanup (#520146) (rvykydal)
- Use IfcfgFile class to back NetworkDevice objects (#520146) (rvykydal)
- Move some consts to module globals for use in other places (#520146)
  (rvykydal)
- Add class for handling ifcfg files (#520146) (rvykydal)
- logging: the ibft message once again. (akozumpl)
- logging: no iBFT is not an error, fix spelling. (akozumpl)
- logging: log loader messages with LOG_LOCAL1 syslog facility. (akozumpl)
- logging: strip the extra newline in FCoE EDD log (akozumpl)
- logging: remove references to "confirminstall" and "confirmupgrade" steps.
  (akozumpl)
- logging: remove all references to the "installtype" step. (akozumpl)
- Determine if an mdmember is biosraid earlier (#586298) (hdegoede)
- Set runlevel 5 based on the presence of both a display manager and X server.
  (#588483) (notting)
- Add "Serial Number" column to the right side of the cleardisks UI. (clumens)
- Set permissions on initrd.addrsize to 0644 (#591455) (dcantrell)
- fix compile error after 7aace0bf0e0557cd914aa93e80a709a9f21f07f8 (akozumpl)
- autoconf: icons/ is missing makefiles (akozumpl)
- new version of report wont start without /etc/report.conf (akozumpl)
- Don't allow creating a new bootloader config in text mode (#580378).
  (clumens)
- Fix verification of DDs, we were looking for wrong path (#508242) (msivak)
- Remove raid clone option and code (#587036) (hdegoede)
- cleanup booty x86 flag.serial handling (#589773) (hdegoede)
- isys/auditd was missing from .gitingore. (akozumpl)
- bootloader timeout default should be None not 0 (jkeating)
- Use iBFT if present and user didn't asked for anything else. (#590719)
  (msivak)
- storage: LUKSDevice takes req_grow after its slave (#589450). (akozumpl)
- Correctly parse system-release (#590407) (lkundrak)
- Offer to ignore unformatted DASDs rather than forcing exit (#580456)
  (dcantrell)
- Make Format and Resize checkboxes mutually exclusive (#589977) (dcantrell)
- Fix usage of deviceNameToDiskByPath in devicetree.py (#589967) (dcantrell)
- Advance line pointer & don't strdup(val) on error in readNetInfo (dcantrell)
- Add non-branded default liveinst icons for anaconda (#588737) (dcantrell)
- Add expanded=False to the base class's detailedMessageWindow as well.
  (clumens)
- Add all possible install class locations to the search path (#587696).
  (clumens)
- Use module reloading in driver disc operations (#590015) (msivak)
- Use gtk consts instead of magic ints. (rvykydal)
- Only initialize logging via a method, not with every import (#584054).
  (akozumpl)
- Remove the check for partitions (#508242) (msivak)
- Close the dir descriptor after usage. (#589580) (msivak)
- Remove partitions after unpartitioned non-partition devices. (#588597)
  (dlehman)
- Work around device node creation issues when creating EFI images. (#589680)
  (pjones)
- Clean up tabs in dispatch.py (bcl)
- Just use /dev/dasdX if we can't get a by-path link (dcantrell)
- Do not prepend /dev/disk/by-path in format DASD window (dcantrell)
- Use udev_device_get_by_path() to get /dev/disk/by-path link (dcantrell)
- Add udev_device_get_by_path() to return /dev/disk/by-path link (dcantrell)
- Expand the details pane when showing unformatted DASDs (#580463) (dcantrell)
- Log problem line if unquoting failed in readNetInfo() (dcantrell)
- Update generic.ins for s390x (#546422) (dcantrell)
- Rename geninitrdsz.c to addrsize.c (#546422) (dcantrell)
- Generate initrd.addrsize file correctly for LPAR booting (#546422)
  (dcantrell)
- Only allow upgrading from one minor release of RHEL to another (#589052).
  (clumens)
- fcoe: use fipvlan instead of fcoemon to bring up fcoe (#486244) (hdegoede)
- memory: increase the RAM limits, check for URL installs (#549653). (akozumpl)
- memory: build auditd as a standalone binary and run it so (#549653).
  (akozumpl)
- gui: don't let metacity display the title right-click menu (#588642).
  (akozumpl)

* Wed May 05 2010 Chris Lumens <clumens@redhat.com> - 14.5-1
- Link /sbin/reboot and /sbin/halt to /sbin/init on s390x (#571370) (dcantrell)
- Don't clear bootloader radio selection on double click (#588771). (clumens)
- Add support to livecd for arbitrarily complex dir structures. (#504986)
  (dlehman)
- Grab everything in $LIBDIR/rsyslog/ (pjones)
- Do not automatically backtrace when telnetd quits (#588964). (clumens)
- Share terminology between the cleardisks text and panel headers (#587879).
  (clumens)
- Allow displaying groups that only contain conditional packages (#475239).
  (clumens)
- Fix hasWindows() to actually work as advertised (hdegoede)
- Revert commit 27a4c7df871744454d1ca8979a576f9f45c67189 (hdegoede)
- Make deviceNameToDiskByPath check udev info instead of sysfs (dcantrell)
- Fix some minor problems in storage/dasd.py (#560702) (dcantrell)
- Read in network settings correctly, as configured by linuxrc.s390 (dcantrell)
- Clean up wording for oversized LVs (#587459) (dcantrell)
- Teach upd-instroot about i686 (jkeating)
- Make the rule for 70-anaconda.rules in updates.img be generic. (pjones)
- Do not use --quiet and --nostart when doing selinux configuration (#568528)
  (msivak)
- Tell dracut it should activate the first swap device (#572771) (hdegoede)
- Remove broken hasWindows function from bootloader.py and its callers
  (hdegoede)
- booty: remove dead code chunk (hdegoede)
- Don't add recovery partitions to the grub boot menu (#534066) (hdegoede)
- Use g_str_has_suffix() to check end of string (dcantrell)
- Find stage2 install.img on local hd installs (dcantrell)
- gui: gray out OK button while adding raid set (#587161). (akozumpl)
- Strip quoting from OPTIONS when composing rd_CCW line (#577193). (dcantrell)
- Default the global grub timeout to 5 for serial (jkeating)
- Print out device sizes in list-harddrives-stub as well (#587395). (clumens)
- Make sure a given path exists before calling os.statvfs on it (#587662).
  (clumens)
- Wait for scsi adapters to be done with scanning their busses (#583143)
  (hdegoede)
- Set CURL_FAILONERROR to catch url download errors (#586925) (dcantrell)
- Bring up network for local hd vnc kickstart installs (#522064) (dcantrell)
- gui: no close buttons etc. in window decoration (#582645) (akozumpl)
- Don't clear BIOS RAID member disks (#587066) (hdegoede)
- Remove devices from libparted's cache when destroying them (#586622)
  (hdegoede)
- Offer to format unformatted DASD devices (#560702) (dcantrell)
- X input configuration has moved to /usr/share (#585621). (clumens)
- Disable button icons on stock GTK buttons (#579701). (akozumpl)
- Remove button icons from the glade files (#579701). (akozumpl)
- Don't traceback on CD-ROM driver in list-harddrives-stub (#586410). (clumens)
- Fetch ks files over NFS when ksdevice is not given (#541873) (dcantrell)
- put liveinst/console.apps/liveinst.h in .gitignore (akozumpl)
- Remove the README files (#583408). (clumens)
- Make it more clear what the purpose of the "Boot" column is (#584811).
  (clumens)
- nfs: off by one error leaves extra slash in a path. (akozumpl)
- removal: umountStage2(). (akozumpl)
- nfs: direct mounting of stage2. (akozumpl)
- loader: strip trailing slash character from stage2= URL. (akozumpl)
- imount: allow bind mounts. (akozumpl)
- Make sure we use 1.0 mdraid metadata when the set is used for boot (#584596)
  (hdegoede)
- Add a preCommitFixup hook to StorageDevice classes (hdegoede)
- Check for not having found any disks after populating the tree (#583906)
  (hdegoede)
- Prune resize and format create/migrate actions if destroying a device.
  (dlehman)
- Schedule actions when removing existing extended partitions. (#568219)
  (dlehman)
- Don't try to zero out extended partitions. (dlehman)
- lvm: check resizing against format's targetSize (#580171). (akozumpl)
- Restore storage.clearPartType after reset when backing out of GUI. (#559233)
  (dlehman)
- Make Cancel button the default for 'Weak Password' dialog (#582660) (bcl)
- Set Create Storage focus to first active radio button (#582676) (bcl)
- BaseInstallClass no longer has a setInstallData method. (clumens)
- livecd.py: set the selected keyboard (#583289). (akozumpl)
- Make rhel.py an installclass that we can inherit from for variants. (notting)
- Don't make all devices on the boot device selector immutable (#583028).
  (clumens)
- Don't allow running as non-root (#583213). (clumens)
- Careful with that WINDOW_TYPE_HINT_DESKTOP, Eugene. (#582998) (akozumpl)
- Introduce flags.preexisting_x11. (akozumpl)
- Fix some HIG problems with the "Write Changes" dialog (#583405). (clumens)
- Fix up some HIG problems with the betanag dialog (#583404). (clumens)
- Fixup P_ usage in questionInitializeDASD (hdegoede)
- Prevent low-level formatting of DASDs in rescue mode (#582638) (hdegoede)
- Move the question about formatting DASD's to the interface class (hdegoede)
- Let the user know if adding a zfcp drive fails (#582632) (hdegoede)
- Fixup P_ usage in installinterfacebase (hdegoede)
- Check for presence of filesystem module in FS.mountable (#580520) (dcantrell)
- Check for fs utils when determining if an fs can be resized (#572431)
  (dcantrell)
- Select "Advanced Storage Devices" by default on s390 (#580433). (clumens)
- Don't sigsegv on stage2= derived from invalid repo= parameter (#574746).
  (rvykydal)
- Removed the tooltips showing glade.gnome.org link (#566773) (mgracik)
- Better filter for commits to ignore for the RPM changelog. (dcantrell)
- In groupListExists, log what groups don't exist. (notting)
- Do not append "rhgb quiet" to s390 boot loader config (#570743) (dcantrell)
- No instdata on master anymore. (anaconda.id -> anaconda) (dlehman)
- Try to get boot reqs onto the selected boot device. (#560387) (dlehman)
- Ensure proper disklabel type on boot disk if CLEARPART_TYPE_ALL. (#570483,
  #530225) (dlehman)
- Add proper support for destruction of disklabels. (dlehman)
- Three small fixes to action sorting. (dlehman)

* Thu Apr 15 2010 Chris Lumens <clumens@redhat.com> - 14.4-1
- There is no rhbz list for non rhel branch builds. (dcantrell)
- pylint up, pychecker down. (clumens)
- Add a script for running pylint on anaconda (hdegoede)
- add_drive_text: Pass interface to iscsi.addTarget (hdegoede)
- Add a questionInitializeDisk method to the rescue interface (#582304)
  (hdegoede)
- Add advanced storage support to rescue mode (#571808) (hdegoede)
- rescue.py: Put our mount / rw, ro, skip question in a loop (hdegoede)
- Move addDriveDialog() and friends to their own class (hdegoede)
- partition_text: Make addDriveDialog() not depend on anaconda.storage
  (hdegoede)
- Fix syntax error in kickstart.py (hdegoede)
- Fix various syntax errors (hdegoede)
- Read ~/.rhbzauth in scripts/makebumpver (dcantrell)
- Simplify HWADDR removal check on s390x (#546005) (dcantrell)
- Set minswap suggestion on s390x to 1 (#466289). (dcantrell)
- Check for and offer to format unformatted DASD devices (#560702). (dcantrell)
- Add /sbin/reboot and /sbin/halt to s390 initrd.img (#571370) (dcantrell)
- Do not append "rhgb quiet" to s390 boot loader config (#570743) (dcantrell)
- Increase ping timeout for gateway/dns server reachability check (#536815)
  (dcantrell)
- Wait on all pids, not just udevd's. (#540923) (pjones)
- Use the new modularized anaconda path in run_test.py. (clumens)
- Fix a mismatched kickstart command as caught by the new test case. (clumens)
- Fix a typo. (clumens)
- Fix "make check" to run the tests against your git checkout of anaconda.
  (clumens)
- Add a test case to verify that kickstart commands use the right handler.
  (clumens)
- filter_gui.py: fixup isProtected changes for biosraid and mpath (hdegoede)
- Write an AUTO ... line to mdadm.conf (#537329) (hdegoede)
- Inherit the ZFCP command from the correct pykickstart class (#581829).
  (clumens)
- Apply yet another translation patch (#573870). (clumens)
- Add bug mapping support to scripts/makebumpver. (dcantrell)
- Makefile.am syntax fixes for the 'bumpver' target. (dcantrell)
- Fix traceback in booty when ppc /boot lives on mdraid (#555272) (hdegoede)
- Call scripts/makebumpver from 'make bumpver' target. (dcantrell)
- Add docs/commit-log.txt explaining git commit log policies. (dcantrell)
- Move 'make bumpver' functionality to scripts/makebumpver (dcantrell)
- Fix some previously difficult-to-translate strings (#573870). (clumens)
- Default to /images/install.img if no dir is given in stage2=hd: (#528809)
  (rvykydal)
- Startup notification in live installer (#530908). (akozumpl)
- init: switch back to tty1 after the installer finishes. (#577380) (akozumpl)
- Don't segfault if proxyUser or proxyPassword are empty (#580226). (clumens)
- yum requires the proxy settings to include a protocol (#576691). (clumens)
- Allow using pre-existing gpt labels for /boot on non EFI x86 (#572488)
  (hdegoede)
- Log successful login to iscsi targets (hdegoede)
- storage/udev.py handle iscsi ID_PATH IPV6 address containing : (#579761)
  (hdegoede)
- Catch errors when downloading the escrow cert (#579992). (clumens)
- fix: mnemonics don't work in the welcome screen until user clicks. (akozumpl)
- refactoring gui.py: setup_window() and setLanguage() are way too similar.
  (akozumpl)
- gui.py: removed unused parameter in setup_window() (akozumpl)

* Tue Apr 06 2010 Chris Lumens <clumens@redhat.com> - 14.3-1
- Sort partition create actions before other unpartitioned devices.
  (#574379) (dlehman)
- Update the partition scheme icons to better looking ones (#579697).
  (clumens)
- Move some kickstart-specific storage init into storageInitialization.
  (clumens)
- Call the right superclass's __init__ method. (clumens)
- Adjust paths that reference things that have moved. (clumens)
- Move compiled things out of /usr/lib/anaconda-runtime. (clumens)
- Move boot files, language data, keymaps, etc. to /usr/share/anaconda/.
  (clumens)
- Move class Anaconda to __init__.py. (clumens)
- Install classes are now under the anaconda module directory. (clumens)
- lang-table and lang-names have moved to /usr/share/anaconda. (clumens)
- upd-instroot no longer needs to explicitly pull in the python parts.
  (clumens)
- Adjust command stubs to use new anaconda module location. (clumens)
- Put /usr/lib*/python?.?/site-packages/pyanaconda at the front of
  PYTHONPATH. (clumens)
- Adjust the Makefiles to install anaconda to /usr/lib{,64}/python?.?.
  (clumens)
- ui: keep the bootloader device dialog always centered (#463489). (akozumpl)
- Reword the filter UI tooltip to be a little more clear (#576144). (clumens)
- Automatically select devices added via the "Add Advanced" button
  (#579051). (clumens)
- Re-Check minimum size of partition after running fsck on it (#578955) (bcl)
- Take the request's format into account when deciding to resize (#578471).
  (clumens)
- Schedule removal actions for any format on a --onpart= device (#576976).
  (clumens)
- Fix early networking log message to correctly assign blame. (pjones)
- Restore xdriver=<driver> functionality (#577312) (msivak)
- loader: con Newt into thinking LANG is always en_US.UTF-8 (#576541).
  (akozumpl)
- network.dracutSetupString(): handle hosts outside the subnet (#577193)
  (hdegoede)
- Copy install.img to install target on http installs. (pjones)
- Make sure the install.img exists before attempting to copy (#578391).
  (clumens)
- Write rd_CCW when root fs is on a network device on s390x (#577193)
  (dcantrell)
- Keep /usr/bin/seq for the initrd.img (#558881). (dcantrell)
- fix: Tackle race condition issues during X startup. (akozumpl)
- Make checksum error message user-friendlier (#578151) (rvykydal)
- Enable network if it is needed when repo is added in UI (#577803).
  (rvykydal)
- Do not try to commit diskLabels on non partitionable devices (#576145)
  (hdegoede)
- Copy install.img and remount no matter how many discs (#577196) (pjones)
- Fix typo in linuxrc.s390. ctm should be ctcm. (dcantrell)
- Remove dasdSetup() from loader. (dcantrell)
- Add new return code check for isomd5sum's mediaCheckFile (#578160).
  (rvykydal)
- Use symbolic constants of libcheckisomd5 (#555107) (rvykydal)
- Adapt for libcheckisomd5 callback abi change (#555107) (rvykydal)
- Include /sbin/*_cio_free commands in s390x initrd.img (#558881).
  (dcantrell)
- Use /sbin/dasd_cio_free to free blacklisted DASDs (#558881) (dcantrell)
- Don't add duplicates to the transaction set (#575878, jantill). (clumens)
- fcoe: sysfs_edd.sh has been renamed to fcoe_edd.sh (hdegoede)
- Fix off-by-one error in string initialization (#577413) (msivak)
- Fix uninitialized variable compile error (#577501) (msivak)
- Do not write OPTIONS=layer2=1 on all architectures (#577005). (dcantrell)
- Show protected devices in the filter UI, but make them immutable
  (#568343). (clumens)
- Turn protected devices into a property on the Anaconda object. (clumens)

* Thu Mar 25 2010 David Lehman <dlehman@redhat.com> - 14.2-1
- Unlock the CD tray door in isys.ejectcdrom() (#569377) (pjones)
- Try to pull in generic libraries as well as optimized ones (#572178)
  (pjones)
- Translate the Back button in glade (#576082) (akozumpl)
- Make the kernel 'sshd' parameter work as expected (#572493) (akozumpl)
- Add originalFormat handling to editLVMLogicalVolume. (#576529) (dlehman)
- Fix a cut&paste error that caused a traceback (#574743) (dlehman)
- Remove isys/str.c, replace calls with glib.h or string.h calls. (dcantrell)
- Only look for extended partitions on partitioned devices (#576628)
  (hdegoede)
- Fix referring to disks by-label, by-uuid, etc (#575855). (clumens)
- fcoe startEDD() add missing return statement (hdegoede)
- Add support for recognizing BIOS EDD configured FCoE drives (#513018)
  (hdegoede)
- Update format of cdrom devices when looking for repos on media (#566269)
  (rvykydal)
- Fix syntax for passing a mapping to a translatable string (#576085).
  (clumens)
- Update filter for translation log entries. (dlehman)

* Mon Mar 22 2010 David Lehman <dlehman@redhat.com> - 14.1-1
- Don't pass size=1 for autopart PVs. Use PartitionDevice's default size.
  (dlehman)
- Update po/POTFILES.in to list all files with strings. (dcantrell)
- platform.py: _diskLabelType is a string itself (hdegoede)
- Make python start with correct default unicode encoding (#539904).
  (akozumpl)
- Add boot= argument to kernel cmdline when in fips mode (#573178) (hdegoede)
- Catch NotImplementedError when scanning for disklabels (#566722) (hdegoede)
- BIOS RAID sets get shown double when adding advanced storage (#574714)
  (hdegoede)
- Filter UI do not start / stop BIOS RAID sets to get there size (#574587)
  (hdegoede)
- Make filter UI honor nodmraid cmdline option (#574684) (hdegoede)
- Properly align the first partition we create (#574220) (hdegoede)
- Move disabling of cylinder alignment to disklabel format (hdegoede)
- put the analog script into the RPM (akozumpl)
- Fix focus, repaint, and stack issues for nm-c-e (#520146) (rvykydal)
- Connect nm-connection-editor to network config button (#520146). (rvykydal)
- Add "Configure Network" button to network UI screen (#520146). (rvykydal)
- Add nm-connection-editor to stage2 (#520146). (rvykydal)
- l10n: Updates to Spanish (Castilian) (es) translation (gguerrer)
- Don't try to set selinux context for read-only mountpoints. (dlehman)
- Derive stage2= from repo=nfsiso: correctly (#565885) (rvykydal)
- Include USB ATA bridge modules in initrd (#531532) (rvykydal)
- Remove hacks that don't apply in present repo setup flow. (rvykydal)
- Reset comps/groups info after editing repo in UI (#555585) (rvykydal)
- Set cache base directory for repos added/edited in UI. (rvykydal)
- Use None, not '', for empty repo proxy attributes (#572460) (rvykydal)
- livecd: show graphical error dialog when memory check fails (#572263)
  (akozumpl)
- l10n: Updates to Sinhala (si) translation (snavin)
- use isSparc not isSPARC (dennis)
- set the bootloader to silo for sparc installs (dennis)
- sparc64 is a lib64 arch (dennis)
- Make sure that SPARC bootdisk Makefile is made (dennis)
- make sure we include sparc boot configs (dennis)
- add function to get the sparc system type (dennis)
- Sparc bootloader config not written to /etc (dennis)
- Fix generation of boot.iso on SPARC (dennis)
- l10n: Updates to Polish (pl) translation (raven)
- Keep the selected device count right when going back to filtering
  (#572882). (clumens)
- Fully qualify _ped.IOException. (dlehman)

* Mon Mar 15 2010 David Lehman <dlehman@redhat.com> - 14.0-1
- Do not crash on .autorelabel when using read only rescue mount (#568367)
  (msivak)
- parted.PartedDisk can throw IOExceptions too (#573539) (hdegoede)
- l10n: fix/updates to hungarian translation (snicore)
- l10n: updated translations (snicore)
- Use the disk name from kickstart in the shouldClear error message.
  (clumens)
- Fix displaying error messages on cleanup/remove callback problems
  (#572893). (clumens)
- Before running shouldClear, make sure a real disk was specified (#572523).
  (clumens)
- Fix: execWithRedirect() unexpectedkeyword argument 'searchPath' (#572853)
  (hdegoede)
- Tell ld.so and friends not to use hardware optimized libs (#572178)
  (pjones)
- By default, libcurl does not appear to follow redirects (#572528).
  (clumens)
- FcoeDiskDevice.dracutSetupString: handle DCB on / off option (hdegoede)
- Redo the 'sshd' flag. (ajax)
- Catch "Exception" when window manager is starting. (akozumpl)
- Preserve encryption setting when re-editing new encrypted LVs. (#568547)
  (dlehman)
- Never pass "<Not applicable>" as mountpoint to format constructors.
  (dlehman)
- Fix up device dialogs' handling of preexisting formatting. (dlehman)
- Set up devices using their original formats for certain action types.
  (#565848) (dlehman)
- Keep a handle to devices' original format instance. (#565848) (dlehman)
- Pick up system's clock settings on upgrade. (#570299) (akozumpl)
- Do not crash when getDevices returns NULL (#567939) (msivak)
- Use new API in libblkid to look for driverdiscs on removable devices
  (#508242) (msivak)
- Use new package structure of firstaidkit (#510346) (msivak)
- Add "crashkernel=auto" to grub.conf for RHEL installs (#561729) (hdegoede)
- Drop iscsi initrd generation hack (hdegoede)
- Fix recognition of partitions on mdraid arrays (#569462) (hdegoede)
- dcbd is being replaced with lldpad (#563790) (hdegoede)
- Use the same cache directory as yum now uses (#568996). (clumens)
- exception.py: switch to tty1 before exit (#569071) (akozumpl)
- Reset conditionals of transaction info too. (#505189) (rvykydal)
- Use '--keyword=P_:1,2' for plural gettext string extraction (#567417).
  (dcantrell)
- make sure the new logging also works when isys is imported as a python
  module. (akozumpl)
- use the new logging approach in imount.c (akozumpl)
- allow logging into program.log and syslog through log.c (akozumpl)
- log.c: factor out common parts from logMessageV() (akozumpl)
- static variable rename in log.c (akozumpl)
- move log.c from loader into isys. (akozumpl)
- Analog, a generator of rsyslog config files to monitor remote installs.
  (akozumpl)
- Remove isys/minifind.c and isys/minifind.h (dcantrell)
- Keep default metacity schema generated for gconf. (#520146) (rvykydal)
- metacity, fix a displaying problem with WaitWindow and ProgressWindow
  (#520146) (akozumpl)
- Nuke addFrame()'s showtitle parameter (#520146). (akozumpl)
- Remove gui code we no longer need when mini-wm is gone (#520146) (akozumpl)
- Remove mini-wm.c. (#520146) (akozumpl)
- Introduces metacity window manager (#520146) (akozumpl)
- fix: do not initialize the install interface whenever is is accessed
  (#565872) (akozumpl)
- Select/Deselect All should only apply to the current tab (#516143,
  #568875). (clumens)
- Don't try to write firewall and auth information twice (#568528). (clumens)
- Fixes bug #569373 - Change udev_trigger block calls to use change action
  (bcl)
- Include the report module and related support files (#562656). (clumens)
- report handles exn saving now, and doesn't require a Filer (#562656).
  (clumens)
- Adapt to using report's UI API (#562656). (clumens)
- Do some editing of package and filter UI strings (#569039). (clumens)

* Thu Mar 04 2010 Chris Lumens <clumens@redhat.com> - 13.33-1
- On live installs, the syslog is /var/log/dmesg. (#568814). (clumens)
- Set up udev environment so anaconda's udev rules run in livecd. (#568460)
  (dlehman)
- Ignore probably-spurious disklabels on unpartitionable devices. (#567832)
  (dlehman)
- The justConfigFile parameter doesn't do anything on x86, either (#568567).
  (clumens)
- Add python-devel's gdbinit, which provides useful debugging macros.
  (pjones)
- Minor style fix (indent "cat" correctly") (pjones)
- doReIPL should return when going back through steps, too (#563862).
  (clumens)
- Skip the filter/cleardisk steps on upgrades, too (#568334). (clumens)

* Thu Feb 25 2010 David Lehman <dlehman@redhat.com> - 13.32-1
- Check for the real device-mapper nodes in /proc/swaps. (#567840) (dlehman)
- It's necessary to give each vfprintf invocation a fresh va_list (#568235)
  (akozumpl)
- Don't unconditionally unskip the partition step on failure (#567889).
  (clumens)
- rpm doesn't always give the callback a tuple (#567878). (clumens)

* Wed Feb 24 2010 David Cantrell <dcantrell@redhat.com> - 13.31-1
- Revert "There is no kernel-PAE package anymore, use kernel for xen
  (#559347)." (dcantrell)
- logging: make loader say 'loader' (#563009). (akozumpl)
- Make loader log into syslog (so remote logging works for it as well)
  (#524980) (akozumpl)

* Tue Feb 23 2010 Chris Lumens <clumens@redhat.com> - 13.30-1
- Revert "Add back hald for Xorg input device queries (#553780)" (clumens)
- No longer remove persistent udev rules files (#566948). (clumens)
- When BUILDARCH==ppc64, set BASEARCH to ppc (#524235). (dcantrell)
- There is no kernel-PAE package anymore, use kernel for xen (#559347).
  (dcantrell)
- Fix a typo, leaving one less string needing translation (#567427).
  (clumens)
- Don't show BIOS RAID and multipath members in the cleardisks UI (#567281).
  (clumens)

* Mon Feb 22 2010 David Cantrell <dcantrell@redhat.com> - 13.29-1
- DiskLabel.status can't be determined so return False. (#563526,#561074)
  (dlehman)
- Remove getDasdDevPort() and getDasdState() from isys.py. (dcantrell)
- Replace calls to isys.getDasdPorts() with calls to new getDasdPorts()
  (dcantrell)
- Add getDasdPorts() to storage/dasd.py. (dcantrell)
- Remove isys/dasd.c, functions no longer needed in isys. (dcantrell)
- Fix creation of encrypted md members and pvs in kickstart. (#567396)
  (dlehman)
- Don't align free space geometries in getFreeRegions. (#565692) (dlehman)
- Align extended partitions like we do other partitions. (dlehman)
- Don't allow the host's LD_LIBRARY_PATH affect get_dso_deps (#565887).
  (clumens)
- Remove a couple redundant network bring up calls. (clumens)
- Reset the resolver cache after bringing up the network (#562209). (clumens)
- Let's have /etc/xorg.conf.d in stage2 (#566396) (akozumpl)
- Add the filter UI screens to the list of translatable files (#567216).
  (clumens)
- Don't traceback when a user tries to put /boot on an LV (#566569)
  (hdegoede)
- RescueInterface should inherit from InstallInterfaceBase too (hdegoede)

* Fri Feb 19 2010 Chris Lumens <clumens@redhat.com> - 13.28-1
- Allow --ignoremissing to work for @base and @core (#566752).
  (clumens)
- Add device node names to the filter UI, hidden by default (#566375).
  (clumens)
- logging: initialize tty3 logging in anaconda_log, along with all other
  basic loggers. (akozumpl)
- logging: introduce stderr logger and use it for critical situations in
  kickstart.py. (akozumpl)
- logging: Loggers live a cosmopolitan life, forget about them after
  created. (akozumpl)
- logging: remove AnacondaLog's unused default parameter. (akozumpl)
- logging, fix: setting remote logging from kicstart (akozumpl)
- logging: addFileHandler does not set autoLevel by default (akozumpl)
- Allow deleting the interface property, too (#566186). (clumens)

* Tue Feb 16 2010 Chris Lumens <clumens@redhat.com> - 13.27-1
- Fix hiding the advanced button on the filter UI (#555769, #565425,
  #560016). (clumens)
- PartitionDevice._setDisk: self.disk can be None. (#565930) (dlehman)
- Add currentSize method to the PartitionDevice class (#565822) (hdegoede)
- Fix instData removal mis merge (hdegoede)
- Require a format to have a mountpoint before testing for RO (#565879).
  (clumens)
- The step is named cleardiskssel, not cleardisksel (#565873). (clumens)
- Use the LUKS UUID, not the filesystem UUID for dracut. (#561373) (dlehman)
- Show the correct device path when formatting as swap or luks. (dlehman)
- Fix ordering of arguments to xfs_admin for writing fs label. (#556546)
  (dlehman)
- Log only the disks' names in PartitionDevice._setDisk. (dlehman)
- Check for the updates directory before using it (#565840). (clumens)
- Fix a handful of simple pychecker errors. (clumens)
- Add the .libs directories to PYTHONPATH so pychecker works again. (clumens)
- Warn when ignoring BIOS RAID members (#560932) (hdegoede)
- Intel BIOS RAID array not recognized (#565458) (hdegoede)
- Fix traceback in filter_gui.py when dealing with RAID10 BIOSRAID (#565444)
  (hdegoede)
- Remove newly added partition from disk if subsequent commit fails.
  (#559907) (dlehman)
- Use property() so we can assign to anaconda.intf (#565639). (clumens)
- Don't always set anaconda.upgrade to be True (#565622). (clumens)
- Re-remove the end of line from pychecker-false-positives. (clumens)
- cryptPassword is not part of any class (#565611). (clumens)
- Fix another missing import (#565599). (clumens)
- Add a missing import (#565592). (clumens)
- createLuserConf is not a part of any class (#565306). (clumens)

* Fri Feb 12 2010 David Lehman <dlehman@redhat.com> - 13.26-1
- Fix return values for dasd_settle_all() in linuxrc.s390 (#558881).
  (dcantrell)
- Don't reset the default package selection on text installs (#564103).
  (clumens)
- Remove rules handled by the device-mapper package's rules. (dlehman)
- Raise default lvm extent size from 4MB to 32MB. (dlehman)
- Add udev_settle after setup of LUKSDevice. (#534043) (dlehman)
- Pass '--force' to vgremove to avoid interactive prompts. (#563873)
  (dlehman)
- Find rsyslog libs in $LIBDIR not /usr/$LIBDIR (jkeating)
- "_Do_ override BASEARCH with BUILDARCH, it does make sense (#524235)"
  (msivak)
- Don't traceback during kickstart if no ignoredisk line is given (#563581).
  (clumens)
- Allow any add-on python module to be updated via an updates.img. (clumens)
- Correct references to lcs and ctcm devices (#561816). (dcantrell)
- Use lsznet.raw from s390utils package (#563548). (dcantrell)
- Revert "Write ARP=no to ifcfg file when VSWITCH=1 is set on s390x
  (#561926)." (dcantrell)
- Use /sys/devices/lcs instead of /sys/devices/cu3088 (#561816). (dcantrell)
- Wait for all DASDs to be online after autodetection (#558881). (dcantrell)
- Prompt user for install method when going back to STEP_METHOD. (dcantrell)
- Set initrd load address to 32MB for s390x (#546422). (dcantrell)
- Only show the error message if there was an error. (dlehman)
- Be even more clear about removing existing linux installations. (#493360)
  (dlehman)
- Improve reboot modes in init.c and shutdown.c. (akozumpl)
- Be more explicit in which libraries we link with. (clumens)
- Do not override BASEARCH with BUILDARCH, it doesn't make sense (#524235)
  (msivak)
- platform.checkBootRequest(): Fix use of map instead of filter (hdegoede)
- Improve platform.checkBootRequest() mdarray handling (hdegoede)
- Fix backtrace when trying to use LV for /boot (#562325) (hdegoede)
- Add lsusb to rescue mode stage2 (#562616) (hdegoede)
- No longer refer to instdata in attrSkipList. (clumens)
- Clarify which storage exceptions are bugs (#557928). (clumens)
- Merge branch 'no-instdata' (clumens)
- Fix partitioning help spelling (#562823). (clumens)
- Keep the end sector aligned when resizing partitions (#560647) (hdegoede)
- Write ARP=no to ifcfg file when VSWITCH=1 is set on s390x (#561926).
  (dcantrell)
- Don't return the passphrase from hasKey. Should return a boolean. (dlehman)
- Fix splitting of error strings from program.log. (dlehman)
- Take advantage of default size for new partitions. (dlehman)
- Add a default size of 500MB for new partition requests. (dlehman)
- Remove check for MD_DEVNAME from udev_device_is_md. (#562024) (dlehman)
- Don't try to specify bitmap for RAID0 since mdadm doesn't allow it.
  (#562023) (dlehman)
- Use 0 for a default max_req_size instead of None. (dlehman)
- Add missing methods to RescueInterface (pjones)
- Clean up imports in __main__. (clumens)
- Nothing uses InstallData anymore, so it can completely be removed.
  (clumens)
- Last attribute out of InstallData, please turn out the lights. (clumens)
- Move firstboot into the Anaconda object. (clumens)
- Move bootloader into the Anaconda object. (clumens)
- Move escrowCertificates into the Storage object. (clumens)
- Move storage into the Anaconda class. (clumens)
- Move desktop to the Anaconda object. (clumens)
- Move timezone to the Anaconda object. (clumens)
- Move firewall into Anaconda. (clumens)
- Move users and security to the Anaconda object. (clumens)
- Move network to the Anaconda object. (clumens)
- Move keyboard to the Anaconda object. (clumens)
- Move instLanguage to the Anaconda object. (clumens)
- Move the writeKS and write methods from InstallData to Anaconda. (clumens)
- Move upgrade-related data to the Anaconda object. (clumens)
- Make a bunch of Anaconda attributes into properties. (clumens)
- Move instProgress to be an attribute on the InstallInterface. (clumens)
- Finally remove the x_already_set hack. (clumens)
- Move instClass to be an attribute on Anaconda. (clumens)
- Use anaconda.ksdata instead of anaconda.isKickstart. (clumens)
- Move ksdata to be an attribute on Anaconda. (clumens)
- Remove backend and other pointless attributes from InstallData. (clumens)
- Move the isHeadless attribute onto the Anaconda class. (clumens)
- Set displayMode on the anaconda object, then refer to that everywhere.
  (clumens)
- Sort the attributes on class Anaconda for my future reference. (clumens)
- Install classes may no longer force text mode. (clumens)
- Add a Requires: for tigervnc-server (#561498). (clumens)

* Wed Feb 03 2010 David Lehman <dlehman@redhat.com> - 13.25-1
- Fix keymaps-override-ppc pickup in mk-images (#524235) (msivak)
- Fix typo in action sorting. Disklabels before partitions. (#560017)
  (dlehman)
- Display ID_PATH for zFCP devices instead of looking for a WWID. (clumens)
- Fix a variety of filtering UI problems caused by switching models around.
  (clumens)
- Add ID_SERIAL in as a backup in case there's no ID_SERIAL_SHORT. (clumens)
- Display ID_PATH instead of WWID for DASDs as well. (clumens)
- Rename the WWID column to Identifier. (clumens)
- Enforce maximum partition sizes. (#528276) (dlehman)
- Log commands as a string instead of as a list of strings. (dlehman)
- Strip off the timestamp from error output pulled from program.log.
  (dlehman)
- Fix: execWithRedirect() logging stderr at wrong loglevel. (akozumpl)
- Fix: execWithCallback() not logging stderr. (akozumpl)
- Fix:  ArithmeticError: Could not align to closest sector (#561278)
  (hdegoede)
- Fixed parsing of strings with multiple values in pyudev (mgracik)
- On text kickstart installs, doBasePackageSelect still needs to run
  (#559593). (clumens)
- Remove unused udev_parse_block_entry() function (hdegoede)
- Fixed the problem with string to list properties (#560262) (mgracik)

* Mon Feb 01 2010 Chris Lumens <clumens@redhat.com> - 13.24-1
- Don't log the size of what we're unpacking anymore. (clumens)
- Fixup partition aligning (#560586) (hdegoede)
- Fix backtrace when adding mdraid arrays (#560360) (hdegoede)
- pyudev: explicitly specify all return value and argument types (#559394)
  (hdegoede)
- Correctly add found multipath devices to our dict (#560029). (clumens)
- gtk.TreeStores are iterable, so use indices instead of iterators. (clumens)
- Build sorted models on top of filtered models to make column sorting work.
  (clumens)
- Skip the filtering UI if there's only one disk in the machine. (clumens)
- Allow getScreen methods to indicate the screen should be skipped. (clumens)
- rename constants and a variable in anconda_log.py so the names make more
  sense. (akozumpl)
- anaconda, storage and yum: log to tty3 in the same format as we log into
  tty4 (akozumpl)
- Remove /sys prefix in udev_enumerate_devices() (hdegoede)
- Use libudev's enumerate_devices function (#559394) (mgracik)
- Update =~ regexps in lsznet.raw for bash-4.1 (#558537). (dcantrell)
- Startup iscsi / fcoe / zfcp before listing drives in the filter UI
  (hdegoede)
- cleardisk_gui: Fix going back to the cleardisks gui (hdegoede)
- cleardisk_gui: Base autoselection of bootdev on detected BIOS order
  (hdegoede)
- Fix typo in partition_ui_helpers_gui.py (hdegoede)
- Remove no longer used isys EDD code (hdegoede)
- Hookup new python EDD code (#478996) (hdegoede)
- Add pure python EDD code parsing and compareDrives substitute (#478996)
  (hdegoede)
- Include /etc/netconfig in the initrd for NFS (#557704). (clumens)
- Log system messages to /tmp/syslog instead of /tmp/messages.log. (clumens)
- Make sure we always check /lib64 and /lib in find_library (#555669).
  (dcantrell)
- Make sure we get required nss-softokn libs in the images. (dcantrell)
- Add 5 second ping delay for gateway and dns test on s390x (#536815).
  (dcantrell)
- Update =~ regexps in linuxrc.s390 for bash-4.1 (#558537). (dcantrell)
- Add strace to the stage2 image and initrd. (clumens)
- multipath gives us CCISS devices names with ! in them, but we expect /.
  (clumens)
- Fix visibility counting on filter notebook pages. (clumens)
- Fix thinko in displaying the first filter notebook page that disks.
  (pjones)
- DMRaidArrayDevice don't pass major/minor to DMDevice.__init__ (#558440)
  (hdegoede)
- Filter UI: don't show cciss controllers without sets (hdegoede)
- Filter UI: give BIOS RAID sets a usable model string and display that
  (hdegoede)
- Make MDRaidArray description the same as DMRaidArray (hdegoede)
- Add DMRaidArrayDevice description and model properties (#558440) (hdegoede)
- DMRaidArrayDevices exist when created (#558440) (hdegoede)
- Clarify syslinux menu text (#557774) (hdegoede)
- Use description property for MDRaidArrayDevice model (hdegoede)
- MDRaidArrayDevice: Get rid of the ugly self.devices[0].type checking
  (hdegoede)
- Make storage.unusedMDFoo also check mdcontainer members (hdegoede)
- Remove MDRaidArrayDevice biosraid property (hdegoede)
- Give MD BIOS RAID arrays there own type (hdegoede)
- Check for devices with no media present in filter_gui.py (#558177)
  (hdegoede)
- multipath requires libaio.so (pjones)
- init, fixes a bug in getSyslog() causing a SEGV (akozumpl)

* Fri Jan 22 2010 Chris Lumens <clumens@redhat.com> - 13.23-1
- Only /boot needs to be on one of the bootFSTypes. (#557718) (dlehman)
- nss files moved around again, NM needs more (#557702) (dcantrell)
- Fix broken log message. (pjones)
- MDRaidMember.__str__ add biosraid attribute to the returned string
  (hdegoede)
- Remove setting of _isDisk and _partitionable from iscsi and fcoe disk code
  (hdegoede)
- Add isDisk property to MDRaidArrayDevice (hdegoede)
- Make isDisk a property (hdegoede)
- Remove DMRaidDevice.mediaPresent method (hdegoede)
- Honor clearPartDisks when clearing whole disk formatting formatted disks
  (hdegoede)
- Fixup MDRaidArrayDevice.biosraid (hdegoede)
- Update exclusiveDisks when handling mdraid BIOSRAID in isIgnored (hdegoede)
- MDRaidDevice does not have serial, vendor or bus arguments (hdegoede)
- Don't traceback on devices without a serial (hdegoede)
- Make addUdevPartitionDevice add lvm filters for ignored partitions
  (hdegoede)
- Remove BIOSRAID see if ignored again code from addUdevPartitionDevice
  (hdegoede)
- Remove special partition handling from isIgnored (hdegoede)
- Fix MDRaidArrayDevice mediaPresent to not depend on paritioned state
  (hdegoede)
- Special handling for mdraid BIOS RAID sets in exclusive disks (hdegoede)
- 2 small mdraid related storage/udev.py changes (hdegoede)
- Fix an infinite loop by properly iterating over the disks store (#557856).
  (clumens)
- Prevent init from telling us its story if the shutdown was planned.
  (akozumpl)
- Add a description attribute to MDRaidArrayDevice (hdegoede)
- Don't do exclusiveDisks checking for BIOS RAID members (hdegoede)
- Fix a syntax error in filter_gui.py (hdegoede)
- Make multipath support use device-mapper-multipath to setup mpaths.
  (pjones)
- Make PartitionDevice have its own teardown() when used with mpath. (pjones)
- Create multipath.conf (pjones)
- Make sure MultipathDevice is setup correctly. (pjones)
- List biosraids w/ disks and don't include them w/ md arrays in partgui.
  (dlehman)
- Add biosraid property and use it in MDRaidArrayDevice.partitionable.
  (dlehman)
- Make partitionable a property of StorageDevice instead of a plain attr.
  (dlehman)
- Remove the multipath name generator, it is no longer used. (pjones)
- Set StorageDevice.exists before calling Device.__init__ (pjones)
- Add another command to .bash_history. (pjones)
- Introducing a proper syslog daemon allows us to remove the syslogd stub we
  have. (akozumpl)
- Merge branch 'forward_all' (akozumpl)
- Python logging is talking to the syslog daemon. (akozumpl)
- make dracut only activate the root LV (#553295) (hdegoede)

* Wed Jan 20 2010 David Cantrell <dcantrell@redhat.com> - 13.22-1
- Add mpath device to selection instead of its constituents. (pjones)
- Make all StorageDevice-s support .vendor and .model (pjones)
- Add a parser for 'multipath -d' output. (pjones)
- Multipath members should not be added to the ignored disk list. (pjones)
- Add udev accessor for ID_MODEL_FROM_DATABASE/ID_MODEL. (pjones)
- Add udev_device_get_multipath_name(). (pjones)
- Use mpath names instead of serials to group them. (pjones)
- Add an exception to use when multipath fails. (pjones)
- Add missing log_method_call()s. (pjones)
- Introduces rsylogd to anaconda (part of #524980) (akozumpl)
- Fix compile problem from 65a3c05. (akozumpl)
- Remove unnecessary free from the rpmextract error handler (msivak)
- Fix SIGSEGV in dlabel feature (#556390) (msivak)
- Support ignore all/reinit all on the disk reinitialization question
  (#512011). (clumens)
- Handle reboot better on s390 (#533198) (dcantrell)
- Reset network setting input counters for IPv4 and IPv6 (#553761).
  (dcantrell)
- Fix reading dasd status sysfs attribute (#536803). (dcantrell)
- Fix whitespace error that was introduced. (pjones)
- setStage2LocFromCmdline() shouldn't strdup so much. (pjones)
- s390 CHPID types must be treated in hex for lookup table to work (#552844)
  (maier)
- Fixed the setting of LD_LIBRARY_PATH in rescue (mgracik)
- Use StorageError insead of enumerating all the different storage errors.
  (pjones)
- Get rid of "stage2param" in parseCmdLineFlags(); it is unused. (pjones)
- Make clearDisksWindow use device.model not device.partedDevice.model
  (pjones)
- Include device-mapper-multipath in stage2.img (pjones)
- Load all scsi_dh_* modules, since they can't be modprobe by aliases...
  (pjones)
- Display the first filter notebook page that has any disks on it. (clumens)
- The firmware and additional-web-server groups no longer exist (#555609).
  (clumens)
- Fix a traceback adding RAID devices to the filtering UI. (clumens)
- reIPL code cleanup in loader (dcantrell)
- Show call depth with spaces in log_method_call() (pjones)
- iutil.execWithRedirect() hasn't used searchPath= since 2006.  Take it out.
  (pjones)
- Look for the SSH config file in /etc/ssh on s390 as well (#555691).
  (clumens)
- Changed the architecture check from __ppc64__ to __powerpc64__ (#555669)
  (mgracik)
- Fix the blkid infinite loop. (#555601) (msivak)
- Testing mode was removed. (rvykydal)
- There's no reason to keep bits of mkinitrd in upd-instroot. (pjones)
- Support the new excludedGroupList in pykickstart (#554717). (clumens)
- Use passed in anaconda parameter instead of relying on handler (hdegoede)
- kickstart.py: Fix stdoutLog not being defined (hdegoede)
- pylint error fixes round 2 (hdegoede)
- Fixup various errors detected by pylint (hdegoede)
- mdraid: various changes to options for new mdraid array creation (hdegoede)
- Emit a dracut setup string for the root device itself (hdegoede)
- Fix path mistakes in dasd_settle() in loader/linuxrc.s390 (dcantrell)
- Do not write HWADDR to ifcfg file on s390x for OSA Layer 2 (#546005)
  (dcantrell)
- Poll DASD status for 'online' or 'unformatted' (#536803) (dcantrell)
- Add back hald for Xorg input device queries (#553780) (dcantrell)
- Support moving multiple rows at once in the cleardisks UI. (clumens)
- Allow disks in the filter and cleardisks UIs to be selected via
  double-click. (clumens)
- Don't log the big parted.Partition string every time we do a flag op.
  (dlehman)
- Check for disklabels on unpartitionable devices. (#539482) (dlehman)
- Make partitioned attr depend on whether the device is partitionable.
  (dlehman)
- Make sure to clear partitions before destroying a disklabel. (dlehman)
- Raise an exception when /etc/fstab contradicts detected fs type (#536906)
  (dlehman)
- Don't include read-only filesystems in fsFreeSpace. (#540525) (dlehman)
- NTFS filesystems are not really modifiable in any real sense. Admit it.
  (dlehman)

* Tue Jan 12 2010 Chris Lumens <clumens@redhat.com> - 13.21-1
- Fix implicit declaration of things in sys/stat.h. (clumens)

* Tue Jan 12 2010 Chris Lumens <clumens@redhat.com> - 13.20-1
- devicetree.devices is a list, not a dict (#554455). (clumens)
- Try to copy the correct traceback file, not anacdump.txt. (clumens)
- Make sure /tmp/DD exists before trying to copy it. (clumens)

* Fri Jan 08 2010 David Cantrell <dcantrell@redhat.com> - 13.19-1
- st_size is off64_t on i386, off_t on others. (dcantrell)

* Fri Jan 08 2010 David Cantrell <dcantrell@redhat.com> - 13.18-1
- RPM version check correction. (dcantrell)

* Fri Jan 08 2010 David Cantrell <dcantrell@redhat.com> - 13.17-1
- fstat->st_size is a long unsigned int, not a long long unsigned int.
  (dcantrell)
- Use libarchive and rpm pkg-config files during build. (dcantrell)
- Take ignoredDisks into account on the filter screen as well. (clumens)
- Don't wait on the filtertype screen on kickstart installs. (clumens)
- Our overridden AutoPart class must be mentioned in commandMap. (clumens)
- Reword filter UI introductory text to be less confusing. (clumens)
- Install the driver discs according to what was loaded in stage1 (msivak)
- Use the updated DriverDisc code in loader (msivak)
- Backport the RHEL5 DriverDisc functionality (msivak)
- Include depmod in stage1 and set it to prefer the DD directory (msivak)
- Add a function to get paths to loaded modules (msivak)
- Add rpm extraction routines (use librpm and libarchive) (msivak)
- Add DriverDisc v3 documentation (msivak)
- When displaying the filter UI, check devices that are in exclusiveDisks.
  (clumens)
- get rid of global import of anaconda_log (akozumpl)
- introduce loglevel flag and use it in yum's tty3 logging (akozumpl)
- Remove LoggerClass but maintain loglevel= functionality (akozumpl)
- Do not duplicate exclusiveDisks when going back to filtering UI. (rvykydal)
- Fixes problems in the manual network configuration screen in loader with
  IPv6. (akozumpl)
- Bring back missing IPv6 pieces that were lost in time. (dcantrell)
- Add configuration option to enable/disable IPv6 support. (dcantrell)
- Ask about LVM inconsistencies only in storageinit step. (rvykydal)
- Ask about disk initialization only in storageinit step. (rvykydal)
- Fix partition request sorting based on number of allowed disks. (#540869)
  (dlehman)

* Wed Jan 06 2010 Chris Lumens <clumens@redhat.com> - 13.16-1
- Add libblkid as a BuildRequires. (clumens)

* Wed Jan 06 2010 Chris Lumens <clumens@redhat.com> - 13.15-1
- Also remove requirement for libbdevid (hdegoede).
- Update the python-pyblock version requirement, too. (clumens)
- Bump the required version numbers on a couple of components. (clumens)
- ID_BUS is not always defined (on virt, for instance) so handle that.
  (clumens)
- opts should always be treated as a list inside isys.mount(). (clumens)

* Mon Jan 04 2010 Chris Lumens <clumens@redhat.com> - 13.14-1
- Include fontconfig files needed for scaling of Meera fonts (#531742,
  #551363). (clumens)
- Don't write dracut kernel cmdline paramters to anaconda-ks.cfg (hdegoede)
- Write dracut rd_NO_foo options to grub.conf (hdegoede)
- Add dracutSetupString methods to all relevant device classes (hdegoede)
- Avoid duplicate kernel cmdline options and cleanup booty dracut code
  (hdegoede)

* Wed Dec 23 2009 Chris Lumens <clumens@redhat.com> - 13.13-1
- lsreipl from s390-utils uses incorrect path (hamzy).
- fix for a bug in 05ce88b2 that split one line over several in program.log
  (akozumpl)
- Dump the initial and final state of the system's storage devices. (dlehman)
- Add a "dict" attribute to Device and DeviceFormat classes. (dlehman)
- Sort Storage.devices by name (not path) for consistency. (dlehman)
- Put fsprofile support back in. (dlehman)
- Fix reset of lvm filtering (#527711) (rvykydal)
- Fix bootloader driveorder dialog. (rvykydal)
- Fix selection of default boot target in UI (#548695) (rvykydal)
- 'cleardiskssel' typos that made it impossible to run text install.
  (akozumpl)

* Fri Dec 18 2009 David Cantrell <dcantrell@redhat.com> - 13.12-1
- Use the per-disk flag to disable cylinder alignment for msdos disklabels.
  (dlehman)
- Don't include advanced devices in the total count on the basic filter UI.
  (clumens)
- For iSCSI devices, put the path into the UI instead of a WWID. (clumens)
- Add udev_device_get_path. (clumens)
- Make Callbacks._update_size_label callable from outside the object.
  (clumens)
- Do not show the "Add Advanced" button on the basic filtering screen.
  (clumens)
- Log into program.log through the standard python logging (part of
  #524980). (akozumpl)
- Fix typo from commit 13022cc2. (dlehman)
- Restore accidentally removed line in backend.py (hdegoede)
- yuminstall: Fix indentation error (hdegoede)
- No need to special case ignoring of dmraid sets (hdegoede)

* Wed Dec 16 2009 Chris Lumens <clumens@redhat.com> - 13.11-1
- Clean up setting paths on preupgrade (jvonau). (clumens)
- And call freetmp, too. (Jerry)
- Add a method to remove /tmp/install.img on low memory conditions (jvonau).
  (clumens)
- Make sure /mnt/stage2 is mounted before trying to unmount. (Jerry)
- Skip the mediaDevice check before attempting to mount the install.img.
  (Jerry)
- Remove install.img from /boot during preupgrade. (Jerry)
- Add __str__ methods to the DeviceFormat classes. (dlehman)
- Expand PartitionDevice.__str__ to include partition geometry and flags.
  (dlehman)
- Hide biosraid member devices that contain MDRaidMember formats. (dlehman)
- Move disklabel handling into handleUdevDeviceFormat with the others.
  (dlehman)
- DiskDevice.__init__ expects an "exists" parameter, so add it. (clumens)
- Fix multipath filtering. (clumens)
- Log error messages before displaying dialogs. (clumens)
- Include error messages when logging selinux context get/set failures.
  (dlehman)
- Catch failures to set selinux contexts so it doesn't cause a crash.
  (dlehman)
- Fix typo logging failure to get default file context. (dlehman)
- Use DiskLabel.alignment instead of getDiskAlignment. (dlehman)
- Add an alignment property to DiskLabel. (dlehman)
- iscsi.py: Do not translate log messages (hdegoede)
- Make iscsi,etc startup use the iscsi,etc Singletons (hdegoede)
- kickstart: Move onlining of fcoe/iscsi/zfcp devices to parse phase
  (hdegoede)
- Make the fcoe, iscsi and zfcp classes singletons (hdegoede)
- Remove call to no longer existing isys DriveDict method (hdegoede)
- Use the correct yum configuration file when searching for the -logos
  package (kanarip)
- Fix two missing closing parens in previous commits. (clumens)
- Add an interface to select the fancy filtering UI vs. the regular one.
  (clumens)
- Add a step to prompt for the cleardisks UI. (clumens)
- Add a dialog to configure advanced storage devices. (clumens)
- Add an early user interface for filtering storage devices. (clumens)
- Rework the upgrade vs. install screen a bit to make it look nicer.
  (clumens)
- Add the updated and simplified parttype screen. (clumens)
- Add a method to determine whether a device is a CCISS RAID device.
  (clumens)
- Move identifyMultipaths from DeviceTree to devicelibs. (clumens)
- Add a method to return a device's WWID. (clumens)
- Add a method to get the bus/interconnect from udev and store it on
  devices. (clumens)
- Add a vendor getting udev method, though udev doesn't always know it.
  (clumens)
- Add the serial number to all DiskDevices and subclasses. (clumens)
- Put less space between rows and allow text to be longer before wrapping.
  (clumens)
- Allow InstallInterfaces to modify the installation steps. (clumens)
- Default /boot to 500 MB. (clumens)
- Some iscsi cleanups (hdegoede)
- Bring auto discovered drives online before parsing the ks file (hdegoede)
- Make a better effort at tearing down everything before action processing.
  (dlehman)
- Tighten restrictions on the type of disklabel on x86 and EFI boot disks.
  (dlehman)
- Use string instead of parted.diskType for disklabel types. (dlehman)
- A couple of cleanups to warnings about formatting preexisting devices.
  (dlehman)
- Rework udev_settle timeout handling (#544177) (hdegoede)
- Remove smp.c from the Makefile.am, too. (clumens)
- Nothing has a kernel-smp anymore so none of this code is useful. (clumens)
- Get rid of the goofy nested try statements. (clumens)
- update reIPL messages (hamzy)
- Change btrfs command line option (josef)

* Wed Dec 09 2009 Chris Lumens <clumens@redhat.com> - 13.10-1
- Kickstart support for unpartitioned disks. (dlehman)
- Skip disklabel handling for biosraid and multipath members. (dlehman)
- Improve disklabel's name attr so we don't have to hide them anymore.
  (dlehman)
- Hide devices with certain formatting in the main partitioning UI. (dlehman)
- Automatic partitioning support for whole-disk formatting. (dlehman)
- Add support for whole-disk formatting. (dlehman)
- Add per-row control over sensitive property for CheckList and
  WideCheckList. (dlehman)
- Use a function to add a device to the partition gui. (dlehman)
- Don't crash if there's no intf passed to getLUKSPassphrase. (dlehman)
- Remove unused selinux file context functions from isys. (dlehman)
- Use selinux python module for file context operations. (dlehman)
- Obtain device alignment information from parted. (#529051) (dlehman)
- Handle roots with or without trailing "/" in FileDevice.path. (#541473)
  (dlehman)
- sundries.h is no longer used. (clumens)
- Kill yet another unused lodaer flag. (clumens)
- stage1 (init): Make /tmp tmpfs large enough to hold install.img (#540146)
  (hdegoede)
- With flags.setupFilesystems gone, justConfig can be removed from booty.
  (clumens)
- Nothing sets flags.setupFilesystems anymore, so it can go too. (clumens)
- Remove test mode from the loader, too. (clumens)
- Complain if we're started in test or rootPath mode instead of aborting.
  (clumens)
- Remove test mode. (clumens)
- Remove rootPath mode. (clumens)
- Enable method/repo nfs options in stage2. (rvykydal)
- Accept "nfs:" prefix in ks repo --baseurl setting beside "nfs://".
  (rvykydal)
- Display url having invalid prefix in repo editing dialog. (rvykydal)
- Do not traceback on invalid ks repo --baseurl values (#543003) (rvykydal)
- Remove /etc/localtime before trying to copy into it (#533240). (akozumpl)
- Whenever storage code tries to log a method call, do so into the
  'tmp/storage.log' file. (a part of #524980) (akozumpl)
- Make loader log time with milliseconds (part of #524980). (akozumpl)
- Log storage in the same format as the main anaconda log (a part of
  #524980) (akozumpl)

* Tue Dec 01 2009 Chris Lumens <clumens@redhat.com> - 13.9-1
- Improve text mode fcoe interface (hdegoede)
- Fix udev rule to test whether we're in anaconda. (dlehman)
- Fix devicelibs.dm.device_is_multipath support for new udev rules. (pjones)
- Display progress or wait window when creating devices. (dlehman)
- Display progress or wait window when formatting devices. (dlehman)
- Add optional progress windows to devicelibs create functions. (dlehman)
- Force mkswap to do its job. (dlehman)
- Don't try to get dm node or update sysfs path for lvm vgs. (dlehman)
- Log upon leaving installer steps as well as entering (a part of #524980).
  (akozumpl)
- An unitialized variable in iw/partition_gui.py and a typo in kickstart.py
  (akozumpl)
- Add DCB option to text mode FCoE setup (#513011) (hdegoede)
- Add DCB option to GUI FCoE setup (#513011) (hdegoede)
- Add DCB option to kickstart FCoE code (#513011) (hdegoede)
- Add support for DCB to fcoe.py (#513011) (hdegoede)
- Include fcoemon and dcbd in install.img for FCoE DCB support (#513011)
  (hdegoede)
- Add RAID4 support (#541433) (oliva)
- Clear a partition's BOOT flag when formatting it (hdegoede)
- Do not set boot flag when there is already a partition with the flag
  (#533658) (hdegoede)
- Fixes a syntax error in commit b495db2cd56c881a7e661ac55bd31069510cf662.
  (akozumpl)
- If /boot is too small to preupgrade, don't allow going back (#499321).
  (clumens)
- One reference to earlyKS somehow survived.  Kill it. (clumens)
- Quote backticks when writing out the .bash_history file, and add another
  cmd. (clumens)
- Set the default keyboard based on language before showing the UI
  (#532843). (clumens)
- Don't attempt to get the size of a filesystem unless it's supported
  (#540598). (clumens)
- Require /boot to be on a GPT or MSDOS disk label on x86 (#540588).
  (clumens)
- Fix killall -USR2 anaconda writing out a traceback file. (clumens)
- Only check for DEVICE_DASD in S390.diskLabelType, not for all platforms.
  (clumens)
- Use installclass to make the bootloader timeout 5 seconds on RHEL. (pjones)
- Make sure we get tcp_wrappers-libs installed for stage 2 (pjones)
- Mount usbfs before installing packages (#532397) (mmatsuya)
- Use fs with largest amount of freespace to store install.img (hdegoede)
- Always update booty drivelist before filling bootstore (#533335) (hdegoede)
- Enhance drive specification for clearpart, ignoredisk, and partition.
  (clumens)
- Add a function that determines which devices match a given shell glob.
  (clumens)
- Extend udev_resolve_devspec to allow specifying devices in more ways.
  (clumens)
- Name log files something that doesn't conflict with the system (#539542).
  (clumens)
- Adds interactive install support for NFS options (#537764) (akozumpl)
- Introduces check_asprintf macro that checks asprintfs return value and
  terminates program in OOM scenarios. (akozumpl)
- Sleep if the kickstart file read fails (#537361) (akozumpl)
- Move libcurl initialization to urlinstTransfer() (#537870). (dcantrell)
- Replace all popt use with glib's option parsing code. (dcantrell)
- Clean up initProductInfo() in loader.c. (dcantrell)
- Use glib string parsing functions in driverselect.c. (dcantrell)
- If a package has %%pre/%%post scriptlet errors, abort the install
  (#531599). (clumens)
- If a package has a dependency problem, offer to continue/abort (#511801).
  (clumens)
- Generate more complete device.map grub file when upgrading grub. (#533621)
  (rvykydal)
- Added the libudev python bindings (mgracik)
- If the kickstart log file's path doesn't exist, make it. (clumens)
- Don't make chown or lsetfilecon errors fatal (#529940). (clumens)
- Get correct boot device in reIPL code for s390 (#537390). (hamzy)
- Expand the proxy table a little bit to reduce clutter (#537878). (clumens)
- Use glib data structures in loader's module handling code. (dcantrell)
- Various improvements to kickstart scriptlet reporting (#510636). (clumens)

* Thu Nov 12 2009 David Cantrell <dcantrell@redhat.com> - 13.8-1
- Ignore merge commit messages when generating the rpm changelog. (dcantrell)
- Remove last references to hal. (dcantrell)
- Log calls to DiskLabel's commit and commitToDisk methods. (dlehman)
- Fix DiskLabel.status so it returns True, not self.partedDisk, when active.
  (dlehman)
- Write /etc/dasd.conf to target system on s390 (#533833). (dcantrell)
- Latest dracut has new syntax for rd_DASD. (dcantrell)
- Handle case of not enough space in VG more gracefully. (#533797) (dlehman)
- Make sure partitioning-related drive lists are sorted properly. (#534065)
  (dlehman)
- Remove the early kickstart processing pass (#532453). (clumens)
- Move all the important stuff out of the KickstartCommand.parse methods.
  (clumens)
- These changes require a later version of pykickstart. (clumens)
- commandMap and dataMap are now updates to the existing dict. (clumens)
- Set a reference to the kickstart handler on BaseData objects. (clumens)
- Move exception setup to right after instdata is populated. (clumens)
- Leave one free logical block before each logical partition. (dlehman)
- Use Chunk's geometry attr to access the parted Geometry. (dlehman)
- Fix sorting of requests by mountpoint. It was backwards. (dlehman)
- Align logical partitions' start sector up one logical block for metadata.
  (dlehman)
- Use parted.Device's sectorSize attr instead of physicalSectorSize.
  (dlehman)
- Select partition layout based on potential for growth. (dlehman)
- Reimplement partition growing. (dlehman)
- Create and use a function to obtain a parted alignment for a disk.
  (dlehman)
- Create and use a new function to create and add new partitions to disk.
  (dlehman)
- Make and use a new function to remove non-existent partitions. (dlehman)
- Disable parted's cylinder alignment code. (dlehman)
- Use new functions for conversion between size and sector count. (dlehman)
- Consider whether a partition is growable when choosing free space.
  (dlehman)
- Allocate fixed-size requests before growable requests. (dlehman)
- For the catch-all case, put the message into the UI, not the exn
  (#536854). (clumens)
- Add a missing binary to KEEPFILES (#533237) (msivak)
- Set boot flag for /boot on mdraid 1 array too (#533533). (rvykydal)
- Report no media present for cpqarray controllers with no disks attached
  (hdegoede)
- Honor existing RUNKS conf file variable on s390 (#513951). (dcantrell)
- Add "Hipersockets" to qeth NETTYPE description (#511962). (dcantrell)
- Set custom_icon to error for advanced storage dialog errors (hdegoede)
- When creating a new md array check we have enough members (#533027)
  (hdegoede)
- Convert string.find calls into something modern (jkeating)
- rescue: Don't copy install.ing to /tmp when not enough RAM (#531304,
  #529392) (jvonau)
- isys: remove stray debug printf (#533597) (hdegoede)
- Don't activate / de-activate dmraid sets on setup / teardown (hdegoede)
- Remove previous mdadm bug 523334 workaorund (hdegoede)
- Don't stop mdraid containers or their arrays (#532971) (hdegoede)
- Include the command line to put anaconda into debugger mode in history.
  (pjones)
- Allow remote(ish) debugging. (pjones)
- Make sure /var/log/lastlog is there so we don't have ugly logs. (pjones)
- Correct modopts initialization in loader (take 2) (#531932). (dcantrell)
- Get rid of dead code, and fix gettimespecofday's math. (pjones)
- Don't exec without forking first when calling udevadm. (pjones)
- If init or loader exit unexpectedly, traceback. (pjones)
- Fix the vim magic in this file to work. (pjones)
- Add handling for sshpw command. (pjones)
- Improve createLuserConf behavior and chroot behavior in users.* (pjones)
- Improve logging of ssh-keygen. (pjones)
- Remove tabs in "anaconda" (pjones)
- pidof is a symlink to killall5, so we need that as well. (pjones)
- Correctly initialize modopts in loader (#531932). (dcantrell)
- Increase the size of /boot a little bit (#530555). (clumens)
- Modify autopart requests to include a separate /home (#150670). (clumens)
- Take the spec's requiredSpace into account when creating LVs. (clumens)
- Add the PartSpec.__str__ method for debugging. (clumens)
- Trim the inital / off the mountpoint before making an LV name from it.
  (clumens)
- Remove "anaconda" from attributes to skip (#532612, #532737). (clumens)
- Fix status for and consolidate handling of '-' in vg/lv names. (#527302)
  (dlehman)
- Rename "setupShellEnvironment" to "setupSshd".  That's all it does.
  (pjones)
- Put "killall -USR2 anaconda" in a pre-populated history. (pjones)
- Only try to split proxy commands out if there's actually one specified.
  (pjones)
- Consolidate the parsing of nfs: locations for ks= and stage2= (#529197)
  (stijn)
- Copy cio_ignore kernel parameter to zipl.conf on s390 (#475675).
  (dcantrell)
- Do not modify /etc/hosts from setup package (#530343). (dcantrell)
- In execWithCallback(), support disabling stdout echo (#528386) (dcantrell)
- Select drives in partition dialog, preserving settings. (#529931) (dlehman)
- Clear pot and po updates after a 'make release' or 'make archive'.
  (dcantrell)
- Use the new anaconda image in fedora-logos (#529267). (jkeating)
- Call udev_trigger with a "change" action and don't filter out dm devices.
  (dlehman)
- Remove unused attr_nomatch keyword argument from baseudev.udev_trigger.
  (dlehman)
- Fix logging of isys mount/umount into program.log. (rvykydal)
- Fix "resize failed: 1" errors for ext2/ext3/ext4 (#517491). (dcantrell)
- Log why we're exiting the installer in storage.DASD.startup() (dcantrell)
- Improve detailedMessageWindow() in text.py. (dcantrell)
- Use 'zerombr' kickstart command for DASDs needing dasdfmt (#528386).
  (dcantrell)
- Add 'zerombr' to list of early kickstart commands we look for. (dcantrell)

* Thu Oct 29 2009 Chris Lumens <clumens@redhat.com> - 13.7-1
- TypeError: '_ped.DiskType' object is not callable (#531730) (hdegoede)
- Fix upgrade of GRUB with md raid boot for versions F11 and earlier.
  (rvykydal)
- Remove another code duplication in grub upgrade code. (rvykydal)
- Remove code duplication, use fixed code from writeGrub. (rvykydal)
- Remove target parameter from grub installation code - it is no more
  needed. (rvykydal)
- Remove support for IUCV networking devices on s390. (#531494) (dcantrell)
- Find and format any unformatted DASD devices (#528386). (dcantrell)
- Improve detailedMessageWindow() in text.py. (dcantrell)
- Create execWithCallback() function in iutil. (dcantrell)
- preexist -> onPart (#531407). (clumens)
- Add sshd support for non-s390 platforms. (pjones)
- When doing initlabel on a dasd disk create a dasd disklabel (#531209)
  (hdegoede)
- Rename platform.diskType to platform.diskLabelType (hdegoede)
- Fix arrow key cycling in the Edit Partition dialog (#519641). (clumens)
- Provide a single checkbox for a minimal install (#523839). (clumens)
- Fix DASD and zFCP device discovery (#530287). (dcantrell)
- Clarify the shrink target message (#530789). (clumens)
- Re-enable running udevadm. (clumens)
- max_logical -> max_logicals (#530786). (clumens)
- Filter out device-mapper devices when doing a udev_trigger. (dlehman)
- Expand udev_trigger to allow attr filtering and action specification.
  (dlehman)
- More udev fixups for device-mapper and cryptsetup temp devices. (#526699)
  (dlehman)
- Add the bcm5974 kernel module needed for some touchpads (#474225).
  (clumens)
- /boot is already being checked by the superclass, so don't check again.
  (clumens)
- Allow /boot to be on a variety of filesystems during kickstart (#529846).
  (clumens)
- Platform.bootloaderPackage -> Platform.packages (clumens)
- Bootloader choice strings were marked with N_, but never translated
  (#530017). (clumens)
- Handle more than x.y version numbers in 'make bumpver'. (dcantrell)
- Mark live device as protected instead of ignoring it. (#517260) (dlehman)
- Don't force logical with a free primary slot and an extended. (#527952)
  (dlehman)
- Use rpm to determine how to set bootloader args and default runlevel
  (#527520). (clumens)
- Improve message given to user for fsck failures (#527626). (dcantrell)
- 'Packages completed' string should use P_() instead of N_(). (dcantrell)
- Reintegrate reipl to trigger reboot/halt on s390x correctly. (#528380)
  (maier)
- Put the icon back on the Back button on livecd installs (#526925).
  (clumens)
- Make LOADER_FLAGS_NOSHELL default also for s390x not just s390 (#527063)
  (maier)
- Adapt standalone shutdown to nokill changes so s390x can use it. (#528380)
  (maier)
- Add dracutSetupData() method to DASDDevice (#526354). (dcantrell)
- Collect DASD kernel parameter information during device tree scan
  (#526354). (dcantrell)
- Add dracutSetupString() method to ZFCPDiskDevice (#526354). (dcantrell)
- Write LAYER2 and PORTNO correctly as parts of OPTIONS to ifcfg for s390x
  (maier)
- Don't set unnecessary multipath defaults. (pjones)
- Add a "File Bug" button to all possibilitys in turnOnFilesystems
  (#528006). (clumens)
- For cmdline mode, add the long text to what messageWindow will print
  (#528006). (clumens)
- Use /dev/mapper/live-osimg-min instead of the old device node name
  (#526789). (clumens)
- Remove double slash from nfs:// ks repo value for use in UI. (rvykydal)
- Make bootLoaderInfo new-style class, so that its properties work
  correctly. (rvykydal)
- liveinst: deactivate mdraid arrays before running liveinst (#528235)
  (hdegoede)
- Set parted filesystemtype for swap partitions (hdegoede)

* Tue Oct 13 2009 David Cantrell <dcantrell@redhat.com> - 13.6-1
- BR system-config-keyboard (dcantrell)

* Tue Oct 13 2009 David Cantrell <dcantrell@redhat.com> - 13.5-1
- Remove extra echo in 'make rpmlog'. (dcantrell)
- Do not traceback if network device doesn't have HwAddress property
  (#506013). (rvykydal)
- Fix liveinst to (1) not unmount /dev/pts, (2) unmount in order (509632).
  (clumens)
- Do not read DASD data from /tmp/install.cfg in booty (#526354). (dcantrell)
- Merge branch 'master' of ssh://git.fedoraproject.org/git/anaconda (notting)
- Support upgrading when the language isn't in lang-table (#528317).
  (clumens)
- Fix task selection when tasks contain the same group. (#528193) (notting)
- Update drivelist with bootloader --driveorder ks option instead of
  replacing it (#506073). (rvykydal)
- Use ID_SERIAL to write multipath.conf, but ID_SERIAL_SHORT for UI. (pjones)
- Don't run 70-anaconda.rules on an installed system (#527781). (clumens)
- Handle Installation Repo (base repo) as any other in repo edit UI.
  (rvykydal)
- Fix methodstr editing dialog. (rvykydal)
- Store methodstr url of repo (#502208, #526022). (rvykydal)
- Show user of which repository he edits the url (methodstr editing).
  (rvykydal)
- Don't traceback with malformed repo= nfs: parameter. (rvykydal)

* Mon Oct 12 2009 David Cantrell <dcantrell@redhat.com> - 13.4-1
- Missing volume_key shouldn't break LUKS support completely. (#526899)
  (dlehman)
- Write multipathd.conf in anaconda so that dracut can find it. (pjones)
- We moved from dialog to newt.. (#528497) (msivak)
- Fix a segfault when stage2= boot parameter and kickstart url method is
  used (#524417). (rvykydal)
- Fix parsing of optional portnr in iscsi target IP (#525118) (hdegoede)

* Fri Oct 09 2009 David Cantrell <dcantrell@redhat.com> - 13.3-1
- Reset PartitionDevice attributes after failed edit. (#498026) (dlehman)
- Add MultipathDevice.getDMNode(), because .updateSysfsPath() needs it.
  (pjones)
- Add MultipathDevice.updateSysfsPath() (pjones)
- Run implantisomd5 on boot.iso on x86. (bz#526902) (pjones)
- Consider encryption when checking for duplicate mountpoint. (#526697)
  (dlehman)
- Fix grub stage1 installation for /boot on md raid1. (rvykydal)
- Do not show the VNC-over-text question, when there is not enough memory
  for GUI (#527979) (msivak)
- Fix filtering out of 'Sending translation for' log messages in bumpver.
  (rvykydal)
- Use addUdevPartitionDevice() for adding dmraid / multipath partitions
  (#527785) (hdegoede)
- Set partedPartition system to the correct FS when creating an FS (hdegoede)
- Reset parted flags in createFormat not destroyFormat (hdegoede)
- Default to mbr bootloader target for mdraid 1 boot device too (#526822).
  (rvykydal)
- Clear out state before calling XkbGetState. (clumens)

* Thu Oct 08 2009 Radek Vykydal <rvykydal@redhat.com> - 13.2-1
- Override fstabSpec in PartitionDevice for by-path DASD (#526364). (dcantrell)
- Create DASDDevice objects for DASD devices when building devicetree.
  (dcantrell)
- Add udev_device_is_dasd() to detect DASD devices. (dcantrell)
- Change existing call to deviceNameToDiskByPath(). (dcantrell)
- Make storage.devices.deviceNameToDiskByPath() more robust. (dcantrell)
- Do not copy over 70-persistent.rules if instPath is '' (#527707) (dcantrell)
- Filter out 'Sending translation for' log messages in bumpver. (dcantrell)
- Don't copy _raidSet, but merely pass around a reference (hdegoede)
- Action...Format setup device before modifying the partition table (hdegoede)
- map() -> filter() in storage.writeEscrowPackets() (dcantrell)
- lokkit has moved to a subpackage, so require that (#523709). (clumens)
- Stop trying to run xrandr (#527678). (clumens)
- Only initialize escrow packet code if there's devices that need it (#527668).
  (clumens)
- On lookup of a PartedDevice also check for _ped.DeviceException (#527699)
  (hdegoede)
- Set related ayum attributes if media is found when editing methodstr
  (#515441). (rvykydal)
- In repo editing UI do not use object we are creating (#515441). (rvykydal)

* Tue Oct 06 2009 David Cantrell <dcantrell@redhat.com> - 13.1-1
- Tell udev to ignore temporary cryptsetup devices. (#526699) (dlehman)
- Have redhat.exec reference generic.prm, not redhat.parm (dcantrell)
- Bring back cio_ignore=all, !0.0.0009 for generic.prm on s390x (#463544)
  (dcantrell)
- Take 70-persistent-net.rules generated at installation (#526322)
  (dcantrell)
- Use $LIBDIR to find the boot-wrapper file. (jkeating)
- formatByDefault: Don't traceback when mountpoint is None (#522609)
  (hdegoede)
- Don't warn /usr should be formatted when "Format as:" is already selected
  (hdegoede)
- Bring up network interface before trying to use it for FCoE (hdegoede)
- DMRaidArray: Don't report no media present when in teared down state
  (hdegoede)
- Wait for udev to settle before trying to find dmraid sets in udev DB
  (hdegoede)
- Implement the double click for free space on the bar view (jgranado)
- Pass only cCB and dcCB to the StripeGraph classes. (jgranado)
- React to a double click on a "free row" in the tree view. (jgranado)
- Create getCurrentDeviceParent function. (jgranado)
- Make sure we don't exceed the 80 character threshold (jgranado)
- Display an LVM graph on the bar view when we click on the VG's free space
  (jgranado)
- Add a free row in the LVM tree view when necessary. (jgranado)
- Reorganize the tree view related to lvm. (jgranado)
- Remove unneeded variable (jgranado)

* Mon Oct 05 2009 David Cantrell <dcantrell@redhat.com> - 13.0-1
- Remove an errant popd. Probably cut/paste error. (jkeating)
- Only add the .img file to .treeinfo if it exists. (jkeating)
- Make the netboot dir before trying to use it (jkeating)
- Only write network --netmask if one has been defined (#527083). (clumens)
- Add --label to anaconda-ks.cfg if needed (#526223). (clumens)
- Fix existing size calculation for NTFS (#520627) (dcantrell)
- Write label to filesystem if we have one set (#526226, #526242) (dcantrell)
- Add wget to the initrd, which is required for rhts. (clumens)
- Fix the check for no /boot request on PPC yet again (#526843). (clumens)
- Surround the stage2= parameter in quotes for RHEL (#526863). (clumens)
- Correct makeupdates script to work with deleted files. (jgranado)
- Stop dragging mkinitrd into the install (hdegoede)
- Add --keyword=P_ to xgettext command arguments. (dcantrell)
- Use named parameters for translatable strings with multiple params.
  (dcantrell)
- Change 'support' to 'supported' in UnknownSwapError dialog (#526549)
  (dcantrell)
- Force interface up before checking link status (#525071). (dcantrell)
- Only ignore partitions <1MB that are freespace. (#526445) (dlehman)
- Try to include error messages in lvm/mdadm exceptions. (dlehman)
- Add the create LV option. (jgranado)
- Give the proper orientation to the gtk objects. (jgranado)
- Show the information message when user hits a non-bar element. (jgranado)
- Control the sensitivity of the "delete" and "create" buttons (jgranado)
- Respond to double click on a VG, LV and RAID device. (jgranado)
- Remove the "Hide RAID/LVM" checkbox. (jgranado)
- Display a message in the bar view when user has no selected items.
  (jgranado)
- Cosmetic changes. (jgranado)
- The StripeGraph class does not need tree nor editCB (jgranado)
- Restrain from outputing any digits after the decimal point. (jgranado)
- Add a slice when the extended partition contains "free space" (jgranado)
- Reduce message size in clone screen. (jgranado)
- Add Slice size to the bar view (jgranado)
- Select the device in the treeview when its selected in the barview.
  (jgranado)
- Make canvas a class method. (jgranado)
- Incorporate all the Graph types in the custom screen. (jgranado)
- Add the Volume Group and md RAID array Graph classes (jgranado)
- Make the Bar View Code generic. (jgranado)
- Pass the device instead of the name to the add funciton. (jgranado)
- Display the device path with a smaller font and different color. (jgranado)
- Display bar view for the selected device only. (jgranado)
- Fix indentation in editCB (jgranado)
- Organize the creation of the custom screen into sections. (jgranado)
- Use a checkmark from a PNG image instead of a string. (jgranado)
- Put the size after the device name in the storage tree. (jgranado)
- Add the warning message for an invalid create. (jgranado)
- Reorganize the Customization screen a little. (jgranado)
- Remove unneeded functions & add the about messages for LVM and RAID.
  (jgranado)
- Have an intermediary screen for the "Create" action. (jgranado)
- New screen for "Create" action. (jgranado)
- New function to tell us if there is free space for a new partition.
  (jgranado)
- Edit LVM LV when user has a LV selected. (jgranado)
- Don't fail to commit partitions due to active lvm/md. (dlehman)
- Create and use DiskLabelCommitError for failure to commit. (dlehman)
- Work around partition renumbering in processActions. (dlehman)
- Re-get preexisting partitions using their original path. (dlehman)
- Don't store a copy of ActionDestroyFormat's device attr. (dlehman)
- Don't retry commiting partition table to disk (hdegoede)
- Stop /lib/udev/rules.d/65-md-incremental.rules from messing with mdraid
  sets (hdegoede)
- Don't try to do format handling on drives without media (#523467)
  (hdegoede)
- Wait for mdraid arrays to become clean before reboot / halt (hdegoede)
- Add repo --proxy= support to kickstart. (clumens)
- Pass the proxy config information to stage2. (clumens)
- Add support for proxies to the command line. (clumens)
- Add proxy support to kickstart in the loader. (clumens)
- Add a function to split up a proxy parameter into its parts. (clumens)
- libcurl supports https in addition to http, so change our tests. (clumens)
- getHostAndPath is only used by the nfs code, so move it. (clumens)
- Add initial loader UI support for proxies (#125917, #484788, #499085).
  (clumens)
- We no longer need our own FTP/HTTP protocol support code. (clumens)
- Get rid of the convertURL/UI functions, make iurlinfo just store a string.
  (clumens)
- Convert urlinstall.c to using the new urlinstTransfer function. (clumens)
- Add proxy support to urlinstTransfer by setting more curl options.
  (clumens)
- Add the urlinstTransfer function, which replaces urlinst*Transfer.
  (clumens)
- Add a function to construct an array of HTTP headers and cache the result.
  (clumens)
- Add a CURL instance to the loader data. (clumens)
- Add checks for libcurl into the makefile process. (clumens)
- Add the packages needed to support libcurl. (clumens)

* Tue Sep 29 2009 David Cantrell <dcantrell@redhat.com> - 12.32-1
- Improve loader messages in parseCmdLineFlags when passing vnc (#526350).
  (maier)
- Update po/anaconda.pot during a 'bumpver' run. (dcantrell)
- Add 'make release' as a synonym for 'make archive'. (dcantrell)
- Whitespace cleanup in loader/net.c. (dcantrell)
- Clean up getHostandPath() debugging messages for host & file. (dcantrell)
- Need an extra  on the PS1 line in /.profile (dcantrell)
- Korean font package name changed (#525597) (dcantrell)
- We can't prompt for new network info in cmdline mode (#526262). (clumens)
- yaboot supports /boot on ext4 (#526219). (clumens)
- bootloader --append= should append, not set the args list (#524004).
  (clumens)
- Don't check if /boot is under the 4MB mark on i/p Series (#526200).
  (clumens)
- "minimal" has been renamed to "core" (#526191). (clumens)
- Remove some unused isys methods. (clumens)
- Make sure the disk holding /boot is setup before setting boot flag
  (#526063) (hdegoede)
- Use temporary repo id for edited object to prevent Duplicate Repo error
  (#524599). (rvykydal)
- Do not delete repo twice or when it had not been added actually (#524599).
  (rvykydal)
- Disable repo before deleting it (#524599). (rvykydal)
- Log more, repo editing UI. (rvykydal)
- Make _enableRepo a little more readable. (rvykydal)

* Fri Sep 25 2009 David Cantrell <dcantrell@redhat.com> - 12.31-1
- Move S390MODS to inside makeBootImages(), remove libiscsi_tcp. (dcantrell)
- Require the latest and greatest python-meh. (clumens)
- Add a stub enableNetwork method for cmdline mode (#525779). (clumens)
- Adapt to python-meh passing a bug description around. (clumens)
- Return None for next part type if all primary slots full. (#524859)
  (dlehman)
- Make sure the Minimal group is selected by default on RHEL installs
  (#524561). (clumens)

* Thu Sep 24 2009 Chris Lumens <clumens@redhat.com> - 12.30-1
- Simplify s390x module list generation. (dcantrell)
- Read cmsfs* commands from $IMGPATH/usr/sbin in mk-images (dcantrell)
- Use correct kernel-bootwrapper on ppc64. (dcantrell)
- Anaconda no longer requires hal. (notting)

* Tue Sep 22 2009 David Cantrell <dcantrell@redhat.com> - 12.29-1
- Updated po/anaconda.pot (dcantrell)
- Remove ui/instkey.glade.h from po/POTFILES.in (dcantrell)

* Tue Sep 22 2009 David Cantrell <dcantrell@redhat.com> - 12.28-1
- Preserve whitespace in $CDLABEL in mk-images.x86 (dcantrell)
- Modify rhel.py installclass for current RHEL development efforts.
  (dcantrell)
- Add --brand switch support to buildinstall script. (dcantrell)
- Remove the installation number screen. (clumens)
- Remove kickstart-docs.txt, since it comes with pykickstart (#515168).
  (clumens)
- ybin, mkofboot, and ofpath moved from /usr/sbin to /sbin (#524608).
  (clumens)
- Honor ignoredisk --only-use. (#514353) (dlehman)
- Make sure user-selected mountpoint is not already in use. (#524584)
  (dlehman)
- Do not raise UI dialog in stage2 if network is set in ks (#487503).
  (rvykydal)
- Use whiptail instead of dialog in rescue mode, supports serial line better
  and looks nicer (msivak)

* Mon Sep 21 2009 David Cantrell <dcantrell@redhat.com> - 12.27-1
- Require at least system-config-keyboard 1.3.1 or higher. (dcantrell)
- Fixes for rhel installclass. (dcantrell)
- Start with all modules from kernel/drivers/s390 on s390x (#524566)
  (dcantrell)
- Do not require dhcpv6-client, package is now obsolete. (dcantrell)
- Take into account snapshots and mirrored volumes in lvm dialogs. (dlehman)
- Add handling for snapshot and mirrored logical volumes to DeviceTree.
  (dlehman)
- Add attrs to LVMLogicalVolumeDevice class for snapshots and mirrored lvs.
  (dlehman)
- Add function lvorigin to determine the name of a snapshot's origin lv.
  (dlehman)
- Add function udev_device_get_lv_attr to retrieve lv attribute strings.
  (dlehman)
- Include hidden volumes and lv attributes in udev db. (dlehman)
- Add 'install' user to start anaconda on s390x. (dcantrell)
- Set a default shell prompt for s390x installs. (dcantrell)
- Do not assume we found a module in addOption() in loader/modules.c
  (dcantrell)
- Do not try to load floppy, edd, pcspkr, or iscsi_ibft on s390x. (dcantrell)
- Handle Esc keypress in (some more) dialogs as Cancel - (#520110).
  (rvykydal)
- All the nss libraries have moved from /lib to /usr/lib (#524410). (clumens)
- Add python-nss as a requirement (#524307, #524313). (clumens)
- Call $LDSO --verify for the binary file -inside- the chroot. This fixes
  building x86 boot images on a x86_64 host system. (thomas.jarosch)
- Just grab everything in a /usr/share/fonts/lohit* directory (#523906).
  (clumens)
- Don't write an empty mdadm.conf (hdegoede)
- Write mdraid arrays to mdadm.conf in sorted order (hdegoede)
- containers and their sets must only have a UUID= parameter in mdamd.conf
  (hdegoede)
- Updated anaconda.pot file. (dcantrell)

* Thu Sep 17 2009 David Cantrell <dcantrell@redhat.com> - 12.26-1
- NetworkManagerSystemSettings.service no longer exists. (jkeating)
- udevsettle is no longer used (udevadm settle is called instead) so don't
  put it in images. (jkeating)
- nm-system-settings is no longer shipped. (jkeating)
- Port from PolicyKit to polkit (jkeating)
- Keep po/anaconda.pot in the source tree (#522072) (dcantrell)
- Do not show Unknown as filesystem type for free space. (dcantrell)
- Catch failures from write(2) in utils/snarffont.c (dcantrell)
- Don't leak fds (#520154) (jgranado)
- Initialize the opts variable. (jgranado)
- Add the help messages for the new options of makeupdates script. (jgranado)
- Revert "The Madan font should no longer be used (apparently).  (#523906)."
  (clumens)
- Fix going back from hd install UI when stage2 is given as boot param
  (#519206). (rvykydal)
- The Madan font should no longer be used (apparently).  (#523906). (clumens)
- Update the pykickstart requirement to reflect the escrow stuff. (clumens)
- add requires for sparc arches on elftoaout and piggyback we need them to
  make the tftp image (dennis)
- copy the sparc boot loader on all sparc arches (dennis)
- make sure we include sparc boot loaders on all sparc arches (dennis)
- make sure we get the sparc64 kernel on sparc (dennis)
- Check whatever contains /boot on PPC as well as the bootable part
  (#523747). (clumens)
- make a call to rpmutils to get the basearch works on all arches that dont
  have anaconda built on the basearch (dennis)
- s-c-keyboard is now provided on all architectures (#523445). (clumens)

* Tue Sep 15 2009 David Cantrell <dcantrell@redhat.com> - 12.25-1
- Use pyblock for device-mapper devices' status. (dlehman)
- load_policy has moved from /usr/sbin to /sbin (#523506). (clumens)
- Collect all modules from modules.{ccwmap|networking} on s390x (#522519)
  (dcantrell)
- Copy cmsfscat from /usr/sbin, not /usr/bin. (dcantrell)
- Remove duplicate search_cu() in linuxrc.s390 (dcantrell)
- Try harder to stop mdraid arrays (hdegoede)
- Log when we are skipping disks without media (hdegoede)
- Don't scan stopped md devices (hdegoede)
- Make udev_get_block_device() return None on failure (hdegoede)
- Do not pass --update=super-minor to mdadm for containers and sets there in
  (hdegoede)
- Write mdadm.conf lines for mdraid container formats (imsm) (hdegoede)
- Really put appended kernel cmdline arguments at the end (hdegoede)
- Install dracut-network when using network storage (hdegoede)
- Make recreateInitrd() generate a dracut initrd (hdegoede)
- Use type of device rather than name in booty target selection. (hdegoede)
- write netroot=fcoe:... to kernel cmdline in grub.conf for dracut (hdegoede)
- write ifname=eth#:MAC to kernel cmdline in grub.conf for dracut (hdegoede)
- write iscsi initiator name to kernel cmdline in grub.conf for dracut
  (hdegoede)
- Make iswmd the default (hdegoede)
- Use new icons in anaconda so we don't look so dated (#515601). (clumens)
- Prevent infinite loop in doClearPartitionedDevice. (dlehman)
- Rename doDeleteDependentDevices to doClearPartitionedDevice for clarity.
  (dlehman)
- Handle Esc keypress in dialogs as Cancel (#520110). (rvykydal)
- Don't use baseurl containing space in yum repo object (#516042). (rvykydal)
- Add escrow support (mitr)
- Add python-{nss,volume_key} to stage2, volume_key to rescue (mitr)
- Update for pykickstart with escrow support (mitr)
- Fix --encrypted when creating volumes in kickstart (mitr)
- Remove the "Remove dmraid Device" button, which isn't even hooked up.
  (clumens)
- Require the right version of system-config-date (#523107). (clumens)
- Fix setting of "Add repository" dialog title. (rvykydal)
- Update state and name of repository in list after editing. (rvykydal)
- Fix busy cursor in repo editing (#518529) (rvykydal)
- Fix busy cursor stack popping when creating formats (#518529). (rvykydal)
- Remove partitions in reverse order when clearing disks. (dlehman)
- Improve the info provided to DeviceAction.__str__. (dlehman)
- Include device id in log lines since partitions can get renumbered.
  (dlehman)
- Don't try to preserve old format attrs when reinitializing pvs. (dlehman)
- remove the no longer used initcb and initlabel DiskDevice.__init__
  arguments (hdegoede)

* Thu Sep 10 2009 Chris Lumens <clumens@redhat.com> - 12.24-1
- dmidecode is in /usr/sbin, not /usr/bin. (clumens)
- Add cmsfscat to the initrd on s390 as well (#522535). (clumens)
- Fix the gawk/awk symlink mess in the initrd (#522535). (clumens)
- No longer use /usr/bin/env (#521337). (clumens)
- It's controlunits, not controlunits.sh. (clumens)
- Get DMRaidArrayDevice's a DiskLabel format when they are added to the tree
  (hdegoede)
- Fix askmethod + stage2= (#516973, #519288, #518194) (rvykydal)

* Wed Sep 09 2009 David Cantrell <dcantrell@redhat.com> - 12.23-1
- initrd-generic.img -> initramfs.img (hdegoede)

* Wed Sep 09 2009 David Cantrell <dcantrell@redhat.com> - 12.22-1
- No longer require xfsdump, since anaconda doesn't use it anywhere
  (#522180). (clumens)
- The zonetab module has moved (#521986). (clumens)
- No longer copy over the CD/DVD repodata or repo config file (#521358).
  (clumens)
- language dracut kernel cmdline should be space seperated (#521113)
  (hdegoede)

* Mon Sep 07 2009 David Cantrell <dcantrell@redhat.com> - 12.21-1
- Require python-meh (#521661) (dcantrell)
- Handle UnknownSwapError when turning on existing swap volumes. (dcantrell)
- Check for a valid interface in swapErrorDialog, exit without one.
  (dcantrell)
- On SuspendError, allow users to skip/format/exit like OldSwapError.
  (dcantrell)
- Raise exception if detected swap volumes are not Linux v1 swap space.
  (dcantrell)
- Handle OldSwapError (#510817) (dcantrell)
- Support a force=True argument on SwapSpace.create() (dcantrell)
- Skip all Makefiles and the liveinst subdirectory in 'make updates'
  (dcantrell)
- Make anaconda know its version number (#520061) (dcantrell)
- Add top back to the stage2 image. (clumens)
- Do not put device node path, but the fs UUID in fstab for mdraid:
  (#519337) (hdegoede)
- Expose common fsset methods and properties in class Storage. (dcantrell)
- Don't display the warning about not enough memory on a VNC install
  (#521109). (clumens)
- The vtoc.h header has moved from the kernel to s390utils (karsten,
  #520830). (clumens)

* Wed Sep 02 2009 David Cantrell <dcantrell@redhat.com> - 12.20-1
- Rename mostlyclean-glade to mostlyclean-liveinst. (dcantrell)
- Handle rootPath referencing a chroot value or actual path (#519665)
  (dcantrell)
- We convert cmdline args to longs in several places, so reduce to a
  function. (clumens)
- Support rootpath overrides in fsset.rootDevice (#519665) (dcantrell)
- Pass anaconda.rootPath to FSSet() (dcantrell)
- Include ui, liveinst, and lang-table strings in po updates (#515411)
  (dcantrell)
- Add some silent make support for sed, mkctype, and other commands.
  (dcantrell)
- Recheck if a partition should be ignored after getting its disk (#518971)
  (hdegoede)
- Fix traceback when editing a pre-existing logical volume (hdegoede)
- Do not traceback on an usb cardreader with no card present (hdegoede)
- Don't identify multi lun usb card readers as multipath (#517603) (hdegoede)
- Device class does not have a format member (hdegoede)
- Device class does not have a path member (hdegoede)
- Simplify language.py to two basic settings, and a lot of support
  (#517569). (clumens)
- clobber is a method of PartedDevice not PartedDisk (hdegoede)
- Remove unused fsFromConfig method (hdegoede)
- allocatePartitions: PartitionCount is a member of PartedDisk not
  DiskDevice (hdegoede)
- New version. (clumens)
- Fix storage/__init__.py:1857: non-keyword arg after keyword arg (hdegoede)
- Remove a bunch of unnecessary semicolons (hdegoede)
- pylint does not like )
- Fix 55:udev_resolve_devspec: Using possibly undefined loop variable 'dev'
  (hdegoede)
- MDRaidArrayDevice.totalDevices is a read only property so don't write it
  (hdegoede)
- storage/__init__.py:471:Storage.exceptionDisks: Undefined variable 'udev'
  (hdegoede)

* Tue Sep 01 2009 Chris Lumens <clumens@redhat.com> - 12.19-1
- NetworkManager changed *again*, use libnm-glib.pc now. (dcantrell)
- Save duplicates from /etc/fstab and don't traceback (#517498). (clumens)
- Update fstab header to reference blkid instead of vol_id. (dlehman)
- Sort fstab entries by mountpoint. (#498354) (dlehman)
- Don't hardcode path to tune2fs. (dlehman)

* Fri Aug 28 2009 David Cantrell <dcantrell@redhat.com> - 12.18-1
- Append s390x packages to PACKAGES list, exclude /sbin/qetharp-2.4
  (dcantrell)
- On kickstart installs, you can't select a different parttype
  (#519137, #520058). (clumens)
- Don't try to create a primary partition if all slots are taken. (#519784)
  (dlehman)
- Fix handling of locked preexisting LUKS devices. (#502310) (dlehman)
- Fix up handling of preexisting partitions. (dlehman)
- Pick up mountpoint set for protected partitions. (#498591) (dlehman)
- Ignore partitions belonging to disks we've reinitialized. (dlehman)
- Handle newly initialized disklabels whether via ks or prompt. (#519235)
  (dlehman)
- Fix some indentation in the disklabel initialization block. (dlehman)
- Use commitToDisk() instead of commit() when only changing flags (hdegoede)
- Update PartitionDevice's partedPartition when the PartedDisks get reset
  (hdegoede)
- Add --localscripts option to buildinstall. (dcantrell)
- Add missing dependencies for linuxrc.s390 and lsznet in mk-images
  (dcantrell)
- Re-enable login of root user in initrd.img (dcantrell)
- Less log clutter with fixing ld64.so.1 symlink in instbin on s390x
  (dcantrell)
- Fix typo in get_dso_deps() for searching /lib on s390x (dcantrell)
- Add hfsplus and netconsole kernel modules (#519756, #519785). (clumens)
- Adapt expandLangs to work with three character base lang names (#517770).
  (clumens)
- Prevent resizes that would go past the end of the disk (#495520)
  (dcantrell)

* Wed Aug 26 2009 Chris Lumens <clumens@redhat.com> - 12.17-1
- dracut has initrd-generic-<version> instead of initrd-<version> (#519185)
  (hdegoede)
- Do not try to commit disks changes to the os while partitions are in use
  (hdegoede)
- disklabel.commit(): DeviceError -> DeviceFormatError (hdegoede)
- A "partition" having no partedPartition shouldn't be a traceback
  (#519128). (clumens)
- Add some debugging code so we know what's going on for #504986 (katzj)
- Fix going back in "Inst. Method" and "Configure TCP/IP" screens in stage 1
  (#515450) (rvykydal)
- Fix going back from stage1 nfs/url setup dialog. (rvykydal)
- When bringing up network in UI, update only ifcfg file of selected device
  (#507084). (rvykydal)
- Update Optional packages button via popup menu too (#515912). (rvykydal)
- Remove the firstadkit-plugin-grub from non-grub archs (msivak)
- Use the path instead of the name for the questionInitialize function.
  (#517926) (jgranado)
- Only add "rhgb quiet" to boot args for non-serial installs (#506508,
  #510523). (clumens)
- On rpm unpack errors, display a fatal error message (#452724). (clumens)
- Use tee thread to ensure line buffered output to screen and log file at
  the same moment... (#506664) (msivak)
- Ensure libraries are copied to initrd.img for xauth (#516369) (maier)
- Import shutil for upgrades (#519011). (clumens)
- Fix focus grabbing on both the password and hostname screens. (clumens)
- x86 and EFI platforms can now have /boot on ext4. (clumens)
- Use the Platform's idea of what filesystem /boot can be on. (clumens)
- zz-liveinst.sh: Restore the #! line (ajax)
- Import _ped so it can be used for _ped.DiskLabelException. (pjones)
- Make sure LV and VG names fit within LVM limits (#517483) (dcantrell)
- Fix updates target to honor KEEP variable correctly. (dcantrell)
- Add support for the reiserfs filesystem (#504401) (dcantrell)
- Update instructions on how to generate source archive. (dcantrell)
- Use disk.description instead of trying to access parted attrs. (#518212)
  (dlehman)
- Fix disk.partedDisk -> disk.format.partedDisk. (dlehman)
- Fix a stupid typo in the logging. (clumens)
- If modifying a repo fails, do not delete it (#516053). (clumens)
- If repo setup fails, also make sure to delete it from yum. (clumens)
- Allow configuring additional NFS repositories, not just the base. (clumens)
- Consolidate "base repo" setup into an extra function. (clumens)
- Allocate memory for login and password and do not meddle with host pointer
  so we can correctly free it (#483818) (msivak)
- Run make in silent mode by default. (jgranado)
- Allow creation of an updates image from a tag offset. (jgranado)

* Tue Aug 18 2009 David Cantrell <dcantrell@redhat.com> - 12.16-1
- correctly deactivate zFCP LUN on s390 (maier)
- correctly activate zFCP LUN on s390 (maier)
- prevent getting started up or shutdown again while already in such state
  (maier)
- Remove unused reipl code in linuxrc.s390 (maier)
- Fix copying of shutdown to initrd.img in mk-images for s390x (#517888)
  (maier)
- 64 bit sparc linux does not define __sparc64__ we need to use
  "(defined(__sparc__) && defined(__arch64__))" fixes building 64 bit sparc
  (dennis)
- make tftp images as small as possible. we have a 10mb hardware limitation
  on there size (dennis)
- make sure we correctly make the sparc tftp image (dennis)
- make sure we have glibc.sparcv9 installed in sparc installers not
  glibc.sparcv9v (dennis)
- add the sparc screen font (dennis)
- add the files for sparc boot config setup configure.ac to define IS_SPARC
  (dennis)
-  add mk-images.sparc script (dennis)
- add support for making sparc images (dennis)
- sparc no longer needs and special keyboard handling.  it uses the standard
  api's interfaces (dennis)
- setup termcap for sparc (dennis)
- Close %%packages with a %%end (#518063) (katzj)
- Call udev_settle from DiskLabel.commit to ensure it happens. (dlehman)
- Fix traceback in text mode upgrade. (#505435) (dlehman)
- Don't traceback if Delete button is hit when no device is selected.
  (dlehman)
- Clean up management of extended partitions we create. (#497293) (dlehman)
- Don't use StorageDevice for partitions w/ biosraid formatting. (#504002)
  (dlehman)
- Don't try to get the size of fstypes w/ no infofsProg defined. (dlehman)
- Change all disklabel manipulations to use the DiskLabel format class.
  (dlehman)
- Create a DiskLabel format class for partition tables. (dlehman)
- Add support for specifying a tag to makeupdates. (dlehman)
- Include changed files from the top level in the updates. (dlehman)
- If asked, put the system SN (as given by dmidecode) into an HTTP header.
  (clumens)
- Add dmidecode to the initrd. (clumens)
- Add the kssendsn parameter and corresponding flag. (clumens)
- Don't keep testing if we're doing URL_METHOD_HTTP. (clumens)
- Later pyparted will define DEVICE_DM, so change the test to use it.
  (clumens)
- Use the new GTK Tooltip API (#517389). (clumens)
- Fix a typo in a kickstart error string (#517760). (clumens)
- Be sure we have a sorted list of mountpoints for live mangling (#504986)
  (katzj)
- Fix askmethod to work with stage= being specified (#516973) (katzj)
- Fix ordering on device list returned from identifyMultipaths() (pjones)
- Fix typo in mpath support. (pjones)

* Wed Aug 12 2009 David Cantrell <dcantrell@redhat.com> - 12.15-1
- Make sure we have the ca cert to handle https repo connections. (517171)
  (jkeating)

* Wed Aug 12 2009 David Cantrell <dcantrell@redhat.com> - 12.14-1
- Correctly inform the user once about obsolete parm/conf file options on
  s390 (maier)
- Handle activation of DASDs in linuxrc.s390 since loader no longer works
  (maier)
- make IPv4 configuration in linuxrc.s390 compatible with NM in loader
  (maier)
- suggest disabled X11-forwarding for ssh login in linuxrc.s390 (maier)
- Fix an erroneous "!" in the test for doKill, and make reboot explicit.
  (pjones)

* Mon Aug 10 2009 David Cantrell <dcantrell@redhat.com> - 12.13-1
- Fix syntax error in identifyMultipaths() (dcantrell)

* Mon Aug 10 2009 David Cantrell <dcantrell@redhat.com> - 12.12-1
- Honor network config boot params for CD-booted ks installs (#433214)
  (dcantrell)
- Include ipcalc command in all initrd.img files, not just s390 (#516084)
  (dcantrell)
- Don't to unmount /mnt/source unless something's mounted there (#516304).
  (clumens)
- Honor nodmraid commandline option (#499733) (hdegoede)
- Don't try to multipath CD devices. (#516362) (pjones)
- booty: Do not strip the trailing p from a devicename like
  mapper/isw_Vol0_tmp (hdegoede)
- booty: isw_Vol0_Stripe is not a disk isw_Vol0_Stri with an e part
  (#505205) (hdegoede)

* Fri Aug 07 2009 Chris Lumens <clumens@redhat.com> - 12.11-1
- upd-instroot: Inspect gtkrc for cursor theme (ajax)
- Support NFS repos in kickstart (#495620, #507093). (clumens)
- upd-instroot: xorg-x11-auth -> xorg-x11-xauth (ajax)
- Check to see if the arch string starts with ppc64. (#516144) (jgranado)
- vtActivate doesn't work on some ppc64 machines, so don't traceback
  (#516206). (clumens)
- Make all sysfs path's be _without_ /sys prefix (#516168) (hdegoede)
- Do not go interactive if timezone in ks is not valid (#473647) (rvykydal)
- Fix going back from "NFS Setup" screen in stage 1 (#507064) (rvykydal)

* Thu Aug 06 2009 David Cantrell <dcantrell@redhat.com> - 12.10-1
- Add missing 'i' in loader/loader.c for non-s390 arches. (dcantrell)

* Thu Aug 06 2009 David Cantrell <dcantrell@redhat.com> - 12.9-1
- Avoid finding the word 'engine' in comments. (jkeating)
- Don't try to get dso deps of statically linked files. (jkeating)
- Call shutDown() correctly for s390 (karsten)
- Remove unused variable from loader/loader.c (karsten)
- Delete unpackaged files on non-livearches. (karsten)
- Do not set parted.PARTITION_BOOTABLE on s390. (root)
- Complete udev setup in linuxrc.s390 for automatic module loading (root)
- Recognize mpath devices when we see them. (pjones)
- Make DiskDevice.partedDisk a property. (pjones)
- Make questionInitializeDisk() somewhat less ugly. (pjones)
- Add a description to DiskDevice, and use it in the UI. (pjones)
- Get rid of Device.description, it is unused. (pjones)
- Close the opened file descriptors when necessary. (#499854) (jgranado)
- Add the glade files to the install image so save-to-bugzilla works
  (#515444). (clumens)
- New system-config-keyboard has a different version then I expected
  (hdegoede)

* Wed Aug 05 2009 Chris Lumens <clumens@redhat.com> - 12.8-1
- Don't try to unmount the CD before we later unmount the CD (#515564).
  (clumens)
- Do not offer going back when ugrade root for ks upgrade is not found
  (#499321) (rvykydal)
- Rebuild .pot file and update translations. (clumens)
- Import the logging stuff (#515564). (clumens)
- Add keyboard kernel cmdline options to grub.conf for dracut (hdegoede)
- Fix backtrace in network.dracutSetupString in the static ip case (hdegoede)
- Write dracut i18n cmdline options to grub.conf (hdegoede)
- Pass InstalltData to booty __init__ as it needs access to many of its
  members (hdegoede)
- Fix ctrl-alt-deleter behavior /before/ end of install. (pjones)
- Merge branch 'master' of ssh://git.fedoraproject.org/git/anaconda (notting)
- No longer use HAL in list-harddrives. (clumens)
- The names of a couple basic udev methods has changed. (clumens)
- Move basic udev methods out of the storage module (#514592). (clumens)
- We do not actually require gtkhtml2 or the python bindings for it.
  (notting)
- Fix some typos in rescue mode (#515091) (msivak)
- Add a dracutSetupString method to network.py (hdegoede)
- Fix backtrace due to iscsi.getNode() not finding the iscsi node (hdegoede)
- Use dracutSetupString() method to add the kernel parameters needed for
  dracut (hdegoede)
- Add a dracutSetupString method to devices.py classes (hdegoede)
- Differentiate between ibft discovered and manually added iscsi disks
  (hdegoede)
- Store iscsi node pointer in iScsiDiskDevice objects (hdegoede)
- When checking logical partition dependcies, make sure the are one the same
  disk (hdegoede)
- Only set iscsi nodes to autostart when none of the LUN's contain /
  (hdegoede)
- Add functions to go from an iScsiDiskDevice to an libiscsi node (hdegoede)

* Fri Jul 31 2009 Chris Lumens <clumens@redhat.com> - 12.7-1
- Fix up udev sillies (related to #514501) (katzj)
- Log when we unmount filesystems so we have a match for mount messages.
  (clumens)
- Let's not exit from buildinstall.functions, say, ever (katzj)
- Rework shutDown() to better accomidate "nokill" better. (pjones)
- Make upgradeany boot option work again (#513227) (rvykydal)
- Update device.map when upgrading (#513393) (rvykydal)
- Catch None devs (katzj)

* Wed Jul 29 2009 Chris Lumens <clumens@redhat.com> - 12.6-1
- Fix CDLABEL substitution in syslinux.cfg for x86 boot.iso (katzj)
- And finish off the removal of rhpl (katzj)
- Use keyboard bits from system-config-keyboard now (katzj)
- Use python-meh instead of our own exception handling now (clumens)
- NM no longer exposes information through HAL (#514501). (clumens)
- Put mkdir into /sbin on the initrd, too. (clumens)
- Make sure controlunits.sh is installed to initrd on s390 (dcantrell)
- Remove ChangeLog (#512502) (dcantrell)
- Add s390utils-cmsfs in upd-instroot for s390 (dcantrell)
- Make sure s390 gets /lib/ld64.so.1 (dcantrell)
- Skip writeDisabledNetInfo() when loader starts on s390 (dcantrell)
- Fix part --onpart= to print the device name instead of the __str__.
  (clumens)
- Just pull in all python modules for stage2 (katzj)
- Trim PACKAGES list in upd-instroot. (dcantrell)
- Update linuxrc.s390 and friends to reflect review comments. (maier)
- Log non-upgradable upgrade candidate roots. (rvykydal)
- unmountFilesystems -> umountFilesystems (#510970). (clumens)
- Disable devel repos on release (#503798) (katzj)
- Work around problems with live installs and dpi other than 96 (#506512)
  (katzj)
- Fix obvious typo in font name (katzj)

* Wed Jul 22 2009 David Cantrell <dcantrell@redhat.com> - 12.5-1
- New build because koji hates me.

* Wed Jul 22 2009 David Cantrell <dcantrell@redhat.com> - 12.4-1
- Add scripts/makeupdates to generate updates.img files. (dcantrell)
- Add python-decorator to the stage2 image for pyparted (#513175). (clumens)
- Set stage2= on x86 boot.iso (katzj)
- Try to auto-find the CD even if stage2= is specified (katzj)
- Make sure we have a device before check if it's protected. (#510033)
  (dlehman)
- Remove unresolvable file devices from the devicetree. (#503830) (dlehman)
- Support multiple fstab entries of a single nodev fstype. (#505969)
  (dlehman)
- Refer to nodev devices as "none", not "nodev". (dlehman)
- Change DeviceTree.devices from a dict to a list. (dlehman)
- Show locked LUKS devices as "Encrypted (LUKS)", not "LUKS". (dlehman)
- Allow creation of four primary partitions on a disk. (#505269) (dlehman)
- Add a bunch more stuff to the initrd needed for networking. (clumens)
- Add more things to /sbin on the initrd that udev requires. (clumens)
- Add dmesg to the images. (clumens)

* Mon Jul 20 2009 David Cantrell <dcantrell@redhat.com> - 12.3-1
- Set GECOS field for new user accounts specific in ks files (dcantrell)
- Show MAC address of network device in text mode too. (rvykydal)
- Fix selection of alternative iface in UI after fail (#507084). (rvykydal)
- Stop the cdrom device before ejecting (#505067) (msivak)
- Add hipersockets to NETTYPE description (bhinson, #511962). (clumens)
- Don't show formatting progress bar after mkfs has exited. (eric_kerin)
- Run firstaidkit-qs script instead of the shell (shows rescue menu)
  (#508512) Add dialog package required for firstaidkit Create /etc/fstab in
  ramdisk to make mount commands easier (#440327) (msivak)
- When ignoring partitions make sure lvm also ignores them (hdegoede)
- 70-anaconda.rules: pass --ignorelockingfailure to lvm invocation (hdegoede)
- Call mdadm -I with --no-degraded for all disks but the last (hdegoede)
- There is no /bin on the initrd so sleep needs to go into /sbin. (clumens)
- Add deviceNameToDiskByPath(). (dcantrell)
- Display drive model and size in MB in partitioning UI (#460697) (dcantrell)
- Lots of small grammar and wording changes. (pjones)
- Edit user-visible dialogs for style. (pjones)
- Get rid of sloppy elipses usage. (pjones)
- Don't write optical devices to /etc/fstab (#505697). (clumens)
- error messages of zFCP on s390: log or pass to the UI (maier)
- correctly delete a SCSI device provided by a zFCP LUN on s390 (maier)
- All other teardown methods take a "recursive" argument (#506166). (clumens)
- Clean yum caches following preupgrade, too (#503096). (clumens)

* Thu Jul 09 2009 David Cantrell <dcantrell@redhat.com> - 12.2-1
- mdmon added to install.img (Jacek.Danecki)
- Remove some unnecessary code. (clumens)
- Use a method yum provides, rather than inventing our own. (clumens)
- Remove _catchallCategory.  yum handles this for us now. (clumens)
- Write out NM_CONTROLLED=no for NICs used for FCoE (hdegoede)
- Add support for biosraid using mdadm (hdegoede)
- Reverse: "Support for MD containers" (hdegoede)
- When all udev_is-foo() checks fail return instead of backtracing (hdegoede)
- 70-anaconda.rules: always import blkid output (hdegoede)
- Make sure to have "self" as an argument. (clumens)
- Add kickstart fcoe command (hdegoede)
- Use the yum preconf object to do $releasever substitution. (clumens)
- Indicate LV status according to lv_attr active bit (#491754) (dcantrell)
- Include lv_attr in lvm.lvs() return value. (dcantrell)
- Fix list of 64-bit arches. (notting)
- We also need -DUSESELINUX if we want to call matchPathContext. (clumens)
- Clean up some arch code. (notting)
- Update /etc/hosts with hostname for loopback IP address (#506384)
  (rvykydal)
- Add missing LAYER2 and PORTNO handling for s390x. (dcantrell)
- Ignore configure.ac when generating updates.img (dcantrell)
- AC_ARG_WITH -> AC_ARG_ENABLE (dcantrell)
- dhclient now reads config files from /etc/dhcp (dcantrell)
- no "rhgb quiet" on s390 to enable visible boot progress and system
  automation (#509881) (maier)
- fix backtrace in s390 reipl support due to missing anaconda.id.fsset
  (#509877) (maier)
- Put sleep in /bin on the initrd (#505639). (clumens)
- Also include the grep programs. (clumens)
- Add programs from vim-minimal, coreutils, and util-linux-ng. (clumens)
- Move programs that aren't s390-specific into the main image. (clumens)
- Look for /bin/sh, not /sbin/busybox. (clumens)
- No longer symlink binaries to busybox. (clumens)
- No longer require busybox. (clumens)

* Mon Jul 06 2009 Chris Lumens <clumens@redhat.com> - 12.1-1
- Include the rest of the libs isys needs to link against (#509572).
  (clumens)
- Add FCoE disks to the devicetree with a type of FcoeDiskDevice (hdegoede)
- Add FcoeDiskDevice class to storage/devices.py (hdegoede)
- Add FCoE support to storage/udev.py (hdegoede)
- Write out configuration of FCoE to installed system (hdegoede)
- Initial FCoE support (hdegoede)

* Thu Jul 02 2009 Chris Lumens <clumens@redhat.com> - 12.0-1
- network --bootproto no longer implies DHCP. (clumens)
- Don't unconditionally skip the network config screen in kickstart. (clumens)
- Allow creating new groups through kickstart. (clumens)
- Set focus on hostname entry in network UI screen (#494135) (rvykydal)
- Fix upgrade selected in UI after storage reset (#503302) (rvykydal)
- Add support for specifying upgrade partition in ks (#471232) (rvykydal)
- Add missing liveinst/* files. (dcantrell)
- Update code that checks for devices that contain install media. (dlehman)
- Rework tracking of devices containing installation media. (#497087) (dlehman)
- Add function storage.udev.udev_resolve_devspec. (dlehman)
- Prevent false positives in devtree's device lookup methods. (dlehman)
- Skip exceptionDisks if exn originated in devtree.populate. (#497240) (dlehman)
- Stop using rhpl.arch in writeRpmPlatform() (katzj)
- Move simpleconfig (back) into anaconda from rhpl (katzj)
- Use iutil arch specifiers rather than rhpl (katzj)
- Remove unused rhpl imports (katzj)
- Switch to using iutil.isS390 instead of rhpl.getArch (katzj)
- Stop using rhpl.translate (katzj)
- Default to /boot on ext4 (katzj)
- Allow /boot on ext4 now that we have a grub that allows it (katzj)
- Make sure the library directory is always set (notting)
- Write out "MAILADDR root" into mdadm.conf (#508321) (rvykydal)
- Do not install grub more times than needed. (rvykydal)
- Ensure we set the SELinux context correctly on symlinks (#505054) (katzj)
- udev dropped vol_id (#506360) (katzj)
- Handle installing multilib into the installer intramfs correctly. (notting)
- Set LIBDIR appropriately on PPC64. (notting)
- Fix grub upgrade (#505966) (rvykydal)
- Include yum.log in anacdump.txt too. (rvykydal)
- Access format options property instead of mountopts attr. (#506219) (dlehman)
- Be more careful about identifying NFS fstab entries. (dlehman)
- Don't add leading directory for files twice. (#503830) (dlehman)
- booty changes for iswmd (Jacek.Danecki)
- Support for MD containers. (Jacek.Danecki)
- New iswmd parameter for kernel cmdline (Jacek.Danecki)
- New udev rule for using mdadm for isw_raid_member (Jacek.Danecki)
- Use isohybrid to make boot.iso a hybrid image (katzj)
- Log yum messages. (rvykydal)
- Tell booty to rescan for bootable drivers when an extra disks get
  added (hdegoede)
- Do not encourage VNC when doing kickstart text installs (#506534) (dcantrell)
- Rename bootstrap to autogen.sh (dcantrell)
- Include the contents of /proc/cmdline in exception reports (katzj)
- Include libwrap library for sshd and telnet in s390 installs (jgranado)
- Enforcing matching rootfs type on LVs as well as for partitions
  (#504743) (katzj)
- Remove problem packages before attempting a re-download (#501887). (clumens)
- Be more explicit about what's lacking on EFI systems (#501341). (clumens)
- If not enough memory is installed, enforce swap partition creation
  (#498742). (clumens)
- Convert to using automake/autoconf. (dcantrell)
- Convert po/ subdirectory to GNU gettext template system. (dcantrell)
- Restructure liveinst/ for the new build system. (dcantrell)
- Add m4/ subdirectory with autoconf macros. (dcantrell)
- Removed py-compile script. (dcantrell)
- Rename anaconda.spec to anaconda.spec.in (dcantrell)
- Ignore autoconf and automake files in the tree. (dcantrell)
- Removed toplevel Makefile and Makefile.inc (dcantrell)
- Show MAC address of network device in combo box (#504216) (dcantrell)
- Remove loader/tr/.cvsignore (dcantrell)
- Increase max NIC identification duration to 5 minutes (#473747). (dcantrell)
- Use /sbin/ipcalc for IP address validation (#460579) (dcantrell)
- Fix an obvious traceback when doing part --ondisk= (#504687). (clumens)
- Catch errors from bootloader installation (#502210). (clumens)
- Remove umask temporarily so device permissions are correct
  (#383531, wmealing).
- Remove the name check on driver disk packages (#472951). (clumens)
- Make the installation key text more descriptive (#474375). (clumens)
- Fix discovery of existing raid/lvm for ks install without clearpart
  (#503310, #503681) (rvykydal)
- Use the F12 version of the bootloader command. (clumens)
- It's /sbin/fsadm, not /sbin/e2fsadm (#504043). (clumens)
- Remove the bootloader --lba32 option. (clumens)
- Use gettext.ldngettext when necessary (#467603) (dcantrell)
- Test NM_CONTROLLED setting correctly in network.py (#502466) (dcantrell)
- Show unknown partitions as "Unknown" in partition editor. (dcantrell)
- Add a type hint on popup windows (rstrode). (clumens)
- Use the F12 version of the driverdisk command. (clumens)
- Remove driverdisk --type, since mount can figure that out. (clumens)
- Fix an error when editing an unreachable repo (#503454). (clumens)
- If /etc/rpm/platform is found, move it out of the way. (clumens)
- We no longer write out /etc/rpm/platform, so don't offer to upgrade
  it. (clumens)
- Remove locals containing "passphrase" or "password" from exns
  (#503442). (clumens)
- Make progress bars modal (#493263, #498553, rstrode). (clumens)
- Make sure to import os.path if we are going to use it. (jgranado)
- ipcalc is copied to /usr/lib. (jgranado)
- Limit the trigger to block type devices. (jgranado)
- We need ipcalc for new s390 installation script. (jgranado)
- Fix off-by-one errors in read. (notting)
- sysconfig file changed names for system-config-firewall (katzj)
- Don't write out firewall settings if they already exist (#502479) (katzj)
- Make sure that the devices are correctly detected (#491700) (jgranado)
- Make the save-to-bugzilla dupe detection smarter. (clumens)
- If network --device=MAC is given, translate to device name
  (#185522). (clumens)
- Add a function to convert MAC addresses to device names. (clumens)
- Move /boot checks from sanityCheck into Platform.checkBootRequest. (clumens)
- Return translated strings from checkBootRequest. (clumens)
- Check that /boot is on a Mac disk label for PPC installs (#497745). (clumens)
- Call checkBootRequest from sanityCheck. (clumens)
- Put some space in that big scary warning. (clumens)
- fond -> found (clumens)
- Use powers of two in swapSuggestion (#463885). (clumens)
- Trim "mapper/" off device names in the bootloader UI (#501057). (clumens)
- Make the weak password dialog comply with the HIG (#487435). (clumens)
- Add a newline to a cmdline mode string (#497575). (clumens)
