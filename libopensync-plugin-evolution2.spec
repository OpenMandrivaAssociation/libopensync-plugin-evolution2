%define name	libopensync-plugin-evolution2
%define version	0.33
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Evolution2 plugin for opensync synchronization tool
URL:		http://www.opensync.org
License:	GPL
Group:		Office
Source:		svn://svn.opensync.org/plugins/syncml/%{name}-%{version}.tar.bz2
Obsoletes:	multisync-evolution
Provides:	multisync-evolution
BuildRequires:	opensync-devel >= %{version}
BuildRequires:	evolution-data-server-devel
# fwang: it does not produce devel files anymore
Obsoletes:	%{name}-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}


%description
This plugin allows applications using OpenSync to synchronise to and from
Evolution.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
