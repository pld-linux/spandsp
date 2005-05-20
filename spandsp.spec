Summary:	DSP functions for telephony
Summary(pl):	Funkcje DSP dla telefonii
Name:		spandsp
%define	_pre	pre18
Version:	0.0.2
Release:	0.%{_pre}.1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.opencall.org/pub/spandsp/%{name}-%{version}%{_pre}/%{name}-%{version}%{_pre}.tar.gz
# Source0-md5:	b01f2fdd47f30b0b80343ed2f75a7199
URL:		http://www.soft-switch.org/
BuildRequires:	audiofile-devel
BuildRequires:	libtiff-devel
BuildRequires:	fftw-devel
BuildRequires:	fltk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
spandsp is a library which provides many of the DSP functions needed
for telephony. It is designed to be independent of the telephony
platform itself.

%description -l pl
spandsp to biblioteka udostêpniaj±ca wiele funkcji DSP potrzebnych dla
telefonii. Jest zaprojektowana tak, by by³a niezale¿na od samej
platformy telefonicznej.

%package devel
Summary:	Header files to develop applications using spandsp
Summary(pl):	Pliki nag³ówkowe do tworzenia aplikacji u¿ywaj±cych spandsp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the spandsp library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki spandsp.

%package static
Summary:	Static spandsp library
Summary(pl):	Statyczna biblioteka spandsp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static spandsp library.

%description static -l pl
Statyczna biblioteka spandsp.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
