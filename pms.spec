Summary:	Password Manager
Summary(pl):	Zarz±dca hase³
Name:		pms
Version:	0.93a
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://www.8ung.at/easysoft/files/%{name}-%{version}.tar.bz2
Patch0:		%{name}.pld.patch
URL:		http://www.8ung.at/easysoft/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Console program for private password management.

%description -l pl
Konsolowy program do zarz±dzania prywatn± baz± hase³.

%prep
%setup -q
%patch0

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}_passwd/%{name}_passwd $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc NOTES README TODO BUGS CHANGES
