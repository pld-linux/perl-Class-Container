# $Revision: 1.1 $
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Container
Summary:	%{pdir}::%{pnam} perl module
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Name:		perl-%{pdir}-%{pnam}
Version:	0.05
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005
#BuildRequires:	perl(Params::Validate) >= 0.18
BuildRequires:	perl-Params-Validate >= 0.18
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

# %description -l pl
# TODO


%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# We do not sleep.
perl -ni -e 'print unless /sleep/' Makefile.PL

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Class/Container.pm
%{_mandir}/man3/*.3pm.gz
