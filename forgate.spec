Summary:	A Packet Redirection Tool For Interception On Switched Networks
Summary(pl):	Narz�dzie przechwytuj�ce pakiety w sieciach opartych na switchach
Name:		forgate
Version:	0.9
Release:	1
License:	GPL	
Vendor:		Darren Bounds <dbounds@intrusense.com>
Group:		Applications/Network
Source0:	http://forgate.sourceforge.net/downloads/%{name}-%{version}.tgz
# Source0-md5:	b5455f0c83547769bd486877362f9553
Patch0:		%{name}-bpf.patch
URL:		http://forgate.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnet-devel >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Forgate was written as a proof of concept in one method of capturing
traffic flows from a 3rd party on a switched network. Forgate uses ARP
cache poisoning, packet capture and packet reconstruction to perform
its task. It should work with nearly all TCP, ICMP and UDP IPv4
traffic.

%description -l pl
Forgate zosta�o napisane jako dow�d dzia�ania jednej z metod
przechwytywania pakiet�w z innych komputer�w w sieci opartej na
switchach. Do wykonania zadania u�ywa zatruwania cache ARP,
przechwytywania pakiet�w oraz rekonstrukcji pakiet�w. Powinno dzia�a�
z prawie ka�dym ruchem IPV4 TCP, ICMP i UDP.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_sbindir}/*
