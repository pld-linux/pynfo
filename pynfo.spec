Summary:	IRC Info/Search/Relay bot
Summary(pl):	Ircowy bot informacyjno-wyszukuj±co-przekazuj±cy
Name:		pynfo
Version:	0.6.2
Release:	1
License:	GPL
Group:          Applications/Communications
Source0:	http://heanet.dl.sourceforge.net/sourceforge/pynfo/%{name}-%{version}.tar.bz2
URL:		https://sourceforge.net/projects/pynfo/	
BuildRequires:  python-Twisted
BuildRequires:  python-Crypto
BuildRequires:  /usr/bin/python
Requires:	python-Twisted
Requires:       python-Crypto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pynfo is a combination IRC infobot, search bot, and network relay. It
supports basic fact definition (with persistence between runs),
searching of Google and Freshmeat. As a network relay, it can "bridge"
channels on multiple networks - that is, pass messages between them.
It also has a plugin interface, allowing users to easily define new
commands.

%description -l pl
Pynfo to po³±czenie ircowego bota informacyjnego, bota wyszukuj±cego i
przeka¼nika sieciowego. Obs³uguje podstawowe definiowanie okoliczno¶ci
(z zachowywaniem miêdzy uruchomieniami), przeszukiwanie Googli i
Freshmeata. Jako przeka¼nik sieciowy mo¿e ³±czyæ kana³y w wielu
sieciach - czyli przekazywaæ komunikaty miêdzy nimi. Ma tak¿e
interfejs do wtyczek, co pozwala u¿ytkownikom na ³atwe definiowanie
nowych poleceñ.

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
