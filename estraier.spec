Summary:	estraier - a full-text search engine
Name:		estraier
Version:	1.2.13
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://estraier.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	68c6c3b998270245492e166b0b31a6d8
URL:		http://estraier.sourceforge.net/
BuildRequires:	zlib-devel
BuildRequires:	kakasi-devel
BuildRequires:	chasen-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
estraier is a full-text search system for personal use. Full-text
search means functions to search lots of documents for some documents
including specified words. The principal purpose of Estraier is to
realize a full-text search system of a web site. It functions
similarly to Google, but for a personal web site or sites in an
intranet.

%prep
%setup -q

%build
%configure \
	--libexecdir=%{_libdir}/%{name} \
	--enable-regex \
	--enable-chasen \
	--enable-kakasi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*
