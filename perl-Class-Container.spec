#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Container
Summary:	Class::Container - Glues object frameworks together transparently
Summary(pl):	Class::Container - przezroczyste sklejanie szkieletów obiektów
Name:		perl-%{pdir}-%{pnam}
Version:	0.08
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.005
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Params-Validate >= 0.18
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(Scalar::Util)"

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
perl -ni -e 'print unless /sleep/' Makefile.PL

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Class/Container.pm
%{_mandir}/man3/*.3pm*
