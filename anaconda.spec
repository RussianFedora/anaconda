%define livearches %{ix86} x86_64 ppc ppc64

Summary: Graphical system installer
Name:    anaconda
Version: 20.25.2
Release: 1%{?dist}
License: GPLv2+
Group:   Applications/System
URL:     http://fedoraproject.org/wiki/Anaconda

# To generate Source0 do:
# git clone http://git.fedorahosted.org/git/anaconda.git
# git checkout -b archive-branch anaconda-%%{version}-%%{release}
# ./autogen.sh
# make dist
Source0: %{name}-%{version}.tar.bz2

# Change product names in installclasses
Patch0: anaconda-19.22-rfremixify.patch
# Change profuct name on GNOME Try window
Patch1: anaconda-18.24-fix-hardcoded-product-name.patch
# We use fedora repos, so we must use fedora name
Patch2: anaconda-20.25.2-hardcode-repo.patch
# Read name from rfremix-release
Patch3: anaconda-19.19-read-from-rfremix-release.patch
# Run liveinst in english
Patch4: anaconda-19.28-start-liveinst-always-in-english.patch

# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).
%define gettextver 0.18.1
%define gconfversion 2.28.1
%define intltoolver 0.31.2-3
%define libnlver 1.0
%define pykickstartver 1.99.42
%define yumver 3.4.3-91
%define partedver 1.8.1
%define pypartedver 2.5-2
%define pythonpyblockver 0.45
%define nmver 1:0.7.1-3.git20090414
%define dbusver 1.2.3
%define yumutilsver 1.1.11-3
%define mehver 0.23-1
%define sckeyboardver 1.3.1
%define firewalldver 0.3.5-1
%define pythonurlgrabberver 3.9.1-5
%define utillinuxver 2.15.1
%define dracutver 034-7
%define isomd5sum 1.0.10
%define fcoeutilsver 1.0.12-3.20100323git
%define iscsiver 6.2.0.870-3
%define rpmver 4.10.0
%define libarchivever 3.0.4
%define langtablever 0.0.7-1

BuildRequires: audit-libs-devel
BuildRequires: gettext >= %{gettextver}
BuildRequires: gtk3-devel
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel
BuildRequires: glade-devel
BuildRequires: pygobject3
BuildRequires: intltool >= %{intltoolver}
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libXxf86misc-devel
BuildRequires: libgnomekbd-devel
BuildRequires: libnl-devel >= %{libnlver}
BuildRequires: libxklavier-devel
BuildRequires: pango-devel
BuildRequires: pykickstart >= %{pykickstartver}
%if ! 0%{?rhel}
BuildRequires: python-bugzilla
%endif
BuildRequires: python-devel
BuildRequires: python-urlgrabber >= %{pythonurlgrabberver}
BuildRequires: python-nose
BuildRequires: systemd
BuildRequires: yum >= %{yumver}
BuildRequires: NetworkManager-devel >= %{nmver}
BuildRequires: NetworkManager-glib-devel >= %{nmver}
BuildRequires: dbus-devel >= %{dbusver}
BuildRequires: dbus-python
BuildRequires: rpm-devel >= %{rpmver}
BuildRequires: libarchive-devel >= %{libarchivever}
%ifarch %livearches
BuildRequires: desktop-file-utils
%endif
%ifarch s390 s390x
BuildRequires: s390utils-devel
%endif

Requires: anaconda-widgets = %{version}-%{release}
Requires: dnf
Requires: python-blivet >= 0.23.1
Requires: gnome-icon-theme-symbolic
Requires: python-meh >= %{mehver}
Requires: libreport-anaconda >= 2.0.21-1
Requires: libselinux-python
Requires: rpm-python >= %{rpmpythonver}
Requires: parted >= %{partedver}
Requires: pyparted >= %{pypartedver}
Requires: yum >= %{yumver}
Requires: python-urlgrabber >= %{pythonurlgrabberver}
Requires: system-logos
Requires: pykickstart >= %{pykickstartver}
Requires: langtable-data >= %{langtablever}
Requires: langtable-python >= %{langtablever}
Requires: libuser-python
Requires: authconfig
Requires: firewalld >= %{firewalldver}
Requires: util-linux >= %{utillinuxver}
Requires: dbus-python
Requires: python-pwquality
Requires: python-IPy
Requires: python-nss
Requires: tigervnc-server-minimal
Requires: pytz
Requires: libxklavier
Requires: libgnomekbd
Requires: realmd
%ifarch %livearches
Requires: usermode
Requires: zenity
%endif
Requires: GConf2 >= %{gconfversion}
%ifarch s390 s390x
Requires: openssh
%endif
Requires: isomd5sum >= %{isomd5sum}
Requires: yum-utils >= %{yumutilsver}
Requires: NetworkManager >= %{nmver}
Requires: nm-connection-editor
Requires: dhclient
Requires: anaconda-yum-plugins
Requires: libselinux-python >= %{libselinuxver}
Requires: kbd
Requires: chrony
Requires: python-ntplib
Requires: rsync
%ifarch %{ix86} x86_64
Requires: fcoe-utils >= %{fcoeutilsver}
%endif
Requires: iscsi-initiator-utils >= %{iscsiver}
%ifarch %{ix86} x86_64 ia64
Requires: dmidecode
%if ! 0%{?rhel}
Requires: hfsplus-tools
%endif
%endif
Obsoletes: anaconda-images <= 10
Provides: anaconda-images = %{version}-%{release}
Obsoletes: anaconda-runtime < %{version}-%{release}
Provides: anaconda-runtime = %{version}-%{release}
Obsoletes: booty <= 0.107-1

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
Requires: dracut >= %{dracutver}
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
%patch2 -p1
%patch3 -p1
#%patch4 -p1

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
%{make_install}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}

%ifarch %livearches
desktop-file-install ---dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop
%else
%{__rm} -rf %{buildroot}%{_bindir}/liveinst %{buildroot}%{_sbindir}/liveinst
%endif

%find_lang %{name}


%ifarch %livearches
%post
update-desktop-database &> /dev/null || :
%endif

%ifarch %livearches
%postun
update-desktop-database &> /dev/null || :
%endif

%files -f %{name}.lang
%doc COPYING
%doc docs/command-line.txt
%doc docs/install-methods.txt
%doc docs/mediacheck.txt
%{_unitdir}/*
%{_prefix}/lib/systemd/system-generators/*
%{_bindir}/instperf
%{_sbindir}/anaconda
%{_sbindir}/handle-sshpw
%{_datadir}/anaconda
%{_prefix}/libexec/anaconda
%{_libdir}/python*/site-packages/pyanaconda/*
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
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
%{_prefix}/libexec/anaconda/dd_*

%changelog
* Tue Oct 22 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 20.25.2-1.R
- apply all RFRemix patches and hacks from RFRemix 19

* Mon Oct 21 2013 Brian C. Lane <bcl@redhat.com> - 20.25.2-1
- Adds additional debug logging to yumpayload.py. (amulhern)
- Handle invalid JSON in geoloc (#1021410) (dshea)
- Revert "Only prompt for LUKS password if the user has chosen to configure
  automatically." (amulhern)
- Reset checks on both password fields. (#1020580) (dshea)
- Fix swaps added to fstab for noformat (gene)
- Don't update hub's continue button and label for every spoke (#1020373)
  (vpodzime)
- BootLoaderError should not reset storage (#1019541) (bcl)
- Only prompt for LUKS password if the user has chosen to configure
  automatically. (amulhern)
- network gui spoke: use GDBus to obtain list of settings (#1018467) (rvykydal)
- Fix liveinst to work with livemedia-creator (#1009711) (bcl)

* Wed Oct 16 2013 Brian C. Lane <bcl@redhat.com> - 20.25.1-1
- New transifex branch for f20 (bcl)
- Fix python-blivet buildrequires for new f20-branch version. (dlehman)
- Save mountpoints specified for existing btrfs volumes. (#892747) (dlehman)
- BTRFS cannot hold swap, no need to care about fstab swaps (vpodzime)
- Fix the alignment of the Network Time switch (#1019301) (dshea)
- Tell blivet which swaps should appear in the fstab (#1011391) (vpodzime)
- Put only newly created or reformated swaps to the new root (vpodzime)
- Make code to get new devices reusable as property (vpodzime)
- Grab journal only from the last boot (vpodzime)
- DNFPayload: allow enable/disable calls for repos that do not exist. (ales)
- network: look for device settings also based on DEVICE value (#1017788)
  (rvykydal)
- Add shell spoke to s390x installations (vpodzime)
- Put TUI spokes in common categories (vpodzime)
- MountpointSelector is a widget, set its property properly (#1013612)
  (vpodzime)
- Include the journal log on installed system (bcl)
- DNFPayload: error handling and logging cleanups. (ales)
- DNFPayload: reset the transaction goal on new package selection check. (ales)
- DNFPayload: implement environmentGroups() (ales)
- Some partition scheme is always selected (#1017435) (vpodzime)

* Fri Oct 11 2013 Brian C. Lane <bcl@redhat.com> - 20.25-1
- Don't use g_object_set on initialized objects. (dshea)
- Remove the "other" tab in the network spoke. (dshea)
- Fix duplicated id in custom.glade (dshea)
- Correctly generate rescue initrd (#1013087) (bcl)
- Refresh swap suggestion once we know which disks to use (vpodzime)
- Initialize the kickstart install method (#1017614) (dshea)
- Use correct format for raise in kickstart.py (bcl)
- Add install-requires target to the Anaconda makefile (mkolman)
- fix luksformat references (#1014493) (bcl)
- kickstart: check for correct format (#1014545) (bcl)
- Add checks for unexpanded macros. (dshea)
- UIScreen doesn't necessarily have the ready property (vpodzime)
- Print long widgets in a nice way (vpodzime)
- Consider errno 5 I/O errors hardware faults (vpodzime)
- Install kernel-lpae if supported (#1013015) (vpodzime)
- Bump firewalld version (mkolman)

* Wed Oct 09 2013 Brian C. Lane <bcl@redhat.com> - 20.24-1
- Clear bootDisk and bootloader stage info on errors (#1013482) (bcl)
- Catch BootLoaderError when setting up bootloader (#1013474) (bcl)
- Fix an incorrect formatting string in makeupdates. (clumens)
- network: remove function we don't need anymore (rvykydal)
- Don't translate constant strings. (dshea)
- Take into account disk space when calculating swap suggestion (#1016673)
  (vpodzime)
- DNFPayload: adapt to DNF change c3de85d6 of Base.install() error reporting.
  (ales)
- DNFPayload: the new libcomps makes env.option_ids a list of GroupID objects.
  (ales)
- Fix warning message when package version is not found in Koji (mkolman)

* Tue Oct 08 2013 Brian C. Lane <bcl@redhat.com> - 20.23-1
- Use Unicode in the TUI buffer strings (#1015620) (dshea)
- DNFPayload: install DNF itself. (ales)
- DNFPayload: direct conf.persistdir to the sysimage. (ales)
- Add a tooltip to the container combobox (#975801) (bcl)
- Use different colors for different message types. (dshea)
- Exit on exception in the askVNC spoke (#962804) (dshea)
- Don't skip the strength check if overriding a kickstart password (dshea)
- Allow password spoke to be exited without password (#1004931) (dshea)
- Re-check the password strength when the username changes (dshea)
- Only call pwquality once per password. (dshea)
- Use GUICheck checks for the root password strength (dshea)
- Use constants for password check failure messages (dshea)
- Use a constant to indicate GUICheck success (dshea)
- Remove a redundant error property from UserSpoke (dshea)
- Fix the usages of PWQError. (#1014405) (dshea)
- Fix usage of GtkLevelBar in glade. (dshea)
- Clean up callbacks in the user spoke. (dshea)
- Removed an untrue portion of a doc comment (dshea)
- Support for removing services from firewall needs newer PyKickstart (mkolman)
- Add support for removing services from the firewall (#957809) (mkolman)

* Fri Oct 04 2013 Brian C. Lane <bcl@redhat.com> - 20.22-1
- Only encrypt the TUI user password once (#1015220) (dshea)
- Don't try to collect removed modules (vpodzime)
- Moved the NFS nolock option into Payload._setupNFS (dshea)
- Grab journalctl logs if there is no /tmp/syslog (vpodzime)
- Pass layout and variant in specific format to Gkbd (#1011155) (vpodzime)
- Translate the "Quit" string at the end of liveinst. (dshea)

* Fri Sep 27 2013 Brian C. Lane <bcl@redhat.com> - 20.21-1
- Remove another reference to log_picker. (clumens)
- Turn spinner back on for configuration (bcl)
- Use assertIsInstance in the kickstart version test. (clumens)
- If the full device path is given in repo=hd:, still select it in the UI
  (#980479). (clumens)
- Display newly created partitions without a mountpoint, too (#886039).
  (clumens)
- Don't require pressing escape twice to kill the media check window (#965625).
  (clumens)
- Fix display of weak password warning (#1011850) (dshea)
- Fix the tui simpleline imports. (dshea)
- Don't confuse users by misleading tooltip (#1011112) (vpodzime)
- Assorted other pylint fixes for scripts and utils (dshea)
- Pass string format arguments as paramters to logging (dshea)
- Ignore the use of func_globals in a test case (dshea)
- Fix issues in the AnacondaWidgets python wrapper (dshea)
- Make exception handling more specific (dshea)
- Remove unused imports and variables (dshea)
- Remove unnecessary lambdas (dshea)
- Remove obsolete files. (dshea)
- Check whether the commit matches the tree (dshea)
- Run pylint on all python files (dshea)
- Don't use relative imports (dshea)
- Use g_signal_handler_disconnect instead of g_object_disconnect (#1010486)
  (vpodzime)
- Fixup Eula class (bcl)
- Allow searching for keyboard layouts in English (#1009806) (vpodzime)
- network: don't create ksdata for devices enslaved in GUI (#1011826)
  (rvykydal)
- Allow a proxy to be set before the method is saved (#1012096) (dshea)
- Export the pykickstart Eula command (vpodzime)

* Wed Sep 25 2013 Brian C. Lane <bcl@redhat.com> - 20.20-1
- Encrypt normal user passwords when doing text install. (#977732)
  (sbueno+anaconda)
- Escape the status before setting it as markup (vpodzime)
- network gui: do not crash on devices without settings (eg wireless)
  (#1010519) (rvykydal)
- Make the keyboard layout preview dialog bigger (#1011140) (vpodzime)
- Return switching options with the same order as shown (#1011130) (vpodzime)
- Use a temporary directory for verifying ISO media (dshea)
- Skip devices not controllable by blivet (#1009809) (dshea)
- Add translation support to check_accelerators (dshea)
- Make sure autopart type is handled deterministicaly in text mode (#1010453)
  (vpodzime)
- Don't rely on X server adding empty variant for its defaults (#1011658)
  (vpodzime)
- Make Keyboard spoke's status consistent with other statuses (#1011166)
  (vpodzime)
- LiveImageKSPayload skip the parent class setup method (#1010500) (bcl)
- Pass the actual format instead of Python built-in (#1009678) (vpodzime)
- Don't allow using updates with non-default network sources (#1008028)
  (vpodzime)
- Use Sphinx documentation format in nm.py. (rvykydal)
- Changed the keyboard accelerator for iscsi "Retry Log In" (dshea)
- Only fail on a missing firewalld command if the firewall is enabled
  (#1004976). (clumens)
- Cleanup some pylint failures in the network module (bcl)
- Add GtkNotebook support to the accelerators check. (dshea)

* Fri Sep 20 2013 Brian C. Lane <bcl@redhat.com> - 20.19-1
- tui ErrorDialog needs to be modal (#983316) (bcl)
- Keyboard variant names may contain dashes (#1008730) (vpodzime)
- Forbid "root" as a user or group name. (#968451) (dshea)
- Set the password strength color based on strength (#965596) (dshea)
- Fix the password confirmation match check (#1009907) (dshea)
- Replace removed python modules with stubs in makeupdates (vpodzime)
- Unlock encrypted partitions before finding installations (#901917) (vpodzime)
- Network TUI: remove unused import, import nm. (rvykydal)
- Network TUI: show the same status as in gui. (rvykydal)
- Network TUI: don't traceback when applying config to device without link.
  (rvykydal)
- Generate ifcfg VLAN_ID value for kickstart network --vlanid. (rvykydal)
- Network TUI: fix updating of ksdata in apply. (rvykydal)
- Network TUI: ignore slaves devices for configuration. (rvykydal)
- Clean up ifcfg file handling. (rvykydal)
- Check the validity of generated usernames in TUI (#965543) (dshea)
- Behave better when PYTHONPATH is already set (dshea)
- Decode keyboard layout descriptions as UTF-8 (#1009278) (dshea)
- Filter out devices with no media from custom (#960794) (bcl)

* Wed Sep 18 2013 Brian C. Lane <bcl@redhat.com> - 20.18-1
- ProgressHub no longer exists in pyanaconda/ui/tui/hubs. (clumens)
- Search all disk types for install media (#1004726) (dshea)
- git commit check for ack flag on rhel branches (bcl)
- Fix Lightbox for compositing window managers (#1008446) (dshea)
- Add metalink support to yumpayload (bcl)
- Make progress screen in text mode standalone spoke instead of hub (vpodzime)
- Render the right arrow based on the widget direction (#1008397) (vpodzime)
- Mirror the GUI if an RTL language is chosen (#1008397) (vpodzime)
- Removed unused GUI elements (dshea)
- Clean up what is and isn't translatable and how. (dshea)
- Removed the exceptionsText constant (dshea)
- Add comments for translators to TUI input strings (#854226) (dshea)
- Use python-format on all intltool-extract strings (dshea)

* Mon Sep 16 2013 Brian C. Lane <bcl@redhat.com> - 20.17-1
- Fix handling of blank size specs in the custom spoke. (#1004903) (dlehman)
- Block resize slider value changed handler when setting range. (#1007387)
  (dlehman)
- Remove an unused import. (clumens)
- Create the XklWrapper singleton in background (vpodzime)
- Translate layout and switching options descriptions on the fly (vpodzime)
- Improve XklWrapper's API (vpodzime)
- Move upcase_first_letter function to iutil (vpodzime)
- Remove the Layout class and things we don't need in XklWrapper (vpodzime)
- Ignore the whole m4 directory (vpodzime)
- Do not schedule hubs with no spokes available (#1006357) (vpodzime)
- Retranslate language filtering placeholder texts (#1007090) (vpodzime)
- Use pigz to create updates.img (vpodzime)
- The Desktop class doesn't need to inherit from SimpleConfigFile. (clumens)
- Fix yet another pylint error caught after the fact. (clumens)
- Move all languages found by geoip to the top in Welcome spoke (mkolman)
- Don't set ksdata.lang.seen to True if using default value (mkolman)
- DNFPayload: reset the sack and repos on updateBaseRepo() (ales)
- refactor: YumPayload: selectKernelPackage()->_select_kernel_package() (ales)
- DNFPayload: mirrorlist can not be an empty string. (ales)
- DNFPayload: display the download step in progressQ. (ales)
- DNFPayload: logging the missed packages/groups. (ales)
- DNFPayload: select kernel packages. (ales)
- DNFPayload: log when the transaction process unexpectedly terminates. (ales)
- DNFpayload: disable all NSS operations in RPM. (ales)
- DNFPayload: keyerror in isRepoEnabled() (ales)
- DNFPayload: implement selectEnvironment() (ales)

* Fri Sep 13 2013 Brian C. Lane <bcl@redhat.com> - 20.16-1
- add pre-commit hook to run pylint (bcl)
- Allow runpylint.sh to be passed files (bcl)
- handle case of no ifcfg and no hostname (#1002737) (bcl)
- Allow make targets to be run outside of $srcdir (dshea)
- Fix the wildcard usage in automake files. (dshea)
- Move the intltool Makefile rules into configure.ac (dshea)
- Fix a format parameter mapping (#1007472) (dshea)
- Check whether keyboard translations are stale (#972236) (dshea)
- Fix the handling of xklavier strings. (dshea)
- Center the Langsupport spoke's description (vpodzime)
- Set minimal width request for the locales box (vpodzime)
- Use constant for default keyboard layout (vpodzime)
- Try to use VConsole keymap name as X layout (#1007359) (vpodzime)
- Retranslate also layout indicator when retranslating BaseWindow (#1007087)
  (vpodzime)
- Check ready state before baseRepo (#1007448) (bcl)
- Fix po/Rules-extract so it doesn't remove itself (dshea)
- Include LayoutIndicator and TimezoneMap to the Micsellaneous Widgets
  (vpodzime)

* Wed Sep 11 2013 Brian C. Lane <bcl@redhat.com> - 20.15-1
- Don't set up the resize slider for non-resizable devices. (#997690) (dlehman)
- Remove 'completed' property from Autopart spoke in text UI. (sbueno+anaconda)
- Clean up code for input handling in TUI spokes. (sbueno+anaconda)
- set_hostname should proceed only on DVD and live installations (vpodzime)
- Don't use temporary file and move when writing out an ifcfg file (vpodzime)
- Set hostname when leaving network spokes (vpodzime)
- Keep file-naming convention with the Lightbox widget (vpodzime)
- Let users configure autopart options in interactive text ks. (#1001061)
  (sbueno+anaconda)
- Add parameters to format strings (dshea)
- Fix pre-processing of files for xgettext (#1005644) (dshea)
- Added a test to check for xgettext warnings (dshea)
- Make sure XklWrapper isn't dumped to the anaconda-tb file (vpodzime)
- Catch race of network device state vs reading its config properties (#980576)
  (rvykydal)

* Tue Sep 10 2013 Brian C. Lane <bcl@redhat.com> - 20.14-1
- Convert the lightbox into a GObject (#1000927) (dshea)
- Remove some more unused imports. (clumens)
- Move the Anaconda class to a proper module (vpodzime)
- Firstboot should be disabled by default after automated installations
  (vpodzime)
- Fix typo introduced in refactorization (#1005511) (vpodzime)
- Remove unused imports in the network spoke. (clumens)
- Get rid of the now-unused new_firmware variable. (clumens)
- Remove magic from the passphrase dialog (#921948) (vpodzime)
- Don't pass extra arguments to LangLocaleHandler.__init__() (vpodzime)
- Fix check for device state when reading its IPXConfig (#1001776, # 1005198)
  (rvykydal)

* Mon Sep 09 2013 Brian C. Lane <bcl@redhat.com> - 20.13-1
- Fix handling of flexible specs in onpart for member devices. (#1004885)
  (dlehman)
- Always regenerate initramfs (#994180) (bcl)
- Avoid the use of NamedTuple._make (dshea)
- Add superclass __init__()s and fix an indent (dshea)
- Pass logging string format variables as parameters (dshea)
- Remove unnecessary variables, imports, semicolons (dshea)
- Fix the user/group name regex (dshea)
- Fix problems with the test scripts (dshea)
- Handle kickstarts that don't specify timezone (#1001598) (mkolman)
- Don't set "date of last password change" /etc/shadow field (#985572)
  (hdegoede)

* Fri Sep 06 2013 Brian C. Lane <bcl@redhat.com> - 20.12-1
- Cleanup arch tests (dshea)
- Rearranged the automake tests. (dshea)
- Update po/ build files to the current gettext (dshea)
- Use libtool with gtkdoc-scanobj (dshea)
- Use autoconf to set the spec file Version. (dshea)
- Use the ustar format with make dist (dshea)
- Fix widgets autotools generation. (dshea)
- Require gtk-doc and GObject. (dshea)
- dracut no longer auto assembles everything (#960496) (bcl)
- Only ignore missing packages entries (#983316) (bcl)
- Fix a string that was modified before translation (#1004960) (dshea)
- Let users configure keyboard via anaconda in live installations (#1002533)
  (vpodzime)
- Use copy instead of move for NTP configuration (#985566) (hdegoede)
- Share code between the Welcome and Langsupport spokes (vpodzime)
- Do not try to set None as hostname (#1002737) (vpodzime)
- Fix crash on LiveCD if network is configured before installing (#1002373)
  (rvykydal)

* Thu Sep 05 2013 Brian C. Lane <bcl@redhat.com> - 20.11-1
- Add more details to iso device selector (#971290) (bcl)
- Warn user if they enter a weak password in TUI. (#1001039) (sbueno+anaconda)
- Don't mark spoke as completed if no repo is set. (#1001538) (sbueno+anaconda)
- Don't enable chronyd if disabled in kickstart (#1002583) (mkolman)
- Run firstboot-only spokes on first boot by default (vpodzime)
- Let hubs specify which environments they support (vpodzime)
- Don't mount cdroms that contain no mountable media. (#1000889) (dlehman)
- Don't try to parse langcode if none given (vpodzime)
- Get rid of the non-deterministic expand_langs and its usage (vpodzime)
- Rework the Langsupport spoke to work with all locales (vpodzime)
- Rework the Welcome spoke to allow users choose from all locales (vpodzime)
- Improve import in GUI utils a bit (vpodzime)
- Remove the cryptic "language-default keyboard" checkbutton (vpodzime)
- Allow seting up locale without modifying ksdata (vpodzime)
- Remove an unused argument of get_available_translations (vpodzime)
- Setup language early to a value we can figure out (vpodzime)

* Tue Sep 03 2013 Brian C. Lane <bcl@redhat.com> - 20.10-1
- Optionally hide the GUI option to install updates (dshea)
- Move the really_hide and really_show functions to utils (vpodzime)
- Search for all translations, not only one per langauge (#1001446) (vpodzime)
- Use the DEFAULT_LANG if GeoIP suggestion cannot be used (#1000715) (vpodzime)
- Network spoke: fix showing of ipv6 addresses (rvykydal)
- Use the sensitive-info log for sensitive location info (#986844) (mkolman)
- Add new logger for sensitive information (mkolman)
- Handle %%define changes for autofetch (mkolman)
- Update dumping of network info for new nmcli interface. (rvykydal)
- Text network spoke: more strict ipv6 address input checking (#909299)
  (rvykydal)
- Network spoke: show global ipv6 addresses (rvykydal)
- Text network spoke: add to translated files (po/POTFILES.in) (#902299)
  (rvykydal)
- Text network spoke: require netmask and gateway for static ipv4 (#902299)
  (rvykydal)
- Text network spoke: Condense device configuration information (#902299)
  (rvykydal)
- Text network spoke: fix ipv4 regex (#909299) (rvykydal)
- Resolved accelerator conflicts and marked excpetions. (dshea)
- Added tests for duplicated keyboard accelerators (dshea)
- Implement group creation with GID in GUI (#968085) (dshea)
- Remove unused imports. (dshea)
- Move dynamic labels out of custom.glade (#1000703) (dshea)

* Mon Aug 26 2013 Brian C. Lane <bcl@redhat.com> - 20.9-1
- Text network spoke: basic configuration support (#909299) (rvykydal)
- Add support for network configuration in TUI. (#909299) (sbueno+anaconda)
- Remove partial matches from Koji search results (mkolman)
- Handle >=,<=,= for package version, fix -a/--add (mkolman)
- Return only network devices supported in installer from nm_devices (#999514)
  (rvykydal)
- Obtain network device type specific dbus interface dynamically (#999514)
  (rvykydal)
- Catch no-hwaddr exception only for the respective call (#999514) (rvykydal)
- Don't catch hwaddr not found exception for ethernet devices (#999514)
  (rvykydal)
- Added a validation test for the GUI group list (dshea)
- Validate input fields on the user spoke. (#967245) (dshea)
- Added an input validation framework. (dshea)
- Pre-fetch widgets in advanced user dialog (dshea)
- Change validatePassword to be more flexible. (dshea)
- Moved regexes into regexes.py. (dshea)

* Fri Aug 23 2013 Brian C. Lane <bcl@redhat.com> - 20.8-1
- Fix a SIGSEGV when returning from storage spoke (#983319) (dshea)
- makebumpver: Fix problem with single line body (bcl)
- For now, ignore checking dnfpayload.py with pylint. (clumens)
- Don't do str() on an exception we're passing into a string substitution.
  (clumens)
- Check for hwaddress exceptions. (dshea)
- If LANG isn't set, set it to default value. (#997397) (sbueno+anaconda)
- Remove yet another unused import. (clumens)
- swap devices should be under the System portion (#962668). (clumens)
- Populate the repo store before changed can ever be called (#994940).
  (clumens)
- Make the ISO choosing widget wider (#973376). (clumens)
- Don't recommend /usr as a separate mount point anymore (#981465). (clumens)
- Do not run another instance of the TUI for errors (#997661) (vpodzime)
- Do not try to exit from the installation thread (vpodzime)
- Tell which thread failed to be added by the ThreadMgr (vpodzime)

* Wed Aug 21 2013 Brian C. Lane <bcl@redhat.com> - 20.7-1
- Modify the gtk_warning function in anaconda to use gtk3. (clumens)
- Fix some pylint warnings in the new DNF code. (clumens)
- Fix a couple more pykickstart handler version mismatches. (clumens)
- anaconda requires a later version of partitioning syntax now. (clumens)
- packaging: add dnf to the Anaconda's requires. (ales)
- Enable DNFPayload on specific triggers. (ales)
- DNFPayload: initial version. (ales)
- refactor: tear down the install device in PackagePayload.reset(). (ales)
- refactor: extract the device handling in YumPayload._configureBaseRepo up to
  PackagePayload. (ales)
- refactor: move YumPayload._setUpMedia() up to PackagePayload._setupMedia().
  (ales)
- Tweaks in the Payload interface. (ales)
- remove: configureAddOnRepo from the Payload interface. (ales)
- Payload: forgotten comment in spaceRequired() (ales)
- Payload: define txID to None. (ales)
- The NFS text dialog should never attempt to use method.url (#998446).
  (clumens)
- Remove the unittest target, since "make check" will do this for us. (clumens)
- Use the latest version of the RAID kickstart handler. (clumens)
- Update both the method and repo info. (dshea)
- remove the UBOOT class arm systems are now using EXTLINUX (dennis)
- ARM: switch to using extlinux by default (dennis)
- Update our pylint arguments. (clumens)
- Don't implicitly unpack exceptions.  That won't be supporetd in the future.
  (clumens)
- Modify how we call logging functions to take a list of parameters. (clumens)
- Use "raise Exception()" instead of "raise Exception, ..." (clumens)
- Hook up pylint and our nosetests to be run via "make check". (clumens)
- Drop unneeded required_space_text variable. (#997690) (dlehman)
- Specify also query script when getting locale's native name (vpodzime)
- Update runpylint.sh for pylint 1.0.0 (bcl)
- Clean up translation placeholders (#890157) (bcl)
- Don't override multilib setting unless the option was passed. (#987557)
  (dlehman)
- Set the encoding of custom.py to utf-8 (dshea)
- Report if a package was not found in Koji during autofetch (mkolman)
- Convert makeupdates from getopt to argparse (mkolman)
- Fixed the interpretation of RAID levels (dshea)
- Consolidate get_object() calls. (dshea)
- Add ASCII-only upper and lower string functions. (dshea)
- Fix the User/Group already exists log messages. (dshea)
- Normalize keyboard layout and variant strings from langtable (vpodzime)
- A few tests for the keyboard layout and variant strings processing (vpodzime)
- More robust parsing of the layout and variant string specification (vpodzime)
- Move DEFAULT_VC_FONT to constants (vpodzime)
- Match langs with stripped accents when filtering languages (vpodzime)
- Fix the User subclass using an old version of the pykickstart superclass.
  (clumens)
- Bring the kickstart version test back to life. (clumens)
- Don't read proxy for methods that have no proxy (dshea)

* Wed Aug 14 2013 Brian C. Lane <bcl@redhat.com> - 20.6-1
- Import DBusGMainLoop directly (bcl)
- Catch AttributeError when looking for InstallClass (bcl)
- dracut/parse-kickstart should use the updated method-related classes
  (#994978). (clumens)
- Ignore warnings about the global keyword and the DefaultInstall class.
  (clumens)
- Fix all the pylint warnings in the anaconda file. (clumens)
- Deal with the last of the catching Exception warnings. (clumens)
- Always define a continueButton and quitButton property. (clumens)
- Fix pylint warnings in the installclasses. (clumens)
- Remove a directory that does not exist from the PYTHONPATH for pylint.
  (clumens)
- Fix up some warnings about calling the superclass's __init__ method.
  (clumens)
- Remove the reference to "anaconda" in reIPL. (clumens)
- Fix up almost all of the redefining warning messages. (clumens)
- Add a bunch of gobject-introspection related ignore lines. (clumens)
- StorageChecker ought to have a self.storage attribute. (clumens)
- Ignore another error pylint can't quite figure out. (clumens)
- pylint doesn't understand what's in AnacondaKSHandler. (clumens)
- Remove the "Add custom add-on" button. (clumens)
- Fix up places where overridden methods don't take the same number of args.
  (clumens)
- Fix up all unused variable warnings. (clumens)
- Added files to MAINTAINERCLEANFILES (dshea)
- Reenabled the pylint test target (dshea)
- Cleanup the autogen scripts. (dshea)
- Remove m4 files from the widgets project. (dshea)
- Install gettext files at build time. (dshea)
- Use the python checks provided by automake. (dshea)
- Added a missing type check found by autoscan (dshea)
- Cleanup the widgets autoconf file (dshea)
- Add detail to logs when creating users and groups (dshea)
- Fix miscellaneous errors in installclass.py. (clumens)
- Fix a variety of errors in the packaging module. (clumens)
- Do not run pylint against executable files in pyanaconda/. (clumens)
- Clean up deprecated uses of the string module. (clumens)
- Call the right superclass's method. (clumens)
- Straighten out text UI methods so they have the same method signature.
  (clumens)
- Remove the lines to ignore E0611. (clumens)
- Bootloader.read is completely unused; cut it. (clumens)
- Fix all the "X is defined outside of __init__" warnings. (clumens)
- Display the correct string for the space required by packages. (clumens)
- Remove lines that clearly just don't do anything. (clumens)
- If we're not going to use the return value, don't grab it. (clumens)
- kernelVersionList in tarpayload.py should act the same as all other versions.
  (clumens)
- If we're not going to use the exception object, don't grab it. (clumens)
- Define stage2_device in the BootLoader class. (clumens)
- Don't call getPassAlgo before running createGroup. (clumens)
- Remove some unused values out of constants.py. (clumens)
- Finish taking care of pylint warnings in image.py. (clumens)
- Remove the unused network and write methods from the Anaconda object.
  (clumens)
- Remove the disable-msg lines for a couple C messages. (clumens)
- Remove some easy unused argument warnings. (clumens)
- Remove everything from InstallInterfaceBase except what Rescue needs.
  (clumens)
- Remove the duplicated imports. (clumens)
- Do not use a list or a dict as a default argument to a method. (clumens)
- Remove unneeded lambdas. (clumens)
- Fix up all the warnings where we used a reserved function name or keyword.
  (clumens)
- Fix up about half of the "except:" and "except Exception:" lines. (clumens)
- Fix a couple undefined variable errors that were real bugs. (clumens)
- Ignore statements that have no effect. (clumens)
- Fix up all the wildcard imports except two in packaging. (clumens)
- Remove all unused import lines. (clumens)
- Remove unnecessary pass statements. (clumens)
- Fix bad indentation and tab-instead-of-space warnings from pylint. (clumens)
- Put the pylint test back into service. (clumens)
- Run make with multiple jobs in makeupdates (vpodzime)
- Use gtk_image_new_from_icon_name (bcl)
- Remove caching of unused device list. (dlehman)
- Check MBR gap size even when /boot is on a plain partition. (#986431)
  (dlehman)

* Thu Aug 08 2013 Brian C. Lane <bcl@redhat.com> - 20.5-1
- Don't wait for systemctl shutdown command to exit (#974383) (bcl)
- Fix the logging of the spice-vdagent status (dshea)
- Update PYTHONPATH so unit tests work right out of the source tree. (clumens)
- Don't check for a firstboot service file before processing the command.
  (clumens)
- Strengthen the services command processing a bit. (clumens)
- Start spice-vdagent (#969405) (dshea)
- Skip password strength check for kickstart passwords (#986490) (dshea)
- Network spoke: fix refresh of device IP configuration (rvykydal)
- Add unsupported hardware dialog (#872728) (bcl)
- storage.py -> system.py in POTFILES.in (clumens)
- border_width=5 -> border_width=6 (clumens)
- No need to call threads_init anymore (bcl)
- Consolidate storage and networking under one category (#973013). (clumens)
- When doing a live install, set the ks method appropriately (#986069).
  (clumens)
- Check that we're doing an HD install before examining the attr (#989428).
  (clumens)

* Thu Aug 01 2013 Brian C. Lane <bcl@redhat.com> - 20.4-1
- POTFILES.in: rename time.py to time_spoke.py (bcl)
- Only move INSTALL_TREE when it is mounted (#888196) (bcl)
- Use ksdata.method.seen (#986069) (bcl)
- Threaded Koji RPM lookups and downloads (mkolman)
- Fix the langcode parsing regexp (vpodzime)
- Move tests to old_tests and add some new, working tests (vpodzime)
- Replace hostname with hostnamectl (#989584) (rvykydal)
- Require fcoe-utils only on ix86 and x86_64 architectures (#989913) (vpodzime)
- Fix searching for local RPMs with no version required (vpodzime)
- Expand the '~' in the RPM_FOLDER_NAME (vpodzime)
- Set system date and time with our own function (vpodzime)
- Remove the useless, confusing and lying PoolsNote (vpodzime)
- Use tiny, fast and thread-safe ntplib module instead of ntpdate (vpodzime)
- For vnc require network in intramfs (#989156) (rvykydal)
- Fix makeupdates' package fetching when no version is specified (vpodzime)
- Make it clear on the summary dialog that changes take effect later. (clumens)
- Don't mark the summary dialog's tree view as insensitive. (clumens)
- Work with files in a more pythonic way in makeupdates (vpodzime)
- Honor hostname set in kickstart (#988483) (rvykydal)
- Do not automatically set UTC mode on kickstart installs. (clumens)
- Add automatic fetching of RPMs for new Defines & Requires (mkolman)
- Don't prompt for ssh on s390x if doing an image install. (#983056) (sbueno)
- Rename tz spoke to avoid potential conflict with std 'time' module. (sbueno)

* Thu Jul 25 2013 Brian C. Lane <bcl@redhat.com> - 20.3-1
- Fix driver disk path for inst.dd= method (#987513) (bcl)
- Add support for NFS as install source in TUI. (#971298) (sbueno+anaconda)
- Allow logging into multiple iscsi nodes at once (#975831). (clumens)
- Fix crash while parsing ntp servers from DHCP6 (#969303) (dshea)
- Use ExceptionInfo namedtuple when dumping anaconda (#982299) (vpodzime)
- Wait for device connections for iface-bound iscsi in kickstart (#740105)
  (rvykydal)
- Refer to blivet instead of storage in iscsi kickstart (#740105) (rvykydal)
- Mark disk 'selected' if only one present in TUI. (#975790) (sbueno+anaconda)
- Update devicetree only if we logged in to some target in add iscsi dialog.
  (rvykydal)
- Don't show multipath members in specialized disks overview (#740105)
  (rvykydal)
- Do not populate devicetree after each single login in iscsi dialog (#740105)
  (rvykydal)
- Match also iface when logging into selected iface-bound iscsi target
  (#740105) (rvykydal)
- Fix handling of non-ASCII names (#969309) (dshea)
- Use inline completion for the region/city selection (vpodzime)
- Fix copyright of the main anaconda script (vpodzime)

* Mon Jul 15 2013 Brian C. Lane <bcl@redhat.com> - 20.2-1
- Use the new wait for connectivity function (mkolman)
- Improve waiting for network connectivity (mkolman)
- Use langtable to get default layout instead of our magic (#485137) (vpodzime)
- Adapt to the new localization module (vpodzime)
- Rewrite the localization module (vpodzime)
- Make the Welcome spoke wait for Geolocation lookup to finish (#975193)
  (mkolman)

* Tue Jul 09 2013 Brian C. Lane <bcl@redhat.com> - 20.1-1

* Thu May 23 2013 Brian C. Lane <bcl@redhat.com> - 19.30-1
- Fix software selection in text UI. (#965974) (sbueno+anaconda)
- Don't call _update_summary from within _add_disk_overview. (clumens)
- getDisks should not return a list that has duplicates in it. (clumens)
- Fix the rescan button (#929299). (clumens)
- Let checkbox disable updates-testing (#962522) (bcl)
- disable updates when method is set in ks (#952791) (bcl)
- Fix string formatting on text UI storage spoke. (#965460) (sbueno+anaconda)

* Tue May 21 2013 Brian C. Lane <bcl@redhat.com> - 19.29-1
- Handle empty text in simpleline (bcl)
- Fixup TUI source to work with kickstart (bcl)
- Add missing disk_selection XML (#962012,#962631) (bcl)
- Add ability for users to specify an installation source repo in text UI.
  (sbueno+anaconda)
- Add the ability to select software in text UI. (sbueno+anaconda)
- Add 'refresh' option in TUI; lock users out of threads that aren't ready
  (sbueno+anaconda)
- Add 'software' category to TUI summary hub (sbueno+anaconda)
- Only try to activate layouts if runtime system can be changed (vpodzime)
- Be more defensive in handling layouts from kickstart (#963103) (vpodzime)
- Return all layouts the XklWrapper knows about (#883555) (vpodzime)
- Fix issue where FS selection not applied in text UI. (#964069)
  (sbueno+anaconda)

* Thu May 16 2013 Brian C. Lane <bcl@redhat.com> - 19.28-1
- Remove testing leftover (#963503) (rvykydal)

* Wed May 15 2013 Brian C. Lane <bcl@redhat.com> - 19.27-1
- Partial fix for screen resize problems (#869364) (clumens)
- Remove an extra call to page clicked handler from refresh. (#959722)
  (dlehman)
- Always run through the full storage spoke. (#960732) (dlehman)
- Update apply button as appropriate after invoking dialogs. (#960254)
  (dlehman)
- Don't allow setting btrfs subvolumes' size. (#959723) (dlehman)
- Drop btrfs-specific raid level "single" for non-btrfs. (#959688) (dlehman)
- Update btrfs volume label when changing volume name. (#959727) (dlehman)
- Don't allow setting labels for btrfs subvolumes. (#960601) (dlehman)

* Wed May 15 2013 Brian C. Lane <bcl@redhat.com> - 19.26-1
- Pressing Delete on custom part should remove the selected mountpoint.
  (clumens)
- Use the same text formatting on the langsupport spoke as on the welcome
  spoke. (clumens)
- Remove the now-unused LanguageMixIn. (clumens)
- Do not BuildRequire python-bugzilla on RHEL (#953182) (dcantrell)
- Don't require network configuration in Live DVD (#962485) (rvykydal)
- Set default FS choice to LVM in text mode (#962600) (sbueno+anaconda)
- Move udev rules generation to pre-trigger (#958924) (bcl)
- Suggest names for btrfs mountpoints (bcl)
- Use a method to reset current_selector (#959707) (bcl)
- Fix non-default language being hidden in welcome spoke (mkolman)
- Mark placeholder text in add addtnl keyboard screen as translatable.
  (sbueno+anaconda)
- Mark language search string translatable. (#955229) (sbueno+anaconda)
- Remove the get_current_layout_name function (#895766) (vpodzime)
- Add support for the realm command (mkolman)
- Revert "Add support for the realm command" (mkolman)
- Add support for the realm command (mkolman)
- Support for getting NTP servers from DHCP (#862755) (mkolman)

* Thu May 09 2013 Brian C. Lane <bcl@redhat.com> - 19.25-1
- Change the buttons on the quit dialog. (clumens)
- Add FONT=latarcyrheb-sun16 to /etc/vconsole.conf (vpodzime)
- Use ntpdate instead of rdate (#950267) (vpodzime)
- Add layouts with a country if not added with a language (#960569) (vpodzime)
- Fixup xconf keymap code for text/dirinstall (bcl)
- Bump pykickstart to 1.99.30 for liveimg support (bcl)
- Add kickstart liveimg install command (bcl)
- Make sure all threads are done before install (bcl)
- Make sure stage1_disk isn't empty (#950487) (bcl)
- Add /boot/efi to suggested mountpoints (#960677) (bcl)
- Add extlinux command-line option. (mattdm)
- Add extlinux as a bootloader type. (mattdm)
- Bump the pykickstart requirement for the extlinux patches. (clumens)
- Revert "Busy cursor when applying changes in the custom spoke" (mkolman)
- Revert "Context manager for doing things with busied cursor" (mkolman)
- Use the F19 bootloader class from pykickstart, for --extlinux (mattdm)
- Transform bootloader --extlinux to extlinux command-line option (mattdm)
- Rework the layout of the storage spoke for low resolution setups. (clumens)
- Fix lower resolution display problems on the filter spoke. (clumens)
- Don't show iscsi passwords when focused, either.  Enjoy typing blind.
  (clumens)
- Add a couple more things to .gitignore. (clumens)
- Remove the bootloader class's obsoletes attribute. (clumens)
- Disable sort indicators on the filter UI. (clumens)
- Remove the Viewport from the disk shopping cart. (clumens)
- Cleaning up some of the TUI storage code (sbueno+anaconda)
- Add ability in TUI for users to select partitioning scheme. (sbueno+anaconda)
- Use the firmware-provided language if it's something we support. (pjones)
- Use systemd-localed for writing out xorg conf file (#958714) (vpodzime)
- Busy cursor when applying changes in the custom spoke (vpodzime)
- Make sure the "unbusy cursor" is used for the exception window (vpodzime)
- Context manager for doing things with busied cursor (vpodzime)
- Revert "Add signal handlers for controlling password entry visibility."
  (#958608). (clumens)
- Force a password to be set if option checked in TUI. (#927956)
  (sbueno+anaconda)
- Fix a minor display issue in TUI. (sbueno+anaconda)
- hostname has dropped -v option (bcl)
- Only override proxy and noverifyssl if specified (#880482) (bcl)

* Fri May 03 2013 Brian C. Lane <bcl@redhat.com> - 19.24-1
- Fix check for early exit from on_container_changed. (dlehman)
- Add ability to manipulate container sizes directly. (dlehman)
- Don't lock users who chose custom storage out. (dlehman)
- Don't allow unhiding of hidden disks during disk image installs. (#956020)
  (dlehman)
- Add layout indicator to the LUKS passphrase dialog (vpodzime)
- Add layout indicator to the BaseWindow (vpodzime)
- LayoutIndicator widget (vpodzime)
- self._password is set to None not "" initially (#958723) (vpodzime)
- Use constants for protocol's order instead of magic numbers (vpodzime)
- Support setting the name of a btrfs subvol (#892363). (clumens)
- If there are errors processing the kickstart file early on, just print them.
  (clumens)
- Stop defining _, N_, and P_ all over the place. (clumens)
- Fix a probably rare traceback in resizing from the custom part UI. (clumens)
- Add methods to do some hiding/showing that we do several different places.
  (clumens)
- Make it more obvious which fields on custom part are editable (#958251).
  (clumens)
- Clean up some of the get_object usage in custom.py. (clumens)
- Streamline DatetimeSpoke's timezone updating (#953311) (vpodzime)
- Allow setting timezone on the map without signal (vpodzime)
- Sensitivity of the date&time settings doesn't depend on timezone (vpodzime)
- Give the RAID level label on custom a mnemonic widget. (clumens)
- Give the hostname entry a keyboard shortcut. (clumens)

* Mon Apr 29 2013 Brian C. Lane <bcl@redhat.com> - 19.23-1
- Only check mandatory spokes in automated install (#956960,#895258) (bcl)
- Add scratch-bumpver target (bcl)
- Add Driver Update Disk repo handling to Anaconda (bcl)
- Add Driver Update Disk support to anaconda-dracut (bcl)
- Port driver update utilities from loader (bcl)
- Fix a typo. (clumens)
- Do not translate a blank window name. (clumens)
- Add a separator under the default language on the welcome screen. (clumens)
- Move the selected language to the top of the list on the welcome screen.
  (clumens)
- Remove the unused LanguageSpoke. (clumens)
- Add the "Add FCoE" dialog (#903122). (clumens)
- Allow enabling /etc/anaconda.repos.d repos like the docs say (#955724).
  (clumens)
- Move where the password quality checker is created (#956049). (clumens)
- Allow multiple disk selection with Shift-click (#864707) (vpodzime)
- Select all disks in the box with advanced storage as well (vpodzime)
- Don't change DiskOverview's background on 'chosen' changed (vpodzime)
- Fix number of arguments for languageGroups (liveDVD class) (#957038)
  (rvykydal)
- Apply some minor padding fixes on the container editing dialog. (clumens)
- If no root password was given, lock root's account (#927922). (clumens)
- Remove some unneeded boxes and alignments in the NTP config dialog. (clumens)
- Default to using the iscsi discovery credentials for login, if provided.
  (clumens)
- langsupport spoke: keep data.lang.lang first in status of spoke (rvykydal)
- Unpack property value returned by GDBus before using it (#956614) (rvykydal)
- Don't traceback when no activated devices were found for ks network default
  (#956614) (rvykydal)
- Ask about VNC also in connecting state, not only connected (#952801)
  (rvykydal)

* Wed Apr 24 2013 Brian C. Lane <bcl@redhat.com> - 19.22-1
- Container management improvements. (dlehman)
- Include swap-related disk space needs in storage options dialogs. (#951269)
  (dlehman)
- Show the summary screen before the luks passphrase dialog. (dlehman)
- Add language support spoke (#912364) (rvykydal)
- Add kickstart lang --addsupport option (#912364) (rvykydal)
- Add network --ipv6gateway kickstart option (#905226) (rvykydal)
- Remove pre-18.0 history from anaconda.spec. (clumens)
- Add free space information to DiskOverviews (#949746). (clumens)
- Raise exception if our module fails to be imported (vpodzime)
- Fix exception handling in rescue mode (vpodzime)
- Select all disks when Ctrl+A is pressed (#864707) (vpodzime)
- DiskOverview needs to grab focus if clicked (vpodzime)

* Mon Apr 22 2013 Brian C. Lane <bcl@redhat.com> - 19.21-1
- Set seen for lang from option & use constant for default (mkolman)
- Hook the Geolocation module to Anaconda (mkolman)
- Add geolocation module (mkolman)
- Add logging to exception handling (vpodzime)
- Run exception handling in the main thread also in TUI (vpodzime)
- Update network ksdata with cmdline options (#893784) (rvykydal)
- Return network devices actually activated (instead of just active) (#949002)
  (rvykydal)
- Don't traceback if we can't find PermHwAddr when looking for slaves (#949341)
  (rvykydal)
- Add support for iSCSI iface binding. (rvykydal)
- Fix a traceback when handling node login authentication. (clumens)
- Add a requirement on python-IPy now. (clumens)
- Display individual buttons on the filter UI instead of a combo. (clumens)
- Hook up authentication for iSCSI discovery and node login. (clumens)
- When the clear button is clicked on the filter spoke, clear out the fields.
  (clumens)
- Remove the extra "Target LUN" search option. (clumens)
- If all iSCSI nodes have been logged into, leave the dialog. (clumens)
- Populate the port combo on the filter spoke's search page. (clumens)
- Hook up filtering for iSCSI devices. (clumens)
- Add initial iSCSI support to the advanced storage UI. (clumens)
- Add a generic function to FilterPage for setting up a GtkComboBoxText.
  (clumens)
- self.disks -> self.pages in filter UI refresh method. (clumens)
- Add a button to bring up the Add Additional dialogs. (clumens)
- Remove pixmaps no longer needed by newui. (clumens)
- Add a checkmark on a DiskOverview when it is selected. (clumens)
- Make a couple UI modifications to the resize slider. (clumens)
- Make several changes to how addons are displayed (#873498). (clumens)
- Allow clicking on environment and addon text to toggle them (#928010).
  (clumens)
- Fix scrolling problems on the environment side of software selection
  (#928008). (clumens)
- Handle quit messages on the text progress UI hub (#895756). (clumens)
- If there's an error while in text mode, display it. (clumens)
- Force sizes on the network toolbar buttons (#951580). (clumens)
- Disable the "Closest mirror" option if there's no fastestmirror plugin
  (#876135). (clumens)
- Move text UI summary hub setup into the setup method (#927315, #950956).
  (clumens)
- Bring the text storage spoke a little more in line with the graphical one.
  (clumens)
- Make a home directory for the user by default (#950792). (clumens)
- Add some padding under the ransom notes on the progress hub. (clumens)
- Remove a lot of ancient crud from the installclasses. (clumens)
- Set the default fs type on RHEL (#951088). (clumens)
- Add a Spoke.changed attribute. (clumens)
- Display device names on MountpointSelectors (#888872). (clumens)
- Add signal handlers for controlling password entry visibility. (clumens)
- Ransom notes can be either PNGs or JPGs. (clumens)
- dracut/parse-kickstart: handle network --mtu (wwoods)
- Exclude a couple more password variables from dumps (bcl)
- Enlightbox dialogs in the custom spoke (vpodzime)
- Create and use GtkWindowGroup for our windows (vpodzime)
- We can import Gtk globally now (vpodzime)
- Handle both types of data we can get from libxklavier (#950921) (vpodzime)

* Tue Apr 16 2013 Brian C. Lane <bcl@redhat.com> - 19.20-1
- Fix two more syntax errors in the custom spoke. (#952662) (dlehman)

* Mon Apr 15 2013 Brian C. Lane <bcl@redhat.com> - 19.19-1
- Show device size with full precision to avoid spurious resize. (#951276)
  (dlehman)
- Fix another typo (old_fstype->old_fs_type). (#951593) (dlehman)
- Fix typo encryption_changed->changed_encryption. (#950700) (dlehman)
- Remove some remnants of old multipath code. (#951259) (dlehman)
- Protect the block device containing the stage2 image. (dlehman)
- Clarify code for iutil.get_active_console() etc. (wwoods)

* Thu Apr 11 2013 Brian C. Lane <bcl@redhat.com> - 19.18-1
- Revert "Revert "Don't emit "gfxterm" in grub2 configs (#821355)"" (pjones)
- Make "s" a hotkey for "Save Changes" on Advanced User Configuration. (pjones)
- Clean up tracebacks saved in pstore space (#950709) (pjones)
- Move anaconda-yum to /usr/libexec/anaconda/ (bcl)
- Cleanup: remove dead upgrade code (wwoods)
- Fix console= persistence, remove serial (#928269) (wwoods)
- Revert "Don't emit "gfxterm" in grub2 configs (#821355)" (pjones)
- Disable grub2-mkconfig's submenus by default. (pjones)
- Don't emit "gfxterm" in grub2 configs (#821355) (pjones)
- updates to boot-options.txt (wwoods)
- flags.py: remove unused flags (wwoods)
- remove flags.virtpconsole (wwoods)
- Call os.chdir("/") after calling os.chroot (vpodzime)

* Tue Apr 09 2013 Brian C. Lane <bcl@redhat.com> - 19.17-1
- Pass open file to execWithRedirect for vncpasswd (#948638) (bcl)
- Fix ip= saving in parse-kickstart (hamzy)
- Fix initial raid level when switching to a raid-capable device type.
  (dlehman)
- The raid level combo cannot be not sensitive for preexisting devices.
  (dlehman)
- Make sure fstype combo is not sensitive for btrfs devices. (dlehman)
- Add an entry to the raid level combo for btrfs' single. (dlehman)
- Clean up _save_right_side and adapt to changes in blivet.devicefactory.
  (dlehman)
- Remove anaconda's udev rules. (dlehman)
- Add requires for some things that aren't strictly required by blivet.
  (dlehman)
- Parent's finalize method needs self (vpodzime)
- Use Sphinx syntax for docstrings (vpodzime)
- Use None for unbounded size requests. (dlehman)
- Disable yum lock debugging for the final release. (clumens)
- The source spoke should display something nicer than "Not ready" (#948112).
  (clumens)
- Don't run storage execution in an endless loop (#948331, #948285). (clumens)
- If an incorrect source is given for a ks install, don't fallback (#948212).
  (clumens)
- Fix a bug when creating a new mountpoint with no given size (#948228).
  (clumens)
- memInstalled has moved (#947261). (clumens)
- Correctly report an error if OSError is hit when setting up the source
  (#947634). (clumens)
- Add anaconda-yum to %%files (bcl)

* Thu Apr 04 2013 Brian C. Lane <bcl@redhat.com> - 19.16-1
- Modify LocaledWrapper to use our safe_dbus module (#928287) (vpodzime)
- Add module providing safe DBus operations (vpodzime)
- Define a DEFAULT_DBUS_TIMEOUT constant and use it (vpodzime)
- Execute the yum transaction in another process (bcl)
- Add anaconda-yum (bcl)
- Add execReadlines utility (bcl)
- Use namedtuple instead of our magic tuples (vpodzime)
- Tell python-meh architecture of the anaconda package (vpodzime)
- Add release number to the result of getAnacondaVersion (vpodzime)
- Fix _isys.so location in the updates.img (vpodzime)
- Network spoke: Fix reading of device type from combobox (#947120) (rvykydal)

* Tue Apr 02 2013 Brian C. Lane <bcl@redhat.com> - 19.15-1
- Fix two small problems with the UID/GID spin buttons (#929173, #929138).
  (clumens)
- The Update Settings button should only be sensitive if you change something.
  (clumens)
- Move datetime spoke initialization into its own thread, too. (clumens)
- Make it more clear nothing will happen immediately on custom storage
  (#883195). (clumens)
- Replace the custom part size spinner with an entry. (clumens)
- Add a factory class for our various communications queues. (clumens)
- Make exception handling in the rescue mode work (#926913) (vpodzime)

* Thu Mar 28 2013 Brian C. Lane <bcl@redhat.com> - 19.14-1
- Handle the end of the %%addon section (vpodzime)
- Don't allow setting a mountpoint for an fstype we cannot mount. (dlehman)
- Fix a bug I introduced with 3c78c1a5c. (clumens)
- Get rid of the customization expanders on custom partitioning. (clumens)
- Translate the "Create a new volume group..." text (#892782). (clumens)
- Move the Desired Capacity label and spinner into its own row (#907883,
  #904999). (clumens)
- move Xorg test up so we might start vnc instead (hamzy)
- Set word wrapping on the label telling you how to switch layouts (#924885).
  (clumens)
- gtk_thread_wait -> gtk_action_wait in custom.py (#926926). (clumens)
- Support multiple values for kicstart network --namserver= in dracut (#917481)
  (rvykydal)
- get_widget -> get_object (#927898). (clumens)
- THREAD_* constants are in pyanaconda, not pykickstart. (clumens)
- Network spoke: fix model access thinko in Add device dialog (rvykydal)
- Use constants for thread names (mkolman)
- Move network connection timeout from network to constants (mkolman)
- udev-settle.service is now systemd-udev-settle.service (wwoods)
- Add boot-options.txt (wwoods)

* Fri Mar 22 2013 Brian C. Lane <bcl@redhat.com> - 19.13-1
- Set Tip text on the create user spoke. (dcantrell)
- Use space instead of underscore when user uses the timezone name (#924352)
  (msivak)
- Use only self.data in TUI timezone spoke's status (msivak)
- Use the named tuple in root password dialog (#924138) (msivak)
- Add message instructing users they can type to search for language.
  (sbueno+anaconda)
- Don't unbusy the cursor until the first action is ready to display. (clumens)
- Move custom storage setup into its own thread. (clumens)
- When you turn off NTP, clear the warning along the bottom of the screen.
  (clumens)
- If the disk has no serial number, don't give the DiskOverview a popup.
  (clumens)
- Reorder the columns on the shopping cart so name is next to description.
  (clumens)
- Add device node names to the resize dialog as a new column. (clumens)
- Use an emblem for indicating spokes have not been completed. (clumens)
- If you remove all the disks in the shopping cart, disable the buttons.
  (clumens)
- Apply a style to the network spoke's toolbar. (clumens)
- Add a little more space between the updates checkbox and the add repo stuff.
  (clumens)
- Remove the partition scheme expanders. (clumens)
- Don't error out if a ks %%include is missing when looking for sshpw
  (#923627). (clumens)
- Do not guess username immediately when user clears it (#924184) (msivak)
- Do not require password when no user is requested (#924150) (msivak)
- Refresh the checkboxes on AdvancedUser dialog properly (#924257) (msivak)
- Allow setting the default GID of the new user. (msivak)
- Add call to new-kernel-pkg --rpmposttrans (#922988) (bcl)
- Make our gtk_* decorators safer and more intelligent (vpodzime)
- Add method for checking if in main thread to the ThreadManager (vpodzime)
- Port the mandatory logic for User and Password spokes from GUI to TUI
  (msivak)
- Use only self.data to determine completeness in User spoke (msivak)
- Make firstboot kickstart command aware of initial-setup (msivak)
- Add command and data updates to AnacondaKSHandler's __init__ (msivak)

* Tue Mar 19 2013 Brian C. Lane <bcl@redhat.com> - 19.12-1
- _model -> model in filter.py. (clumens)
- Add some documentation to FilterPage. (clumens)
- Add the advanced storage UI and hook it up. (clumens)
- Don't wrap the DO creation in gtk_thread_wait. (clumens)
- Add a button to the specialized window to bring up the add dialog. (clumens)
- Filter out multipath devices from the getDisks results. (clumens)
- Reduce duplicated code between the GUI and TUI. (clumens)
- Set the horizontal and vertical scales to what we want. (clumens)
- Move DiskOverview creation out into its own method. (clumens)
- Add a slot on the storage spoke for display of advanced storage. (clumens)
- Log the actual exception for getPackage (bcl)
- Add the addon repos from a repo's treeinfo file (bcl)
- Disable failed repos, not remove them (bcl)
- Add repo addon to source spoke (bcl)
- Remove the previous addon repo code and UI (bcl)
- Addon repo glade changes (bcl)
- Enable updates repo by default (bcl)
- Adjust _getTreeInfo so that proxy_url can be passed (bcl)
- Add enable flag to RepoData object (bcl)
- Modify repo interface in packaging (bcl)
- Change the source DiskOverview to a label (bcl)
- Display the reason for payloadInstallHandler error (bcl)

* Mon Mar 18 2013 Brian C. Lane <bcl@redhat.com> - 19.11-1
- Don't create temporary lists if not needed (vpodzime)
- Fix reclaiming disk space for non-us installations. (rvykydal)
- Allow for raising thread exceptions when threadMgr.get is called (bcl,
  clumens). (clumens)
- Hook up the new refresh dialog. (clumens)
- Add a dialog prompting the user to refresh anaconda's view of storage.
  (clumens)
- Add a refresh button to the custom partitioning toolbar. (clumens)
- Add a reset button to the bottom right of the custom spoke. (clumens)
- Hook up the new action summary dialog. (clumens)
- Add a summary screen of actions to be performed on all disks. (clumens)
- Catch error when incorrect nfs address entered (sbueno+anaconda)
- Use GDBus also for connection settings update. (rvykydal)
- Network spoke: improve message format parametrization for translators
  (rvykydal)
- Don't set ibft device renaming for dracut, let it just do its job (#828505)
  (rvykydal)
- Mark Timezone selection as firstboot spoke (msivak)
- Add user creation spoke to TUI (msivak)
- Refactor TUI password spoke to use the declarative EditTUISpoke (msivak)
- Use guess_username from pyanaconda.users in gui.spokes.UserSpoke (msivak)
- Add declarative EditTUISpoke (msivak)
- Allow modyfying exit question in TUI (msivak)
- Return False from TUI.run() if it was exited prematurely (msivak)
- Add guess_username function to users.py (msivak)
- Mark incomplete mandatory spokes in text mode (msivak)
- Network spoke: move formatting parameters out of translation function
  (rvykydal)
- Network spoke: add keyboard accelerator to add device combobox (#906263)
  (rvykydal)
- Network spoke: don't decorate add_device_dialog (#906263) (rvykydal)
- Don't pass undefined stdout from execWithCapture. (rvykydal)
- Network spoke: import network module instead of list of too many functions
  (rvykydal)
- Vlan support: kickstart (#906272) (rvykydal)
- Vlan support: generate kickstart (#906272) (rvykydal)
- Vlan support: GUI - hub status information (#906272) (rvykydal)
- Network spoke: check whether added network device is already in list
  (#906272) (rvykydal)
- Vlan support: GUI - add "Vlan ID" and "Parent" to vlan tab (#906272)
  (rvykydal)
- Return correct nm_device_setting_value for bonds and vlans (#906272)
  (rvykydal)
- Vlan support: GUI - show vlan devices (#906272) (rvykydal)
- Vlan support: GUI - add "Parent" and "Vlan ID" info (glade) (#906272)
  (rvykydal)
- Vlan support: GUI - add vlan device (glade) (#906272) (rvykydal)
- Show that password was set by kickstart in TUI (msivak)
- Add settable quit message to TUI (msivak)
- Check _current_action for not being None before using it (vpodzime)

* Mon Mar 11 2013 Brian C. Lane <bcl@redhat.com> - 19.10-1
- Bonding support: GUI - hub status information (#906263) (rvykydal)
- Bonding support: GUI - generate kickstart network command for bonds (#906263)
  (rvykydal)
- Bonding support: GUI - add device dialog (#906263) (rvykydal)
- Bonding support: GUI - add device dialog (glade) (#906263) (rvykydal)
- Bonding support: GUI - device list, configuration and adding bond (#906263)
  (rvykydal)
- Bonding support: GUI - Slaves line in Wired tab (glade) (#906263) (rvykydal)
- Crypt the root we get from the user (#918991). (jkeating)
- Adapt to the new libxklavier's behaviour (vpodzime)
- We use python-meh's interfaces instead of Anaconda's (vpodzime)
- Redraw screen in case of valid input and nothing new scheduled (vpodzime)
- Fix two places where we are locking up the main thread (#886680). (clumens)
- Log when we acquire and release the _yum_lock (dlehman, clumens). (clumens)
- Do not fail when the logging stream cannot be opened (in initial-setup..)
  (msivak)
- Mark DateTime spoke as usable for Firstboot (msivak)
- Fix a missing import and move the addon KS output template (msivak)
- Make the TUI mainloop more resistant to screen implementation errors (msivak)
- Teach TUI how to react on async events (msivak)
- Could not load UI file advanced_user.glade (hamzy)
- Don't try to remove the timer when it's None (DatetimeSpoke) (vpodzime)
- Log failed imports in the collect functions (vpodzime)
- remove the remnants of sparc support (dennis)
- Remove installmethod.py (dead code) (wwoods)
- Make default media eject behavior match old behavior (wwoods)
- Silence "cp: cannot stat '/etc/cmdline'..." error message (wwoods)

* Fri Mar 01 2013 Brian C. Lane <bcl@redhat.com> - 19.9-1
- Behave nice when root password is set by kickstart (msivak)
- Password spoke is mandatory if the created user is not an admin (msivak)
- Use the user data provided by kickstart (msivak)
- Add the User creation spoke including the Advanced dialog (msivak)
- Bonding support: kickstart (rvykydal)
- Condense some duplicated and overly wordy code in custom.py. (clumens)
- Add a new allMembers property that returns a list of pages and members.
  (clumens)
- All Pages have a title, so get rid of the getattr games. (clumens)
- Allow more than one Page to be expanded at a time. (clumens)
- Get rid of the currentPage method. (clumens)
- Promote page._members to page.members. (clumens)
- Require passing the title to a Page's constructor. (clumens)
- Pressing F12 should do the same thing as clicking "Done" (#840998). (clumens)
- A bunch more "install" -> "installation" changes. (clumens)
- When the user clicks "Reclaim Space", go back to the hub (#911792). (clumens)
- Modify the logic that makes the reclaim button sensitive (#911793). (clumens)
- Add a free space line under every disk in the reclaim dialog. (clumens)
- Remove the initial sentence from the top of the reclaim dialog (#911793).
  (clumens)
- Fix a traceback in verifying optical media on the source spoke. (clumens)
- Revert "Hook up the "Remove Packages" button on the dep solving error
  screen." (#905899). (clumens)
- Don't display "(null)" as a MountpointSelector's mountpoint. (clumens)
- dracut: add anaconda-pre-shutdown.sh to fix eject (#809920) (wwoods)
- Continue booting when checkisomd5 is aborted (#891551) (bcl)
- Fix ksdevice=<MAC> - instead of renaming the device to ksdev0 just use it
  (rvykydal)
- Add pigz to initrd.img (wwoods)
- Use %%_prefix macro value when calling configure in makeupdates (vpodzime)
- Try to import modules the standard way first in collect (msivak)

* Thu Feb 21 2013 Brian C. Lane <bcl@redhat.com> - 19.8-1
- Add more stuff to the exception reporting skip list. (clumens)
- Compare Sizes to Sizes in the reclaim dialog (#913484). (clumens)
- The disk cart summary does not need a mnemonic. (clumens)

* Wed Feb 20 2013 Brian C. Lane <bcl@redhat.com> - 19.7-1
- Fix RAID level test (bcl)
- unpack product.img to /updates (#911873) (bcl)
- If you attempt to search on the network device pane, don't crash. (clumens)
- Don't treat the _ in x86_64 as a mnemonic. (clumens)
- If you set_markup, the label forgets set_use_underline from glade. (clumens)
- Don't try to update spokes that are indirect. (clumens)
- If you cannot reclaim more space, don't show the reclaim radio (#911791).
  (clumens)
- Swap the order of the part scheme combo and encryption checkbox. (clumens)
- Fix for the addons kickstart support (vpodzime)
- kickstart.py needs udev that now lives in blivet (vpodzime)
- Refactor pieces of the Datetime spoke and move some parts to kickstart.py
  (vpodzime)
- Set ONBOOT=no for default autoconnections (#905918, #886090) (rvykydal)
- Don't use "type" to name a variable. (rvykydal)
- Update all spokes on a Hub when spoke is exited (msivak)
- Wait for continueButton in KS mode if the user changed anything (msivak)
- Fix up word wrap on the DetailedErrorDialog. (clumens)
- Display storage warnings, similar to how errors are displayed (#909410).
  (clumens)
- Fix reprompting and screen redrawing on invalid input (vpodzime)
- Refresh addons_paths once we know if gui or tui takes place (vpodzime)
- Fixup anaconda.spec (bcl)

* Thu Feb 14 2013 Brian C. Lane <bcl@redhat.com> - 19.6-1
- fix uuid reference in parse-kickstart (bcl)
- Fixup kickstart script logging (bcl)
- Tell libreport the crash happened in Anaconda (#885690) (vpodzime)
- Restore older behavior regarding ks argument without a file name (#910550).
  (clumens)
- Move the encryption checkbox to the dialog (bcl)
- re-fetch metadata when proxy settings change (bcl)
- Apply some fixes to the spec file (#909592, metherid (clumens)
- install -> installation in a couple user-visible strings. (clumens)
- Restore support for partial kickstart files (#887254). (clumens)
- Get rid of packagesSeen. (clumens)
- Remove debugging print (DatetimeSpoke) (vpodzime)
- Honor modules' __all__ when doing collect (msivak)
- Use ksdata.addons instead of ksdata.addon and add ADDON_PATHS to sys.path
  (vpodzime)
- Remove unused modules (dbus) and stuff from network.py (rvykydal)
- Replace get_NM_connection() using new nm module. (rvykydal)
- Replace get_NM_settings_value() using new nm module (rvykydal)
- Replace nmIsConnected() using new nm module (rvykydal)
- Replace hasActiveNetDev() using new nm module (rvykydal)
- Replace getDevicesProperies() using new nm module (rvykydal)
- Replace getIPAddresses() using new nm module (rvykydal)
- Replace getMacAddress() using new nm module (rvykydal)
- Replace isWirelessDevice() using new nm module (rvykydal)
- Replace getLinkStatus() using new nm module (rvykydal)
- Replace getActiveNetDevs() using new nm module (rvykydal)
- Replace getDevices() using new nm module (rvykydal)
- Move NM dbus calls to separate module. (rvykydal)
- Move networking functions from isys to network module. (rvykydal)
- Remove unused stuff from network.py (rvykydal)
- Remove unused networking stuff from isys (rvykydal)
- Network spoke: remove unused NM path and interface constants (rvykydal)
- Add 'eject' to the anaconda initramfs (wwoods)
- Ensure hookdir exists before creating eject script (wwoods)
- remove anaconda-cleanup-initramfs.service (wwoods)
- Add dracut/save-initramfs.sh (wwoods)
- Bring back the askmethod parameter (#889887). (clumens)
- Add a new selectorFromDevice method to the accordion. (clumens)
- The storage logger is now the blivet logger. (dlehman)
- DeviceFactory has moved from blivet to blivet.devicefactory. (dlehman)

* Fri Feb 08 2013 Brian C. Lane <bcl@redhat.com> - 19.5-1
- Add --dirinstall command (bcl)
- Convert the mount point entry to one containing a drop down. (clumens)
- Move the Modify SW button into a link in the text. (clumens)
- Rework all the dialogs after you click Done on the storage spoke (#903501).
  (clumens)
- Overrides for the Gdk have _2BUTTON_PRESS defined (vpodzime)
- Add entries with completions to the comboboxes (DatetimeSpoke) (vpodzime)
- Make the custom partitioning bullet points take up less horizontal space.
  (clumens)
- Don't say you can reuse existing mountpoints unless there are some. (clumens)
- Point gobject-introspection at our updates directory for overrides. (clumens)

* Mon Feb 04 2013 Brian C. Lane <bcl@redhat.com> - 19.4-1
- Remove libcurl requirement from configure.ac. (dlehman)
- DMI_CHASSIS_VENDOR has moved into blivet. (dlehman)

* Fri Feb 01 2013 Brian C. Lane <bcl@redhat.com> - 19.3-1
- unpack product.img to correct location (#869098) (bcl)
- Fix including _isys.so and isys/__init__.py in updates.img (vpodzime)
- Fix typo "DHCPV6" (rvykydal)
- Don't crash on wireless connections created in Live CD desktop (#895736)
  (rvykydal)
- Adapt ifcfg -> ksdata mapping to NM change from IPADDR to IPADDR0. (rvykydal)
- Fix static and dhcp of network --ipv6 command (set IPV6_AUTOCONF=no)
  (rvykydal)
- NM defaults to IPV6_AUTOCONF=yes (rvykydal)
- Fix up spacing on installation options dialog buttons a little bit. (clumens)
- Ignore double clicks on the DiskOverviews (#902467). (clumens)
- When the user creates a new mountpoint, display it by default (#886039).
  (clumens)
- Add device node name information to the storage spoke and disk cart
  (#902617). (clumens)
- Do not include disks that have 0 size (#903131, #904977). (clumens)
- Preserve the state of the Customize... expanders on custom storage (#883134).
  (clumens)
- Make it a little more clear what's happening on the disk selection spoke
  (#903498). (clumens)
- Move Xorg to vt7 (bcl)
- Network: read ipv6 configuration type from NM settings instead of ifcfg file
  (rvykydal)
- Don't fail on missing ifcfg file when setting default ONBOOT (#904817)
  (rvykydal)
- Don't fail on invalid network --device kickstart specification. (rvykydal)
- Ignore ipv6 for a device (IPV6INIT=no) only for noipv6 option. (rvykydal)
- Network: fix disabling of ipv6 (noipv6 option) (rvykydal)
- Stop writing /etc/sysconfig/network (#895900) (rvykydal)
- We dont create missing ifcfg files on our own in anaconda anymore. (rvykydal)
- Use NM dbus interface to modify ifcfg configuration (#893892) (rvykydal)
- Document FileSystemSpaceChecker. (clumens)
- Add the customization category to POTFILES.in. (clumens)
- Add a license and overview to the g-i overrides file. (clumens)
- Create/clarify some documentation in the custom widgets. (clumens)
- Condense string formatting in a couple custom widgets. (clumens)
- Remove the widget-specific TODO list. (clumens)
- Add selinux to the list of parameters we pass on (#895860). (clumens)
- Display error status messages in a darker red color. (clumens)
- Add newline at the end of xorg.conf generated from ksdata (vpodzime)
- Move pyanaconda.packaging.get_mount_* into blivet.util. (dlehman)
- Remove obsolete references to simpleFilter. (dlehman)
- Remove the storage module and replace it with blivet. (dlehman)
- Move tsort, platform, and baseudev into storage. (dlehman)
- Start laying groundwork for splitting storage out of pyanaconda. (dlehman)
- Remove anaconda flag checking from OpticalDevice.eject. (dlehman)
- Remove unused functions and move storage-specific utils to storage. (dlehman)
- Remove installclass arch filtering. (dlehman)
- Handle sending program output to tty5 through the logging setup. (dlehman)
- Use dumpe2fs output to determine dirty fs. (dlehman)
- Remove filesystem migration code. (dlehman)
- Use threadMgr.wait to check threads (bcl)
- Add error reporting to threadMgr (bcl)

* Fri Jan 25 2013 Brian C. Lane <bcl@redhat.com> - 19.2-1
- Use only one large grid for the hubs. (clumens)
- Indicate nothing will happen until "Begin Installation" is clicked (#883195).
  (clumens)
- Exit anaconda correctly on SIGTERM (vpodzime)
- Move communication module to pyanaconda/ui (vpodzime)
- Function getDefaultHostname was renamed some time ago. (rvykydal)
- Use constant for default hostname ("localhost.localdomain" currently)
  (rvykydal)
- Make update_hostname function do just one thing - update ksdata. (rvykydal)
- Rename wait_for_dhcp pieces to say what they actually do (rvykydal)
- Initialize network synchronously (#902090) (rvykydal)
- xgettext wants "utf-8", not "utf8".  Python doesn't seem to care. (clumens)
- On the storage spoke, only show the summary button if a disk is selected.
  (clumens)
- Add text letting people know they can use existing filesystems (#883150).
  (clumens)
- Default to mirrored RAID instead of striped (#888867). (clumens)
- Replace the RAID level checkboxes with a single combo box. (clumens)
- Don't allow mountpoints to start with /proc or /sys either. (clumens)
- Add 'nmcli dev list' output to data gathered after crash (vpodzime)
- Add lsblk output to data gathered after crash (#879940) (vpodzime)
- Cleanup some trailing whitespace on otherwise empty lines (vpodzime)
- Refactor and cleanup exception handling pieces (vpodzime)
- Exception handling for text mode (#865325) (vpodzime)
- python-meh's saveExceptionWindow no longer uses the accountManager (vpodzime)
- Enable line wrapping in a couple more places (#901551). (clumens)
- Support /boot on RAID metadata version 1.2 (#896163). (clumens)
- Don't check memory for rescue mode (#895948). (clumens)
- Split __init__ and setup in TUI screens so we can set the environment and
  search paths (msivak)
- Add a requirement on device-mapper-multipath (#895973) (msivak)
- Update default fs type code (#855401). (clumens)
- Display the background gradient image from a map signal handler. (clumens)
- Remove the old cmdline and script interfaces. (clumens)
- anaconda-cleanup doesn't use an interface at all. (clumens)
- Remove the old text mode UI. (clumens)
- Move constants_text out of the textw directory. (clumens)
- Remove more references to system-config-*. (clumens)
- Add device NM_DEVICE_TYPE_ETHERNET to isys (#893892) (rvykydal)
- Dump missing ifcfg ifles only for ethernet devices (#893892) (rvykydal)
- Take over dhcp connection by NM for network root (eg nfs) (#883451, #893656)
  (rvykydal)
- Use DEFAULT_LANG instead of magic value "en_US.UTF-8" (vpodzime)
- fixup spec with 19.1 commits (bcl)

* Mon Jan 14 2013 Brian C. Lane <bcl@redhat.com> - 19.1-1
- Rework the reclaim dialog to have a resize slider. (clumens)
- g_type_init call is no longer needed (bcl)

* Fri Jan 11 2013 Brian C. Lane <bcl@redhat.com> - 18.40-1
- Prepare structures to save spoke completenes for firstboot and GIE (msivak)
- Do not call exit at the end of GUI interface, just quit the main loop
  (msivak)
- Improve handling of .py and .pyc equivalence while collecting classes
  (msivak)
- Set default language to en_US.UTF-8 (#891379) (msivak)
- Set the local hostname during installation (vpodzime)
- Refactor and cleanup our localization module (vpodzime)
- Network spoke: use correct state value to display device status. (rvykydal)
- drop fcoe-utils dependency for s390x (rhbz#894025) (sbueno+anaconda)
- More TODO list wrangling. (clumens)
- On storage, remove the "Continue" button and make "Done" do it all (#882737).
  (clumens)
- getLUKSPassphrase is no longer used, so kill it. (clumens)
- "Hub" shouldn't be in the title for any text mode hub. (clumens)
- Do not lightbox any dialogs on the custom storage spoke (#875291). (clumens)
- Revert "Do not lightbox the Add Mountpoint dialog (#875291)." (clumens)
- Don't allow changing a VG name to empty in the VG editor (#892395). (clumens)
- Check country_layouts is not None when using it (#893026) (vpodzime)
- Don't redownload payload from closest mirror only if we actually have some
  (#892665) (rvykydal)
- Remove some modules obsoleted by the packaging module. (dlehman)
- Prefer country over language when returning default layout (#867110)
  (vpodzime)
- Fix Quit button in standalone network spoke (#892120) (rvykydal)
- Network spoke: add sanity check for hostname setting (#856456) (rvykydal)
- Network spoke: add hostname setting (#856456) (rvykydal)
- Fix completeness check for md fwraid arrays. (#892621) (dlehman)
- Fix handling of failure to create a new container. (#892046) (dlehman)
- Force disk selection for interactive installs. (#888293) (dlehman)
- Mark another string for translation (#892760). (clumens)
- Do not lightbox the Add Mountpoint dialog (#875291). (clumens)
- Strip out pango markup before attempting to match languages (#892463).
  (clumens)
- Mark the live progress hub message for translation (#892069). (clumens)
- Allow deleting whole disks using the reclaim dialog (#880686). (clumens)
- Don't allow mountpoints to start with /dev (#891447). (clumens)
- Disable the configure button for pre-existing devices (#888296). (clumens)
- Add keyboard mnemonics to the spoke selectors, too. (clumens)
- Add keyboard accelerators to a whole lot of widgets (#864964). (clumens)
- Try fallback if none exactly matching language is found (#891487) (vpodzime)
- Only skip welcome screen for ks installs (#891755) (bcl)
- protect getDirSize from vanishing files (#891759) (bcl)
- start vnc without ip address (#832510) (bcl)
- Update physical device's sysfs path for btrfs (sub)volumes. (#891443)
  (dlehman)
- Wrap text on the updates checkbox to fix screen placement (#888880).
  (clumens)
- The return value from execWithRedirect is an int (#891313). (clumens)
- Add placeholder names to a couple strings (#890157). (clumens)
- Fix multiple copies of spokes appearing from update image (msivak)
- Import pyanaconda.addons in the anaconda script (vpodzime)
- Update the API which controls where should spokes be displayed (msivak)
- Update the way we look for glade files, spokes, hubs and categories (msivak)
- Make screenshot routines reusable in Firstboot (msivak)
- Do not fail when missing directories are present in addon paths (msivak)
- Pass addons paths to user interfaces (msivak)
- hook up help window close button (#889570) (bcl)
- add setKeyboardCheckButton to list of things to translate (#889352) (bcl)
- Mark for translation and show translated some more GUI elements (#877658)
  (vpodzime)
- Translate storage errors (#877658) (vpodzime)
- Don't allow changing the boot disk from inside the custom spoke. (#889585)
  (dlehman)
- Add help text and a help button to the custom storage spoke. (#889570)
  (dlehman)
- Allow /boot on btrfs subvol if using grub2. (#888603,868465) (dlehman)
- Don't keep old device name when switching to btrfs in custom. (dlehman)
- Fix container member set management for md arrays. (#889101) (dlehman)
- Include incomplete devices when listing dependant devices. (#889330)
  (dlehman)
- Use systemd to run checkisomd5 (#874486) (harald)
- fixup direct nfs iso url handling (#879187) (bcl)
- fixup nfs repo install code (#879187) (bcl)

* Wed Dec 19 2012 Brian C. Lane <bcl@redhat.com> - 18.39-1
- Add more yum locking to yumpayload (#860022) (bcl)
- The percent bar can go in the same column as the space label. (clumens)
- Don't resize NTFS partitions to smaller than the filesystem on them
  (#885912). (clumens)
- Remove some unused error handling code from old UI. (clumens)
- Don't generate ifcfg files for non-existing devices in parse-kickstart
  (#886647) (rvykydal)
- Encode unicode strings returned by pytz.country_timezones() (#887236)
  (vpodzime)
- Always set passphrase for newly encrypted devices. (#888560) (dlehman)
- Handle edit of preexisting encrypted lv. (#885378) (dlehman)
- Raise DeviceError instead of ValueError from device ctor. (#888089) (dlehman)
- Set line wrap on the info bar (#888112). (clumens)
- Don't crash when vg edit triggers spurious change event. (#883699) (dlehman)
- Add handling for incomplete lvm/md devices. (#876441) (dlehman)
- Fallback to mdN if no name was found for incomplete md array. (#873224)
  (dlehman)
- Add product.py to POTFILES (#858628). (clumens)
- Sort categories in GUI alphabetically (msivak)
- Fix typo in variable name (msivak)
- Collect addon paths properly (msivak)
- Move the import constants line below setupPythonUpdates (msivak)
- Only close AddLayout dialog on double-click if something is selected
  (#887371) (vpodzime)
- Add warning to keyboard spoke on live installations (#886463) (vpodzime)
- Split ksdata execute and setup methods for addons (msivak)
- Add support for KS %%addon section and the API+code to use it (msivak)
- Import collected modules only once (msivak)
- Update run-spoke to use paths (msivak)
- Export QuitDialog and it's message string (msivak)
- Update the hack we use to preload AnacondaWidgets - we need to load the
  typelib not just the .so file (msivak)
- Add FirstbootMixIn (msivak)
- Move the path definitions to Interface and pass it to the Hubs from there
  (msivak)
- Make TUI ready for getting spokes from multiple directories (msivak)
- Make GUI more reusable and support multiple directories for spokes and
  categories (msivak)
- Modify collect so it works with directories with missing __init__.py (msivak)
- Split completed and mandatory attributes (msivak)
- Move info about possible actions below the free space info (vpodzime)
- Fix a couple pylint errors (#867125). (clumens)
- Fix an undefined variable error (#867129). (clumens)
- The fs type combo should be sensitive when reformat is checked (#887201).
  (clumens)
- Remove idiomatic, hard to translate text (#865598). (clumens)
- Activate default layout when it is changed (#882440) (vpodzime)
- Validate and correct vg names as needed. (dlehman)
- Don't allow resize of devices with no/unrecognized formatting. (#869841)
  (dlehman)
- Add keyboard dracut setup args (#875567) (vpodzime)
- recheck software when source changes (#875599) (bcl)
- Include the new lib directory in the package (#886319, #886470). (clumens)
- Add a gradient background to spoke headers (mizmo, clumens). (clumens)
- Only allow changing filesystem type if the reformat combo is checked
  (#885906). (clumens)
- It's possible for mountpoint to be None (#885279). (clumens)
- Explicitly set True/False in the bootloader setting (#885381). (clumens)

* Tue Dec 11 2012 Brian C. Lane <bcl@redhat.com> - 18.38-1
- In interactive installs, default to bootloader in the MBR (#885284).
  (clumens)
- Make sure software selection is checked against filesystem space. (#853636)
  (dlehman)
- Update default install size and disk space estimate. (dlehman)
- Add checkbox for setting language default layout (#866887) (vpodzime)
- Change testing area label to something more appropriate (KeyboardSpoke)
  (vpodzime)
- Fix getting country layout variants (vpodzime)
- Wait for slower dhcp before running vnc server (#868777) (rvykydal)
- Network spoke: fix NMClient signal callback arguments (#885488) (rvykydal)
- Add logging for networking and improve logging of ifcfg files (rvykydal)
- Honor user request via UI to not install a bootloader. (#885240) (dlehman)
- Handle partition removals regardless of deepcopy. (#884896) (dlehman)
- Default to partitions for /boot* instead of just /boot/efi. (#884606)
  (dlehman)
- Fix a logic error in ActionDestroyFormat.obsoletes. (#885004) (dlehman)
- Take device type into account when making the config button sensitive
  (#885051). (clumens)
- Hide VG-related widgets when displaying a non-LV mountpoint first (#885131).
  (clumens)
- Install default system for %%packages --default (#869978) (bcl)
- Fix a typo in the live cd completion text (#884373). (clumens)
- Do not allow deleting or editing a protected device in custom part (#884599).
  (clumens)
- If path doesn't exist, don't traceback.  Return None. (clumens)
- Add/remove the HDISO source from protectedDevSpecs (#882147). (clumens)
- Put the bad VG name into the error message (#884359). (clumens)
- Use updated connection settings object for default auto config files
  (#883383) (rvykydal)

* Wed Dec 05 2012 Brian C. Lane <bcl@redhat.com> - 18.36-1
- Call udev_settle from inside udev_trigger. (dlehman)
- Prevent enabling the encryption checkbutton erroneously. (dlehman)
- Make sure Storage is initialized before refreshing the custom spoke.
  (dlehman)
- Fix initialization of Storage.roots to use a list. (#884270) (dlehman)
- Don't allow reformat without setting a mountpoint. (#883076) (dlehman)
- Fix check for toggled encryption checkbutton. (#882722) (dlehman)
- Make sure FS minSize is never greater than its currentSize. (#876547)
  (dlehman)
- When considering whether anything can be shrunk, throw out protected devs.
  (clumens)
- In the UI, mark the HDISO source device as protected (#879610). (clumens)
- update mdraid superBlock space calculation (#883483) (bcl)
- Remove resetResolver function, we don't need it anymore (#868695) (rvykydal)
- Network spoke: improve logging. (rvykydal)
- Unify writeNetworkConf with other modules (rename, put in ks.execute)
  (rvykydal)
- Fix network command --onboot and --activate options. (rvykydal)
- Fix two calls of self.window.set_info (#883632) (vpodzime)
- Use BaseWindow.set_warning and set_error in GUIObject's methods (vpodzime)

* Tue Dec 04 2012 Brian C. Lane <bcl@redhat.com> - 18.35-1
- Fix a bug when switching back to an HDISO install source (#879612). (clumens)
- Lower case the DONE button on media check. (clumens)
- Change mirrorlist checkbox text (#883191). (clumens)
- Change the bootloader button to indicate you can also not install one.
  (clumens)
- Stop writing /etc/sysconfig/keyboard (#871543) (mschmidt)
- Stop writing /etc/sysconfig/i18n (#871543) (mschmidt)
- Write /etc/hostname (#871543) (mschmidt)
- Correct doing string substitution for encryption. (clumens)
- Add install.py to POTFILES.in so a lot more strings can be translated.
  (clumens)
- Only instantiate main line action objects when they are needed. (clumens)
- Add a category to POTFILES.in so "USER SETTINGS" gets translated. (clumens)
- Make sure product info and spoke titles are translated throughout. (clumens)
- Substitute on new_install_name when it's needed, not at the top of custom.py.
  (clumens)
- Compare the protocol combox box on position, not text. (clumens)
- When we retranslate the welcome window, inform glibc. (clumens)
- Add gettext checks to widgets/configure.ac. (clumens)
- The initial welcome screen is the only one that needs to do retranslation.
  (clumens)
- Remove the generic retranslate method from the python portion of the UI.
  (clumens)
- Do not allow manipulating protected devices in the reclaim dialog (#882147).
  (clumens)
- ISOImage needs to look at /run/install/source for the mounted image
  (#879142). (clumens)
- Minor TODO list update. (clumens)
- Get rid of the unneeded action1. (clumens)
- Do not list some layouts twice (#882526) (vpodzime)
- Check if the given NTP server is a valid hostname (#865869) (vpodzime)
- Improve and document network.sanityCheckHostname (vpodzime)
- don't write network settings on image install (bcl)

* Sat Dec 01 2012 Brian C. Lane <bcl@redhat.com> - 18.34-1
- remove extra space in custom.py (bcl)

* Fri Nov 30 2012 Brian C. Lane <bcl@redhat.com> - 18.33-1
- Escape single percent signs in RPM changelog entries. (dcantrell)
- Fixes for PkgWrangler review. (dcantrell)
- Don't let defaults override user-specified container settings. (#879702)
  (dlehman)
- Fix partition allocation when enabling container encryption. (#879702)
  (dlehman)
- Remove partitions from all appropriate DiskLabel instances. (#870586)
  (dlehman)
- Add a way for users to set the names of lvm and md devices. (dlehman)
- Update the RAID-specific UI after changing the device's disk set. (dlehman)
- Correctly handle the default vg not having been instantiated yet. (dlehman)
- Drop requested container disks that don't have enough space. (#873293)
  (dlehman)
- Don't allow LVM disk set selection via configure button. (dlehman)
- Try to add new device to an existing container if disks are full. (dlehman)
- Fix code to lock encryption checkbutton for LV in existing VG (#877871)
  (dlehman)
- Add support for changing a new LV's VG. (dlehman)
- Fix check for in-use LV name to include VG name. (#875477) (dlehman)
- Remove the automatic show_all from those info_bar related functions.
  (clumens)
- Add set_info, set_error, set_warning functions to the BaseWindow object.
  (clumens)
- set_info functions may not be called from outside the main thread (#873600).
  (clumens)
- Test if path is valid before using it (NTPConfigDialog) (vpodzime)

* Wed Nov 28 2012 Brian C. Lane <bcl@redhat.com> - 18.32-1
- Bootloader checking should work in terms of self.stage1/2_ attrs (#880277).
  (clumens)
- Catch OverflowError in manual partitioning. (sbueno+anaconda)
- Do not accept tabs in the keyboard layout test box (#897312). (clumens)
- Wait for slower dhcp for payload setup and hostname setting (#873468)
  (rvykydal)

* Mon Nov 26 2012 Brian C. Lane <bcl@redhat.com> - 18.31-1
- Rename icons for liveinst (conflict with redhat-logos) (#878037) (rvykydal)
- Rework actions in the resize dialog to avoid shortcomings (#866209, #867770).
  (clumens)
- Check that everything's a GDK window before attempting to manipulate it.
  (clumens)
- On live installs, the progress hub should have a Quit button (#854904).
  (clumens)
- If no bootloader is to be installed, pop up a warning. (clumens)
- Escape ampersands in spoke status text. (clumens)
- Allow not setting any boot device via the UI (#867469). (clumens)
- Allow specifying whether the URL you've given is a mirrorlist or not
  (#868558). (clumens)
- Prevent false positives when checking for encryption change. (dlehman)
- Don't add incomplete VGs to the LVM reject filter. (#878225) (dlehman)
- Show device names for devices in the Unknown page/subsection. (#855646)
  (dlehman)
- Add a page to the custom RHS notebook for uneditable devices. (#875942)
  (dlehman)
- Fix error in iutil.execCapture when fatal and non-zero exit (stefw)
- Allow iutil.execWithCapture to work without a chroot (stefw)
- Handle hd iso leavings by dracut (#876897) (jkeating)
- show error when rsync fails (#868755) (bcl)

* Mon Nov 19 2012 Brian C. Lane <bcl@redhat.com> - 18.30-1
- only raise rsync error on error 12 (#868755) (bcl)
- Dump default auto connection's ifcfg file instead of writing a new one
  (#870922) (rvykydal)
- Number timezones starting with 1 (#859342) (msivak)
- only call bootloader.check() if bootloader is setup (#875278) (bcl)
- Fix operator precedence when checking for the presence of transifex-client.
  (clumens)
- Make the custom and keyboard toolbar buttons larger (mizmo). (clumens)
- More changes to leave the spoke via a glib idle call, not calling directly.
  (clumens)
- Hide the custom addon button. (clumens)
- Enable verbose yum logging once more (jkeating)
- rm transifex-client buildreq; check and install only if needed (sbueno)
- Handle nfsiso leavings by dracut (#876223) (jkeating)
- Prevent some raid-related tracebacks. (#874034) (dlehman)
- Don't try to save changes to a locked luks device. (#876180) (dlehman)
- Keyboard test layout padding fix (mizmo). (clumens)
- Correct colors for selected items in mountpoint selector widget (mizmo).
  (clumens)
- Include hidden disks in the storage spoke's list of devices (#875475).
  (clumens)
- Make the DetailedErrorDialog taller by default (#874620). (clumens)
- If there's only a Quit button, don't make it secondary. (clumens)
- Handle package dependency errors on kickstart installs too (#865073).
  (clumens)
- Remove iso-codes dependency, libxklavier has it fixed now (vpodzime)
- Rework custom partitioning alignment too (mizmo). (clumens)
- Attempt to fix the shrunken storage UI (mizmo). (clumens)
- Do not allow TreeView search in AddLayout dialog (#876131) (vpodzime)
- DiskOverview widget selection color correction (mizmo). (clumens)
- Use the main loop to control displaying the resize dialog. (clumens)
- Use ksdata to set default runlevel (jkeating)
- Execute xconfig data (#874868) (jkeating)
- Write out xconfig data when executed (jkeating)
- Code cleanups (jkeating)
- Link to the correct default target (jkeating)
- Add a mapping of old run level to new systemd target (jkeating)

* Mon Nov 12 2012 Brian C. Lane <bcl@redhat.com> - 18.29-1
- Quit after handling transaction errors. (clumens)
- Add a function to display relevant transaction errors (#873106). (clumens)
- Don't decorate error dialogs. (clumens)
- Fix error handling when new device ends up with size 0. (dlehman)
- Explicitly request all free space when no size given in custom. (#872833)
  (dlehman)
- Disable the language spoke off the first hub, for now (#874263). (clumens)
- Wrap text on install options dialogs (#874265). (clumens)
- Encode unicode strings from XklWrapper (#873762) (vpodzime)
- New version (out of order) (bcl)
- Network spoke: fix traceback (number of callback parameters) (#875393)
  (rvykydal)
- Adjust right margin for MountpointSelector (mizmo). (clumens)
- Fix introspection warnings for widgets (stefw)

* Fri Nov 09 2012 Brian C. Lane <bcl@redhat.com> - 18.28-1
- Show NFS as the source if dracut left it for us (#875235) (jkeating)
- Convert the accordion Button to a LinkButton (mizmo). (clumens)
- Buttons shouldn't scream at people (#868536, mizmo). (clumens)
- Don't attempt to handle exceptions when NFS mounts fail. (clumens)
- If there's an error setting up the source, display it as the status.
  (clumens)
- Add logging around the messages that can be processed by the hub. (clumens)
- You can't reformat a btrfs volume/subvolume. (dlehman)
- Always account for device removals in their containers. (dlehman)
- Fix container member management for md devices. (dlehman)
- Use a more robust method for removing previous autopart. (#868589) (dlehman)
- Post-custom sanity check determines storage spoke completeness. (#868925)
  (dlehman)
- Fix detection of inactive md arrays. (#873031) (dlehman)
- Vastly simplify the process for applying changes from custom spoke. (dlehman)
- Clean up container disk set and encryption change handling. (#874714)
  (dlehman)
- Honor kickstart bootloader --location=none. (#871143) (dlehman)
- Use original raid level and disk set when reverting a device. (dlehman)
- Set raid level based on defined volume for not-yet-btrfs mounts. (dlehman)
- Network spoke: improve status info (shorten) (rvykydal)
- Network spoke: update list of connected devices in hub status (rvykydal)
- Network spoke: Add "Connecting..." state to status (#868704) (rvykydal)
- Network spoke: Update status of networking in hub (#868704) (rvykydal)
- check for small grub2 embed space (#737508) (bcl)
- Set SpokeSelector's tooltip to spoke's status (vpodzime)
- Don't let mount/umount block python threads (#873600). (clumens)
- Fix makeupdates to correctly detect and include changes in isys. (clumens)
- Update pot file with proper lower cased buttons (#868536, mizmo). (clumens)
- Default to LVM on text installs too (#874586). (clumens)
- Remove network enablement in anaconda from rescue mode (#873854) (rvykydal)
- Add very basic U-Boot support for ARM platforms (dmarlin)
- Fix test for changed disk set for partitions. (#873994) (dlehman)
- Add support for preexisting whole-disk formatting. (#870476) (dlehman)
- There is no Storage.destroyFormat method. (dlehman)
- Move DEVICE_TYPE constants into storage and use them everywhere. (dlehman)
- A device scheduled for reformat is not unused. (dlehman)
- Catch the right exception when settin up raid options ui. (#873486) (dlehman)
- Network spoke: Use connection state that triggered a callback (bug #871429)
  (rvykydal)
- Use sr_Latn_RS instead of sr_RS (vpodzime)

* Wed Nov 07 2012 Brian C. Lane <bcl@redhat.com> - 18.27-1
- Mark more UI strings with N_ (#874276). (clumens)
- Pressing Enter on the passphrase dialog should continue (#788556). (clumens)
- Pressing Enter should activate the rightmost button on the detailed dialog.
  (clumens)
- Pressing enter on a MountpointSelector should display it on the RHS
  (#873352). (clumens)
- Make language groups work again (#873865) (jkeating)
- Update payload if slower dhcp succeeds in network pre-hub spoke (#873468)
  (rvykydal)
- Fix group access after parsing btrfs subvol list output. (#868468) (dlehman)
- Account for autopart swap size when checking free space. (dlehman)
- ignoredisk.onlyuse contains names, not StorageDevice instances. (#873463)
  (dlehman)
- Correctly handle toggle of encryption state for devices. (#873445) (dlehman)
- Handle changes to encryption state of container members. (#873445) (dlehman)
- Change custom spoke to apply encryption to PVs, not LVs. (dlehman)
- Widen the sidebar on custom partitioning (mizmo). (clumens)
- Fix spacing and padding on SpokeSelectors (mizmo). (clumens)
- Set the font globally (mizmo). (clumens)
- Handle if we get something other than a .treeinfo file (#872012). (clumens)
- If repo metadata fetching fails, set an info error message (#873605).
  (clumens)
- Enable yum langpacks plugin to get conditional packages (#868869) (jkeating)
- Base whether an add-on is selected on the selectedGroups, not ksdata
  (#873092). (clumens)
- Add UTC and GMT-X timezones (#863199) (vpodzime)
- TimezoneMap should handle "" timezone (vpodzime)
- raise error on rsync failure (#868755) (bcl)
- exclude bind mounts from rsync (#871637) (bcl)
- Fix up the InstallOptions3Dialog.refresh arguments (#873392). (clumens)
- Mark strings at the top of spokes with N_; translate later with _ (#872791).
  (clumens)
- Do not decorate the dialog that appears when you click on storage info bar.
  (clumens)
- You have to give "raise" an exception if you're outside a handler (#872874).
  (clumens)
- Prompt for encryption passphrase in reclaim path. (#869391) (dlehman)
- Prevent user from hitting save without entering a passphrase. (#869391)
  (dlehman)
- Font and padding updates for the network spoke (mizmo). (clumens)
- Fix alignment on the Add and Configure Mount Point dialogs. (clumens)
- Network spoke: activate wifi connection after setting secrets (#871132)
  (rvykydal)
- Fix nfsiso as stage2 (#871554) (jkeating)
- Fix traceback when saving changes to an existing partition. (#872446)
  (dlehman)
- Some more stuff for the mangleMap (#866730) (vpodzime)
- Handle locale's encoding and script in a better way (vpodzime)
- Use both language and country to guess layout (#861061) (vpodzime)
- Fix remaining issues with md fwraid. (#872739) (dlehman)
- Do not return None from Size.__str__ (#869405) (vpodzime)
- Add a platform weight for ARM images (dmarlin)
- Remove a bunch of stuff from the TODO list. (clumens)
- Don't decorate the main exception window. (clumens)
- Move the custom partitioning's Apply Changes button. (clumens)
- Indent partition type options under the expander further. (clumens)
- Left align the Label label, and indent the custom options further. (clumens)
- Lots of custom partitioning UI changes (mizmo). (clumens)
- Update fonts on the welcome language spoke (rlerch). (clumens)
- Lots of storage spoke font and spacing changes (mizmo). (clumens)
- Set the background of the custom partitioning accordion back to white
  (mizmo). (clumens)
- Set the Local Standard Disks background back to white (mizmo). (clumens)
- Reorder Device Type options in custom part to match the Partition Type combo.
  (clumens)
- Use the same terminology for partitions as is in use on the custom spoke.
  (clumens)
- livecd specific code has moved (bcl)
- Add progress percentage info to liveinst (bcl)

* Thu Nov 01 2012 Brian C. Lane <bcl@redhat.com> - 18.23-1
- Update parsing of 'btrfs subvol list' to match its new output. (#868468)
  (dlehman)
- Add a way to select the default device type. (dlehman)
- Enable specification of disk(s) for individual mountpoints. (#870569)
  (dlehman)
- Improve management of complex devices in custom spoke. (#865199) (dlehman)
- Save btrfs subvols' requested size. (dlehman)
- Reclaim extra set member growth evenly across members. (dlehman)
- Give lvmpv a slightly more realistic minimum size. (dlehman)
- Fix required space calculation for lvm. (dlehman)
- Don't filter disks when scanning storage after autopart fails. (#866717)
  (dlehman)
- Fix detection of partitioned md devices. (#866519) (dlehman)
- Correct handling of disks with hidden formats. (#866519) (dlehman)
- Revert "Fall back to lvm autopart if the default fails." (dlehman)
- Revert the default autopart type to lvm. (#870207) (dlehman)
- Apparently necessary kpartx changes (#867593) (dlehman)
- Mark a few more important strings for translation. (clumens)
- If lang= was provided on the command line, set the installation language.
  (clumens)
- Make the decision to skip the welcome screen more complicated. (clumens)
- Set a translation domain before loading a glade file. (clumens)
- Don't decorate the NTP config dialog. (clumens)
- Mark properties in existing glade files as translatable. (clumens)
- Widget properties exposed via glade need to be marked as translatable.
  (clumens)
- Network spoke: don't try to call replace on None (traceback) (#869106)
  (rvykydal)
- Fix nfsiso repo selection (#871648) (jkeating)

* Wed Oct 31 2012 Brian C. Lane <bcl@redhat.com> - 18.22-1
- Revert "Update parsing of 'btrfs subvol list' to match its new output.
  (#868468)" (dlehman)
- Pass RAID level to btrfs volume constructor. (#866101) (dlehman)
- Fix a traceback when removing non-existing partitions in custom. (#869839)
  (dlehman)
- Update parsing of 'btrfs subvol list' to match its new output. (#868468)
  (dlehman)
- Remove the word "review" from the label on the custom checkbutton. (#871109)
  (dlehman)
- Require that the root filesystem be created by anaconda. (#871104) (dlehman)
- On error, reset the RHS to what it used to be (#869422). (clumens)
- Don't prompt when in cmdline mode (#869685) (jkeating)
- Force a root password to be set (#869675) (jkeating)
- Network spoke: fix hostname handling in standalone spoke (#868535) (rvykydal)
- Network spoke: fix config info update after switching device OFF and ON
  (#871429) (rvykydal)
- Network spoke: connected requires activated (not active) connection (#871129)
  (rvykydal)
- Blank out passphrases from /root/anaconda-ks.cfg (#868519). (clumens)
- Setup package repo in the background (#870552) (jkeating)
- check disklabels when calculating free space (#863892) (bcl)
- updateBaseRepo does not need a storage argument. (clumens)
- Fix up calling superclass setup methods in packaging (#870556). (clumens)
- Fix a race condition with kickstarts (#868834) (jkeating)
- run checkisomd5 from anaconda-diskroot (#848764) (bcl)
- skip luks passphrase in exception dump (#868509) (bcl)
- Replace ' ' with '_' when looking for ifcfg files (#869106) (rvykydal)
- Remove storageComplete, which was only called from dispatch.py. (clumens)
- Remove dispatch.py and its associated test case. (clumens)
- Use a slightly different method to get supported languages (#858801, tagoh).
  (clumens)
- Fix problems when changing things in the software spoke (#868742, #869424).
  (clumens)
- Network spoke: fix callback arguments for device add/remove. (rvykydal)
- display storage errors in text mode storage spoke (bcl)
- only clear errors if re-running the check (#868707) (bcl)
- set boot flag and name for EFI partition (#866106) (bcl)
- clear pmbr_boot on EFI systems (#844551) (bcl)
- Lots of UI layout tweaks (mizmo). (clumens)
- /etc/sysconfig/keyboard doesn't support vconsole.xyz options. (notting)

* Thu Oct 25 2012 Brian C. Lane <bcl@redhat.com> - 18.21-1
- Add PowerNV as a recognized PPC platform (nacc)
- anaconda should print unknown platform information (hamzy)
- Toggle chosen property on focus change (MountpointSelector) (vpodzime)
- Lock source spoke while depsolving (#867591) (jkeating)
- In custom part, don't display mountpoints without associated disks (#865942).
  (clumens)
- Tie "Reclaim Space" button sensitivity to how much space the user freed
  (#869375). (clumens)

* Tue Oct 23 2012 Brian C. Lane <bcl@redhat.com> - 18.20-1
- Add dialog for configuring layout switching options (vpodzime)
- Initialize layout switching if needed (vpodzime)
- Save layout switching configuration (vpodzime)
- Add support for layout switching options to XklWrapper (vpodzime)
- We need to set _root in two places for a MountpointSelector. (clumens)
- Correctly destroy the deletion confirmation dialog. (clumens)
- Don't set self.data.method.url until after checking for a protocol (#869102).
  (clumens)
- Fix an undetected bug when setting up an HTTPS method. (clumens)
- YabootSILOBase objects don't have an encrypted_password parameter (#869016).
  (clumens)
- rprivate -> make-rprivate (#869246). (clumens)
- If NFS is selected in the source spoke, the URL must contain a colon
  (#869103). (clumens)
- Modify behavior when leaving the reclaim storage dialog (#864128, #867770,
  #868903). (clumens)
- Set the status text in the SpokeSelector widget differently now. (clumens)
- Use the correct font for each language on the welcome screen (#868836,
  tagoh). (clumens)
- Everywhere we make a MountpointSelector, give it a _root attr (#868702).
  (clumens)
- payloadInstallHandler should only optionally take a package argument
  (#868542). (clumens)
- Add a reformat checkbutton to indicate a desire to reformat the device.
  (dlehman)

* Fri Oct 19 2012 Brian C. Lane <bcl@redhat.com> - 18.19-1
- Reset the comps to empty along with everything else in yum. (clumens)
- Hook up the "Remove Packages" button on the dep solving error screen.
  (clumens)
- If nothing's changed in the software spoke, don't redo dep solving. (clumens)
- skip vnc prompt with text mode and kickstart (bcl)
- Use correct name for MD RAID device description text. (dlehman)
- Fix selector management after a reformat action is scheduled. (dlehman)
- Aqcuire yum lock before doing the work of _yumCacheDirHack. (#858993)
  (dlehman)
- Reset error list on success of doKickstartStorage. (dlehman)
- Tighten up management of passphrases across Storage resets. (#865364)
  (dlehman)
- Do not count not-yet-created filesystems as free space. (#866895) (dlehman)
- Remove any preexisting autopart layout before space check. (#866895)
  (dlehman)
- Apply disk selections to the devicetree before the space check. (#866895)
  (dlehman)
- Update free space totals before refresh after removing a device. (dlehman)
- Log exceptions raised from PartitionDevice constructor. (dlehman)
- Fix size specs for PartitionFactory. (dlehman)
- Reinitialize disks after removing the last partition from custom spoke.
  (dlehman)
- Refactor shouldClear slightly. (dlehman)
- Use correct means for getting device type in the custom spoke. (dlehman)
- Repopulate the RHS after editing a device. (dlehman)
- Don't bother resizing a container that has just been emptied. (dlehman)
- Don't allow implicit fstype change via mountpoint. (#866953) (dlehman)
- Set up devices before trying to decrypt them. (#865247, #867533) (dlehman)
- Don't short-circuit devicetree populate based on clearpart setting. (dlehman)
- Keep hostname when updating ksdata after GUI network configuration (#866516)
  (rvykydal)
- don't save system time on s390 (#867856) (dan)
- Network spoke: make Configure button insensitive when running nmce (#865931)
  (rvykydal)

* Wed Oct 17 2012 Brian C. Lane <bcl@redhat.com> - 18.18-1
- remove firewall.py from POTFILES.in (bcl)
- Add missing pieces for kickstart's encryption cipher option. (dlehman)
- update to use firewalld (#815540) (bcl)
- Fix a typo in method name (#863765) (msivak)
- Add missing import (#867296) (msivak)
- There is no anaconda object available in writeSysconfigKernel (vpodzime)

* Tue Oct 16 2012 Brian C. Lane <bcl@redhat.com> - 18.17-1
- Add an error handler for fatal package installation errors (#865291).
  (clumens)
- Modify the status test for the software selection spoke. (clumens)
- Various layout and font improvements to the keyboard spoke (mizmo, rlerch).
  (clumens)
- Just return the size string uppercased (#867074). (clumens)
- Revert "Use a capital "B" in the size module (#859932)." (clumens)
- Revert "Fix one more reference to bits (#859932)." (clumens)
- Fix padding around the addons view in the software spoke. (clumens)
- The Unknown page selectors/devices have no root. (dlehman)
- Avoid using mount --move on shared paths (#853508) (jkeating)
- Revert "Release Gdk lock in exception handling" (msivak)
- Make all Gtk calls from inside of it's main loop (and thread) (msivak)
- Remove Gdk thread initialization, introduce new helper functions and make
  exception handler be called by Gtk only once (msivak)
- Fix threading initialization (msivak)
- Do not remove the layout if it was added back (#865830) (vpodzime)
- Release Gdk lock in exception handling (vpodzime)
- Configure new-kernel-pkg to keep tboot configuration on updates (#742885)
  (pjones)
- Honor the nompath option. (dlehman)
- Validate lv names. (dlehman)
- Add support for specifying encryption cipher mode via kickstart. (dlehman)
- Acquire the yum lock before accessing YumBase.repos. (#858993) (dlehman)
- Remove the entry on the resize dialog's combo boxes. (clumens)
- disks_free -> disks_size (#863647). (clumens)
- Fix one more reference to bits (#859932). (clumens)
- Fix a traceback in media check (#865897). (clumens)
- Add support for deleting an entire root via the existing ConfirmDeleteDialog.
  (clumens)
- Don't traceback when removing a mountpoint with no expanded selector
  (#862746). (clumens)
- Remove the code for removing an entire Root all at once. (clumens)
- Yet more TODO list updates. (clumens)
- Don't display "None" in the name of a root. (clumens)
- Fix configuration of protected wireless connections (#855526) (rvykydal)
- Fix graphical kickstart with %%packages data (jkeating)
- Add password validation to text password spoke (jkeating)
- Make use of the validatePassword routine from users.py (jkeating)
- Add a password verification method to users.py (jkeating)
- Always honor the 'nokill' flag (vpodzime)
- Fall back to lvm autopart if the default fails. (#864708) (dlehman)
- Special boot devices are handled the same whether they exist or not.
  (dlehman)
- Fix a bug allocating fixed-size partitions. (dlehman)
- Clean up size sets immediately after allocation run. (#864771) (dlehman)
- Make sure partition base sizes are adequate for their formatting. (dlehman)
- Don't fail to account for all set members' growth. (dlehman)
- Remove some extra calls to show_first_mountpoint. (dlehman)
- Show the correct raid options for btrfs. (dlehman)
- Support change of raid level in custom spoke. (dlehman)
- Use devicetree as partition list source instead of parted. (#864718)
  (dlehman)
- Use Storage convenience methods to schedule reclaim actions. (dlehman)
- Pass disk list when trying to recover from device type change failure.
  (dlehman)
- Fill in missing parts of the disabled raid features dict. (dlehman)
- Clear errors when entering or leaving the custom spoke. (dlehman)
- Hook up signal handler for raid feature checkbuttons. (dlehman)
- Raise MDRaidError instead of ValueError from devicelibs.mdraid. (dlehman)
- Minimum we have to do with HW clock (vpodzime)
- Check X layouts specified in kickstart for validity (vpodzime)
- Work with VConsole keymap and X layouts separately (vpodzime)
- Add class wrapping systemd-localed functionality (vpodzime)
- Don't write XkbVariants if none are specified (vpodzime)
- Add comment to the begining of generated xorg.conf file (vpodzime)
- Don't display "None" for NIC vendors and products NM can't identify (#859540)
  (rvykydal)

* Thu Oct 11 2012 Brian C. Lane <bcl@redhat.com> - 18.16-1
- Don't try to load ifcfg files for wifi devices (#865355) (vpodzime)
- Rewrite isWirelessDevice to Python and DBus calls (#862801) (vpodzime)
- Use a capital "B" in the size module (#859932). (clumens)
- The environment window needs a vertical scroll bar (#865066). (clumens)
- liveinst should recognize inst.updates too (#865398). (clumens)
- Improve validation of device edit requests. (dlehman)
- Fix listing of subvolumes for existing btrfs volumes. (dlehman)
- Remove overzealous correction of device type for /boot*. (#863574) (dlehman)
- Pad filesystem minimum sizes to ensure other OS can still run. (dlehman)
- Handle encrypted partitions in size set classes. (dlehman)
- Don't set mountpoints of "(null)" in mountpoint selectors. (dlehman)
- Prevent crash trying to populate raid options on a one-disk system. (dlehman)
- Rework type combos and don't offer RAID on one-disk systems. (dlehman)
- Bundle more of data/ in updates.img (jkeating)
- Revive reipl (#860244) (jkeating)

* Wed Oct 10 2012 Brian C. Lane <bcl@redhat.com> - 18.15-1
- add noverifyssl to anaconda-dracut (#852229) (bcl)
- Don't crash when running anaconda a second time (jkeating)
- Handle ssh prompt in new tmux world (jkeating)
- Add a service to run anaconda directly on the tty (jkeating)
- Add a script to attach to anaconda's tmux (jkeating)
- Add ARM-OMAP class to create a uboot partition to support the boot-loader.
  (dmarlin)
- Avoid a loop of storage spoke executions during kickstart (#865048).
  (clumens)
- Correct lookup of raid.XX "mountpoints" for kickstart installs (#864764).
  (clumens)
- Change language matching on the welcome screen back around. (clumens)
- Another attempt at fixing the squished screen bug (#849211). (clumens)
- Fix a stupid typo in the disk shopping cart (#864842). (clumens)
- Reorder the buttons and labels on the bottom left of the storage spoke.
  (clumens)
- Modify the DetailedErrorDialog buttons. (clumens)
- Sync up hidden/unhidden disks between the UI and storage module (#864180).
  (clumens)
- When handling a storage error, reload self.disks (#862972). (clumens)
- Fix sshd bringup when also using a kickstart file (#863441) (jkeating)
- Require root password spoke be visited (#859069) (jkeating)
- add some thread logging (bcl)
- Reword the description on the resize dialog (#863577). (clumens)
- Present an error message if no disks are detected (#864093). (clumens)
- When changing environments, don't explicitly exclude groups (#863886).
  (clumens)
- Fix marking the "Modify Software Selection" button as sensitive in one case.
  (clumens)

* Mon Oct 08 2012 Brian C. Lane <bcl@redhat.com> - 18.14-1
- Add UI support for encrypted automatic partitioning. (dlehman)
- Add support to the custom spoke for encrypted block devices. (dlehman)
- Add a page for decrypting existing LUKS devices. (dlehman)
- Add a dialog for collecting a passphrase for newly encrypted devices.
  (dlehman)
- Add a property that provides a list of all selectors in the accordion.
  (dlehman)
- Handle luks formats during populate if they have a passphrase set. (dlehman)
- Add encryption support to the device factory classes. (dlehman)
- s/dev/disk in the disk shopping cart. (clumens)
- Set a default payload in InstallOptions1Dialog (#863582). (clumens)
- Pass disks into the SelectedDisksDialog (#863588). (clumens)

* Fri Oct 05 2012 Chris Lumens <clumens@redhat.com> - 18.13-1
- Make sure packages anaconda requires are installed. (clumens)
- Add method returning current activated X layout (vpodzime)
- Fix a deadlock when trying to add a keyboard layout (#862612). (clumens)
- ntfsresize uses SI (MB) while the rest of us use IEC (MiB). (#862109)
  (dlehman)
- Remove empty extended partitions after removing a logical partition.
  (dlehman)
- Handle all logical/extended partitions in unusedDevices. (dlehman)
- Update autopart/custom setting before moving to reclaim dialog. (#863225)
  (dlehman)
- Raise an exception early in newDevice if no disks were specified. (#858139)
  (dlehman)
- Fix a regression in BTRFSVolumeDevice.listSubVolumes. (#862742) (dlehman)
- Fix behavior of resolveDevice when devspec is a device name. (dlehman)
- Prevent BTRFS volumes from ever having the name None. (dlehman)
- Prevent negative free value for filesystems. (#861812) (dlehman)
- Don't show extended partitions that contain logical partitions. (#862971)
  (dlehman)
- Delete ts data instead of trying to undo dep installs. (#851114) (dlehman)
- Change the manglings for a couple locales (petersen). (clumens)
- Hook up the "Modify Software Selection" button on install opts dialogs.
  (clumens)
- More TODO list updates. (clumens)
- Add a label to the resize dialog for how much space is required. (clumens)
- Add a column to the disk shopping cart for setting the boot device (#860430).
  (clumens)
- Rework the disk shopping cart link a little bit. (clumens)
- Do not use constant value in SoftwareSpoke's completed property (vpodzime)
- Pull in existing swaps and bootloader devices whenever there are mounts.
  (dlehman)
- Revert broken logic for newly formatted devices in unusedDevices. (dlehman)
- Add an apply button to the device/mountpoint configuration options. (dlehman)
- Don't base StorageSpoke.ready on storage execute thread presence. (#861574)
  (dlehman)
- Prevent systemd timeout waiting for encryption passphrase. (#861123)
  (dlehman)
- Fix traceback when switching device type to lvm. (#860990) (dlehman)
- Fix error handling in the add mountpoint dialog. (#860992) (dlehman)
- Allow xfs /boot. (dlehman)
- Fix makeupdates to work for glade files in subdirs of spokes/ or hubs/.
  (dlehman)
- Fix parsing of NFS method strings (#860966) (jkeating)
- Make the URL entry sensitive for NFS installs, too (#863014). (clumens)
- Add in a locale mapping to avoid incorrect system settings (#858591).
  (clumens)

* Wed Oct 03 2012 Brian C. Lane <bcl@redhat.com> - 18.12-1
- copy-logs changed names (bcl)
- Reference correct UI button name (#862409) (jkeating)
- Don't echo vnc password to the screen (#862593) (jkeating)
- Make the log copy script the last one to run (jkeating)
- Copy ks script logs into the install root as well (jkeating)
- Create ks script logs outside of chroot (jkeating)
- Don't look for ifcfgs of wireless devices (#860791) (rvykydal)
- doAutoPartition should raise errors instead of handle them. (clumens)
- In the install options dialogs, call out how much space is on selected disks.
  (clumens)
- In order to display the resize prompt dialog, we need to compare Sizes to
  Sizes. (clumens)
- Use a better starting value for required space than 0. (clumens)
- Default to CLEARPART_TYPE_NONE (#855976). (clumens)
- Remove some unused clearpart-related settings. (clumens)
- Hook up the new resize dialog. (clumens)
- Add a resize dialog. (clumens)
- Require the hostname package (#862419) (jkeating)

* Tue Oct 02 2012 Chris Lumens <clumens@redhat.com> - 18.11-1
- Use gdk_threaded() when running AddLayout dialog (vpodzime)
- Work the anaconda object into the VNC test (jkeating)
- Use askvnc spoke to change vnc password (jkeating)
- Fix logic error in vnc password length check (jkeating)
- Allow vncpassword spoke text to be configurable (jkeating)
- Don't ask for VNC if we can't do it (jkeating)
- Skip VNC prompt if text is requested in kickstart (jkeating)
- KEYTABLE is now vconsole.keymap (#859298) (bcl)
- The partitionErrorHandler text needs a 's' in the format string (#861376).
  (clumens)
- Fix a problem with storage error handling (#861376). (clumens)
- Fix bootloader setup on s390. (#857940) (dlehman)
- Make Keboard and Welcome spokes runtime-system friendly (vpodzime)
- Make DateTime spoke runtime-system friendly (vpodzime)
- Add a guard for testing if we can modify runtime system (vpodzime)
- Bring back prompt for VNC (jkeating)
- Add standalone spoke to prompt for VNC (jkeating)
- Fail on incomplete ksdata when in cmdline mode (jkeating)
- Add a flag attribute to handle cmdline mode (jkeating)
- fix libuser setup (#855481) (bcl)
- Remove obsolete requirement on comps-extras. (notting)

* Wed Sep 26 2012 Chris Lumens <clumens@redhat.com> - 18.10-1
- isys.mount needs to be told when something should be mounted NFS (#860273).
  (clumens)
- Disks with new disklabels don't count as new devices in custom. (dlehman)
- Fix thread synchronization issue going from storage to custom. (#860495)
  (dlehman)
- Treat disks with unrecognized or no formatting as empty. (#858862) (dlehman)
- Improve management of mountpoint selectors in the custom spoke. (dlehman)
- Improve handling of existing devices when refreshing the custom spoke.
  (dlehman)
- Apply custom changes not involving actions to the main devicetree. (dlehman)
- Add a mountpoint entry to the device options area. (dlehman)
- Move mountpoint validation out of the add mountpoint dialog. (dlehman)
- Only run the storage sanity check if we've run autopart. (dlehman)
- Add a method to reset a device to its original state. (dlehman)
- Make a copy of the original format instead of just storing another ref.
  (dlehman)
- Reformatting effectively removes a device from an existing Root. (dlehman)
- Fix test for whether to create biosboot during autopart. (#853628) (dlehman)
- Close AddLayout dialog on double-click (vpodzime)
- Remove useless handler of Cancel button (AddLayout dialog) (vpodzime)
- Don't rely on having some month and year selected (#859185) (vpodzime)
- Add debug option to bumpver (bcl)
- Raise an error if bootDrive is invalid (jkeating)
- Handle automated installs (jkeating)
- Handle errors from text storage execute (jkeating)
- Fix ready and completed properties for text storage (jkeating)
- Use ksdata to determine text password completeness (jkeating)

* Tue Sep 25 2012 Chris Lumens <clumens@redhat.com> - 18.9-1
- And remove compssort.py from POTFILES.in, too. (clumens)
- Select a default environment (#858180). (clumens)
- Remove compssort.py. (clumens)
- Don't attempt to catch and re-raise a SystemError from AnacondaThread.run.
  (clumens)
- Add a progress message for quitting the installer. (clumens)
- GUI error handling dialogs need to be protected from threading deadlocks.
  (clumens)
- Initialize gdk threading as well. (clumens)
- Handle --ignoremissing in _applyYumSelections (#859021). (clumens)
- Fix the destination path for anaconda.xlog (#860041). (clumens)
- Hide the ISO install source if you've nuked all possible drives (#858088).
  (clumens)
- Don't write out /etc/sysconfig/clock anymore (#859217). (clumens)
- Index the exn mapping by string, not by object. (clumens)
- Don't write HOSTNAME=HOSTNAME=myhostnamehere (#859141). (clumens)
- Close temp file before moving it (#858681) (vpodzime)
- Update widget-specific TODO list. (clumens)
- Don't use grey for the status text of a SpokeSelector (#855638). (clumens)
- Fix a typo in makeupdates. (clumens)
- UEFI paths must include a leading backslash on some machines. (#856938)
  (pjones)
- Read cmdline files from /run/install (jkeating)
- Copy command line files prior to pivot (jkeating)
- Grab the proxy username from the correct text entry (#858536). (clumens)
- Remove our use of scsi_wait_scan (#858393). (clumens)
- Don't overwrite the opts attribute on NFS installs (#858700). (clumens)
- Change the keyboard shortcut for the updates checkbox. (clumens)
- Add the storage category to POTFILES.in. (clumens)
- Don't explicitly start the progress spinner in python code. (clumens)
- Move the progress bar back down to the bottom of the progress hub. (clumens)
- Remove a bunch of stuff from the TODO list for a change. (clumens)
- Move check of new partition size against format limits. (dlehman)
- Improve growth check when deciding where to allocate new partitions.
  (dlehman)
- Keep btrfs selectors' sizes in sync as volume size changes. (dlehman)
- Allow specification of a label for new swap space via custom ui. (dlehman)
- Don't allow stage2 as stage1 unless specified via location. (dlehman)
- Remove reference to PartitioningWarning, which was removed last week
  (#875931). (clumens)
- Add a way to test exception handling (vpodzime)
- Fix dumpState to work with the new python-meh (#856235) (vpodzime)

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
- dracut: suppress ks errors from missing %%include (wwoods)
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
