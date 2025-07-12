Summary:	A Wayland window-stacking compositor
Name:		labwc
Version:	0.9.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://github.com/labwc/labwc/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5baaddbd9fe7d14179e11c3cd8b0e851
URL:		https://labwc.github.io
BuildRequires:	cairo-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	libdrm-devel
BuildRequires:	libinput-devel >= 1.14
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.46
BuildRequires:	libsfdo-devel >= 0.1.3
BuildRequires:	libxcb-devel
BuildRequires:	libxml2-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pango-devel
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc
BuildRequires:	wayland-devel >= 1.19.0
BuildRequires:	wayland-protocols >= 1.39
BuildRequires:	wlroots0.19-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xorg-xserver-Xwayland-devel >= 21.1.9
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libinput >= 1.14
Requires:	librsvg >= 2.46
Requires:	libsfdo >= 0.1.3
Requires:	wayland >= 1.19.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Labwc is a wlroots-based window-stacking compositor for wayland,
inspired by openbox.

It is light-weight and independent with a focus on simply stacking
windows well and rendering some window decorations. It takes a
no-bling/frills approach and says no to features such as animations.
It relies on clients for panels, screenshots, wallpapers and so on to
create a full desktop environment.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}/{README,autostart,environment,menu.xml,rc.xml,rc.xml.all,shutdown,themerc}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CONTRIBUTING.md NEWS.md README.md docs/{autostart,environment,menu.xml,rc.xml,rc.xml.all,shutdown,themerc}
%attr(755,root,root) %{_bindir}/labwc
%attr(755,root,root) %{_bindir}/lab-sensible-terminal
%{_iconsdir}/hicolor/scalable/apps/labwc*.svg
%{_mandir}/man1/labwc.1*
%{_mandir}/man5/labwc-*.5*
%{_datadir}/wayland-sessions/labwc.desktop
%{_datadir}/xdg-desktop-portal/labwc-portals.conf
