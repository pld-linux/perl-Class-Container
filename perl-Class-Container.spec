#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Container
Summary:	Class::Container - glues object frameworks together transparently
Summary(pl):	Class::Container - przezroczyste sklejanie szkieletów obiektów
Name:		perl-Class-Container
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	57bc137f6e167fab10d7173088157d5e
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Params-Validate >= 0.18
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Scalar::Util)'

%description
This class facilitates building frameworks of several classes that
inter-operate. It was first designed and built for "HTML::Mason", in
which the Compiler, Lexer, Interpreter, Resolver, Component, Buffer,
and several other objects must create each other transparently, passing
the appropriate parameters to the right class, possibly substituting
their own subclass for any of these objects.

%description -l pl
Ta klasa u³atwia tworzenie szkieletu dla ró¿nych, wspó³pracuj±cych ze
sob±, klas. Pierwotnie by³a zaprojektowana i stworzona dla
HTML::Mason, w którym Compiler, Lexer, Interpreter, Resolver,
Component, Buffer i kilka innych obiektów musz± tworzyæ inne w sposób
przezroczysty, przekazuj±c odpowiednie parametry do w³a¶ciwej klasy,
byæ mo¿e tak¿e podstawiaj±c swoj± w³asn± podklasê za dowolny z tych
obiektów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# We do not sleep.
%{__perl} -ni -e 'print unless /sleep/' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

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
%{perl_vendorlib}/Class/Container.pm
%{_mandir}/man3/*.3pm*
