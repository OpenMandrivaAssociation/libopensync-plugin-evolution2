Name: 	 	libopensync-plugin-evolution2
Version: 	0.22
Epoch:		1
Release: 	%{mkrel 5}
Summary: 	Evolution plugin for OpenSync synchronization framework
URL:		http://www.opensync.org
License:	LGPLv2+
Group:		Office
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
# Don't use -Wall and -Werror - AdamW 2008/03
Patch0:		libopensync-plugin-evolution2-0.22-warning.patch
Obsoletes:	multisync-evolution
Provides:	multisync-evolution
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	evolution-data-server-devel
BuildRequires:	dbus-glib-devel
Requires:	libopensync >= %{epoch}:%{version}
Requires:	evolution
BuildRoot:	%{_tmppath}/%{name}-%{version}
Obsoletes:	%{name}-devel <= %{version}-%{release}

%description
This plugin allows applications using OpenSync to synchronise to and from
Evolution.

%prep
%setup -q
%patch0 -p1 -b .warning

%build
autoreconf -i
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}%{_includedir}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*

