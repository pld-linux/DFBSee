Summary:	DirectFBSee - an image viewer and video player for the Linux framebuffer
Summary(pl):	DirectFBSee - przegl±darka obrazków i filmów dla linuksowego framebuffera
Name:		DFBSee
Version:	0.7.4
Release:	4
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.directfb.org/download/DFBSee/%{name}-%{version}.tar.gz
# Source0-md5:	3320a976457d3b3e9eaef530fdf56b37
Patch0:		%{name}-API-fix.patch
URL:		http://www.directfb.org/index.php?path=Development/Projects/DFBSee
BuildRequires:	DirectFB-devel >= 0.9.15
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
Requires:	DirectFB-font-ft2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectFBSee is an image viewer and video player for the Linux
framebuffer. dfbsee opens the specified file and tries the image and
video providers available with DirectFB. At the moment these are PNG,
JPEG, GIF and MPEG or a Video4Linux video device.

%description -l pl
DirectFBSee to przegl±darka obrazków i filmów dla linuksowego
framebuffera. dfbsee otwiera podany plik i próbuje dostêpnych modu³ów
dostarczaj±cych grafikê i obraz DirectFB. Aktualnie s± to PNG, JPEG,
GIF oraz MPEG lub urz±dzenie Video4Linux.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
