%define upstream_name    asa
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Lets your class/object say it works like something else
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(base)
BuildArch:	noarch

%description
Perl 5 doesn't natively support Java-style interfaces, and it doesn't
support Perl 6 style roles either.

You can get both of these things in half a dozen different ways via various
CPAN modules, but they usually require that you buy into "their way" of
implementing your code.

Other have turned to "duck typing".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 685620
- update to new version 1.03

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2
+ Revision: 653626
- rebuild for updated spec-helper

* Wed Jul 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 562790
- import perl-asa


* Fri Feb 05 2010 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
