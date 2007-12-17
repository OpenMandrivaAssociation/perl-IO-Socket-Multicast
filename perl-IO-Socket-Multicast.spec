%define module  IO-Socket-Multicast
%define name    perl-%{module}
%define version 1.05
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Send and receive multicast messages
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/IO/%{module}-%{version}.tar.bz2
BuildRequires:  perl-devel

%description
IO::Socket::Multicast is designed to take the effort out of managing
some multicast network.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README 
%{perl_vendorarch}/IO
%{perl_vendorarch}/auto/IO
%{_mandir}/man*/*

