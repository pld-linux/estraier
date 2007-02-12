# TODO:
# - --with-sysqdbm
#
# Conditional build:
%bcond_without	chasen		# build without chasen, Japanese Morphological Analysis System.
%bcond_without	kakasi		# build without kakasi, kanji kana simple inverter
#
Summary:	estraier - a full-text search engine
Summary(pl.UTF-8):	estraier - silnik przeszukiwania pełnotekstowego
Name:		estraier
Version:	1.2.28
Release:	1.2
License:	GPL
Group:		Applications/Text
Source0:	http://estraier.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	f099d80e5ad03cb6255db0397225a069
URL:		http://estraier.sourceforge.net/
%{?with_chasen:BuildRequires:	chasen-devel}
%{?with_kakasi:BuildRequires:	kakasi-devel}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
estraier is a full-text search system for personal use. Full-text
search means functions to search lots of documents for some documents
including specified words. The principal purpose of Estraier is to
realize a full-text search system of a web site. It functions
similarly to Google, but for a personal web site or sites in an
intranet.

%description -l pl.UTF-8
estraier to system przeszukiwania pełnotekstowego do użytku
własnego. Przeszukiwanie pełnotekstowe oznacza funkcje do szukania w
dużej liczbie dokumentów pewnych dokumentów zawierających określone
słowa. Zasadniczym celem Straiera jest realizacja systemu
przeszukiwania pełnotekstowego dla serwisu WWW. Działa podobnie do
Google, ale dla własnej strony lub w intranecie.

%prep
%setup -q

%build
%configure \
	--libexecdir=%{_libdir}/%{name} \
	--enable-regex \
	%{?with_chasen:--enable-chasen} \
	%{?with_kakasi:--enable-kakasi} \
	--enable-dlfilter \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install estfind $RPM_BUILD_ROOT%{_bindir}

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
