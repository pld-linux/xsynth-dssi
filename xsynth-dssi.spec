Summary:	Software synthesizer plugin for the DSSI Soft Synth Interface
Summary(pl.UTF-8):	Wtyczka programowego syntezatora dla interfejsu DSSI Soft Synth Interface
Name:		xsynth-dssi
Version:	0.9.4
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/dssi/%{name}-%{version}.tar.gz
# Source0-md5:	3432ecdac06407a992f80eb1c1ecf7cd
Patch0:		%{name}-no_gtk1.patch
URL:		http://dssi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dssi-devel >= 0.9
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	ladspa-devel
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

%description -l pl.UTF-8
Xsynth-DSSI to programowy syntezator w stylu klasyczno-analogowym
(VCOs-VCF-VCA), działający jako wtyczka dla interfejsu DSSI Soft
Synth Interface.

Xsynth-DSSI jest oparty na programie XSynth 1.0.2 Steve'a Brooke'a.

Xsynth-DSSI zachowuje podstawowy model syntezy z Xsynth, dodając
jednocześnie następujące możliwości:
 - działanie jako wtyczka DSSI,
 - praca polifoniczna,
 - oscylatory z ograniczonym zakresem,
 - nowy, stabilniejszy tryb filtra,
 - obudowanie wrażliwe na szybkość.

%package gui
Summary:	Graphical interface for Xsynth-DSSI
Summary(pl.UTF-8):	Graficzny interfejs do Xsynth-DSSI
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui
GTK+ graphical user interface for Xsynth-DSSI.

%description gui -l pl.UTF-8
Oparty na GTK+ graficzny interfejs użytkownika do Xsynth-DSSI.

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/dssi/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO ChangeLog
%attr(755,root,root) %{_libdir}/dssi/%{name}.so
%dir %{_libdir}/dssi/%{name}
%{_datadir}/%{name}

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dssi/%{name}/*_gtk
