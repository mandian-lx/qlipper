Summary:	Lightweight clipboard history
Name:		qlipper
Version:	5.0.0
Release:	1
License:	GPLv2
Group:		Text tools
Url:		https://github.com/pvanek/qlipper
Source0:	https://github.com/pvanek/qlipper/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  imagemagick
#BuildRequires:	libqxt-devel
BuildRequires:  pkgconfig(ice)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(xext)
BuildRequires:	qmake5
BuildRequires:	qtsingleapplication-devel

%description
Lightweight and cross-platform clipboard history applet.

%files -f %{name}.lang
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.*

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

# remove unudes bundled libs
rm -rf qtsingleapplication #qxt

%build
%cmake_qt5 \
    -DUSE_SYSTEM_QTSINGLEAPPLICATION=ON \
    -DUSE_SYSTEM_QXT=OFF \
    %{nil}
%make

%install
%makeinstall_std -C build

# icons
for d in 16 32 48 64 72 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -background none -resize "${d}x${d}" src/icons/%{name}.png \
		%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
#   pixmap
install -dm 0755 %{buildroot}%{_datadir}/pixmaps
convert -background none -resize "32x32" src/icons/%{name}.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# locales
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

