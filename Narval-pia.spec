Summary:	Personal information assistant
Name:		pia
Version:	20011016	
Release:	1
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{name}-%{version}.npm
License:	GPL
Group:		Applications
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Narval
Url:		http://www.logilab.org/narval/app.html

%description
Pia is an extension set for Narval

It let one set up a personal information assistant that manages
appointments and meetings, contact information, etc.


%description -l pl
Pia to zestaw rozszerze� dla Narval'a

Pozwala na skonfigurowanie osobistego asystenta, kt�ry
zarz�dza spotkaniami, informacjami kontaktowymi itp.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/narval/apps
install %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
