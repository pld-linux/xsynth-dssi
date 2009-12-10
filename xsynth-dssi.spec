#
Summary:	Software synthesizer plugin for the DSSI Soft Synth Interface
Name:		xsynth-dssi
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/dssi/%{name}-%{version}.tar.gz
# Source0-md5:	9186bb3ef8aff99e2aef644c946e5d55
Patch0:		%{name}-no_gtk1.patch
URL:		http://dssi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dssi-devel
BuildRequires:	gtk+2-devel
BuildRequires:	liblo-devel >= 0.23
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xsynth-DSSI is a classic-analog (VCOs-VCF-VCA) style software
synthesizer which operates as a plugin for the DSSI Soft Synth
Interface.

Xsynth-DSSI is based on Steve Brooke's Xsynth 1.0.2.

Xsynth-DSSI retains the basic synthesis model of Xsynth, while
adding the following features:
    - operation as a DSSI plugin,
    - polyphonic operation,
    - band-limited oscillators,
    - a new, more stable filter mode, and
    - velocity-sensitive envelopes.

%package gui
Summary:	Graphical interface for Xsynth-DSSI
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui
GTK+ graphical user interface for Xsynth-DSSI.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/dssi/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO ChangeLog
%{_libdir}/dssi/%{name}.so
%dir %{_libdir}/dssi/%{name}
%{_datadir}/%{name}

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dssi/%{name}/*_gtk
