#
# TODO:
#	- build and package the 'tests' (sample programs)
#		should be conditional, as adds BR!
#
# Conditional build:
%bcond_without	mmx		# use MMX instructions
%bcond_without	sse		# use SSE instructions
%bcond_with	tests		# test programs

%ifnarch athlon pentium3 pentium4 %{x8664} x32
%undefine	with_mmx
%endif
%ifnarch pentium3 pentium4 %{x8664} x32
%undefine	with_sse
%endif

Summary:	DSP functions for telephony
Summary(pl.UTF-8):	Funkcje DSP dla telefonii
Name:		spandsp
Version:	0.0.6
Release:	3
Epoch:		1
License:	LGPL v2.1
Group:		Libraries
Source0:	https://www.soft-switch.org/downloads/spandsp/%{name}-%{version}.tar.gz
# Source0-md5:	897d839516a6d4edb20397d4757a7ca3
Patch0:		x32.patch
URL:		https://www.soft-switch.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9.5
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	doxygen
%{?with_tests:BuildRequires:	fftw3-common-devel}
%{?with_tests:BuildRequires:	fftw3-devel}
BuildRequires:	fltk-devel
BuildRequires:	libjpeg-devel
%{?with_tests:BuildRequires:	libpcap-devel}
%{?with_tests:BuildRequires:	libsndfile-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
%{?with_tests:BuildRequires:	libtiff-progs}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
%{?with_tests:BuildRequires:	netpbm-progs}
BuildRequires:	pkgconfig
%{?with_tests:BuildRequires:	sox}
%{?with_tests:BuildRequires:	xorg-lib-libX11-devel}
%{?with_tests:BuildRequires:	xorg-lib-libXext-devel}
%{?with_tests:BuildRequires:	xorg-lib-libXft-devel}
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
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-doc \
	%{?with_mmx:--enable-mmx} \
	%{?with_sse:--enable-sse} \
	%{?with_tests:--enable-tests}
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
%doc AUTHORS ChangeLog DueDiligence NEWS README
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
