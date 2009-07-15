%define upstream_name    IO-Socket-Multicast
%define upstream_version 1.07

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Send and receive multicast messages
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source:         http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-devel
BuildRequires:  perl(IO::Interface)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
IO::Socket::Multicast is designed to take the effort out of managing
some multicast network.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

