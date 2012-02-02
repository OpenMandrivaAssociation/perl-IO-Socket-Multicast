%define	module	IO-Socket-Multicast
%define	upstream_version 1.12

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Send and receive multicast messages
License;	GPL+ or Artistic
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

