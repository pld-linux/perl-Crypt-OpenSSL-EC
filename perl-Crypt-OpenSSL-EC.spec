#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-EC
Summary:	Crypt::OpenSSL::EC - Perl extension for OpenSSL EC (Elliptic Curves) library
Summary(pl.UTF-8):	Crypt::OpenSSL::EC - moduł Perla do obliczeń na krzywych eliptycznych
Name:		perl-Crypt-OpenSSL-EC
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	742f192f26bcac2249017cdd9e8bac35
URL:		http://search.cpan.org/dist/Crypt-OpenSSL-EC/
BuildRequires:	openssl-devel >= 0.9.8i
BuildRequires:	perl-Crypt-OpenSSL-Bignum >= 0.04
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a standard (non-OO) interface to the OpenSSL EC
(Elliptic Curve) library. Some OO Calls are supported.
Most of the functions described in openssl/ec.h are supported.
It provides the Crypt::OpenSSL::EC class which defines some high level
functions and constants.

%description -l pl.UTF-8
Ten moduł dostarcza nieobiektowy interfejs programistyczny do
obliczeń na krzywych eliptycznych z blbioteki OpenSSL.
Dostępna jest wiekszość funkcji opisanych w pliku openssl/ec.h.
Klasa Crypt::OpenSSL::EC definiuje trochę wysokopoziomowych funkcji
i stałych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/OpenSSL/EC.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/EC
%{perl_vendorarch}/auto/Crypt/OpenSSL/EC/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/EC/*.so
%{_mandir}/man3/Crypt::OpenSSL::EC.3pm*