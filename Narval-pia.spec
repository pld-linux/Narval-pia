%define short_name pia

Summary:	Personal information assistant
Summary(pl):	Asystent informacji osobistych
Name:		Narval-%{short_name}
Version:	20011016	
Release:	1
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
URL:		http://www.logilab.org/narval/app.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Narval

%description
Pia is an extension set for Narval.

It let one set up a personal information assistant that manages
appointments and meetings, contact information, etc.

%description -l pl
Pia to zestaw rozszerzeñ dla Narval-a.

Pozwala na skonfigurowanie osobistego asystenta, który zarz±dza
spotkaniami, informacjami kontaktowymi itp.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/narval/apps
install %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
