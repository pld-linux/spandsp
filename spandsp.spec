Summary:	DSP functions for telephony
Summary(pl.UTF-8):   Funkcje DSP dla telefonii
Name:		spandsp
# do not upgrade to 0.0.3 series until it's stable
%define	_pre	pre26
Version:	0.0.2
Release:	0.%{_pre}.1
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://soft-switch.org/downloads/spandsp/%{name}-%{version}%{_pre}/%{name}-%{version}%{_pre}.tar.gz
# Source0-md5:	2b28a75b1d7c49616534bd7264317241
Patch0:		%{name}-nommx.patch
URL:		http://www.soft-switch.org/
BuildRequires:	audiofile-devel
BuildRequires:	automake
BuildRequires:	fftw-devel
BuildRequires:	fltk-devel
BuildRequires:	libtiff-devel
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
Summary(pl.UTF-8):   Pliki nagłówkowe do tworzenia aplikacji używających spandsp
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for the spandsp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki spandsp.

%package static
Summary:	Static spandsp library
Summary(pl.UTF-8):   Statyczna biblioteka spandsp
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static spandsp library.

%description static -l pl.UTF-8
Statyczna biblioteka spandsp.

%prep
%setup -q
%patch0 -p1

%build
install /usr/share/automake/config.* config
%configure
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
