Summary:	IRC Info/Search/Relay bot
Summary(pl.UTF-8):	Ircowy bot informacyjno-wyszukująco-przekazujący
Name:		pynfo
Version:	0.6.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/sourceforge/pynfo/%{name}-%{version}.tar.bz2
# Source0-md5:	773c5f4fd78197c26d27256ff1a94a83
URL:		https://sourceforge.net/projects/pynfo/
BuildRequires:	python-Twisted
BuildRequires:	python-Crypto
BuildRequires:	/usr/bin/python
Requires:	python-Twisted
Requires:	python-Crypto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pynfo is a combination IRC infobot, search bot, and network relay. It
supports basic fact definition (with persistence between runs),
searching of Google and Freshmeat. As a network relay, it can "bridge"
channels on multiple networks - that is, pass messages between them.
It also has a plugin interface, allowing users to easily define new
commands.

%description -l pl.UTF-8
Pynfo to połączenie ircowego bota informacyjnego, bota wyszukującego i
przekaźnika sieciowego. Obsługuje podstawowe definiowanie okoliczności
(z zachowywaniem między uruchomieniami), przeszukiwanie Google i
Freshmeata. Jako przekaźnik sieciowy może łączyć kanały w wielu
sieciach - czyli przekazywać komunikaty między nimi. Ma także
interfejs do wtyczek, co pozwala użytkownikom na łatwe definiowanie
nowych poleceń.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python -c "import twisted; import Crypto"
python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO ChangeLog README
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/Pynfo
%{py_sitedir}/Pynfo/*.py[co]
%{py_sitedir}/Pynfo/*.tml
%dir %{py_sitedir}/Pynfo/plugins
%{py_sitedir}/Pynfo/plugins/*.py[co]
%{py_sitedir}/Pynfo/plugins/*.tml
