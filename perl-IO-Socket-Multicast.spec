%define	module	IO-Socket-Multicast
%define	upstream_version 1.12

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Send and receive multicast messages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/IO/%{module}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Interface)

%description
IO::Socket::Multicast is designed to take the effort out of managing
some multicast network.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README 
%{perl_vendorarch}/IO
%{perl_vendorarch}/auto/IO
%{_mandir}/man*/*



%changelog
* Thu Feb 02 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.120.0-3
+ Revision: 770586
- clean up spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 552324
- update to 1.12

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.1
+ Revision: 461297
- update to 1.11

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 396357
- adding missing buildrequires:
- wrongly changed extension
- adding missing buildrequires:
- using %%perl_convert_version

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.07

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.05-5mdv2009.0
+ Revision: 257316
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.05-3mdv2008.1
+ Revision: 152121
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-2mdv2008.0
+ Revision: 86509
- rebuild


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2007.0
- New version 1.05
- spec cleanup
- better summary
- drop explicit provides

* Thu Jun 22 2006 Erwan Velu <erwan@seanodes.com> 1.04-3
- Rebuild

* Mon Feb 20 2006 Erwan Velu <erwan@seanodes.com> 1.04-2mdk
- Wrong spec name

* Mon Feb 06 2006 Erwan Velu <erwan@seanodes.com> 1.04-1mdk
- 1.04

