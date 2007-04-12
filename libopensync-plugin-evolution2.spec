%define name	libopensync-plugin-evolution2
%define version	0.20
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Evolution2 plugin for opensync synchronization tool
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.gz
URL:		http://www.opensync.org
License:	GPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel >= %{version}
BuildRequires:	evolution-data-server-devel

Obsoletes:	multisync-evolution
Provides:	multisync-evolution

%description
This plugin allows applications using OpenSync to synchronise to and from
Evolution.

%package	devel
Summary:        Header files from %name
Group:          Development/C

%description 	devel
Header files for developing programs based on %name.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*

%files devel
%defattr(-,root,root)
%{_includedir}/opensync-1.0/opensync/*


