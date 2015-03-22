#
# TODO:
#	- build and package the 'tests' (sample programs)
#		should be conditional, as adds BR!
#
%define	subver	pre20
%define	rel	2
Summary:	DSP functions for telephony
Summary(pl.UTF-8):	Funkcje DSP dla telefonii
Name:		spandsp
Version:	0.0.6
Release:	0.%{subver}.%{rel}
Epoch:		1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://www.soft-switch.org/downloads/spandsp/%{name}-%{version}%{subver}.tgz
# Source0-md5:	9bdf1d027f1b5dc5e622d707fa1634cb
URL:		http://www.soft-switch.org/
#audiofile-devel may be superfluous !
#BuildRequires:	audiofile-devel
BuildRequires:	automake
# AUTO: -- ../t38_manual.xml:3: warning: failed to load external entity "http://www.oasis-open.org/docbook/xml/4.3/docbookx.dtd"
BuildRequires:	docbook-dtd43-xml
# AUTO: -- warning: failed to load external entity "http://docbook.sourceforge.net/release/xsl/current/xhtml/chunk.xsl"
BuildRequires:	docbook-style-xsl
BuildRequires:	doxygen
#fftw-devel may be superfluous !
#BuildRequires:	fftw-devel
# AUTO: -- conftest.c:106:19: fatal error: fftw3.h: No such file or directory
BuildRequires:	fftw3-common-devel
# AUTO: -- /usr/bin/ld: cannot find -lfftw3
BuildRequires:	fftw3-devel
# AUTO: -- conftest.cc:111:19: fatal error: FL/Fl.H: No such file or directory
BuildRequires:	fltk-devel
# AUTO: -- configure:5457: checking for x86_64-pld-linux-gfortran
BuildRequires:	gcc-fortran
# AUTO: -- /usr/bin/ld: cannot find -lpcap
BuildRequires:	libpcap-devel
# AUTO: -- /usr/bin/ld: cannot find -lsndfile
BuildRequires:	libsndfile-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
spandsp is a library which provides many of the DSP functions needed
for telephony. It is designed to be independent of the telephony
platform itself.

%description -l pl.UTF-8
spandsp to biblioteka udostępniająca wiele funkcji DSP potrzebnych dla
telefonii. Jest zaprojektowana tak, by była niezależna od samej
platformy telefonicznej.

%package devel
Summary:	Header files to develop applications using spandsp
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji używających spandsp
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libtiff-devel

%description devel
Header files for the spandsp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki spandsp.

%package static
Summary:	Static spandsp library
Summary(pl.UTF-8):	Statyczna biblioteka spandsp
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static spandsp library.

%description static -l pl.UTF-8
Statyczna biblioteka spandsp.

%prep
%setup -q

%build
install /usr/share/automake/config.* config
%configure \
	--disable-tests \
%ifarch athlon pentium3 pentium4
	--enable-mmx \
%endif
%ifarch pentium3 pentium4
	--enable-sse \
%endif
	--enable-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libspandsp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspandsp.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspandsp.so
%{_libdir}/libspandsp.la
%{_includedir}/spandsp
%{_includedir}/spandsp.h
%{_pkgconfigdir}/spandsp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libspandsp.a
