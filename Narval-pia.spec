%define short_name pia

Summary:	Personal information assistant
Summary(pl):	Asystent informacji osobistych
Name:		Narval-%{short_name}
Version:	20011016	
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
# Source0-md5:	2e1a3f673a82637c1d6acfeadea13d9c
URL:		http://www.logilab.org/narval/app.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Narval

%description
Pia is an extension set for Narval.

It let one set up a personal information assistant that manages
appointments and meetings, contact information, etc.

%description -l pl
Pia to zestaw rozszerzeñ dla Narvala.

Pozwala na skonfigurowanie osobistego asystenta, który zarz±dza
spotkaniami, informacjami kontaktowymi itp.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/narval/apps/%{short_name}-%{version}.npm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
