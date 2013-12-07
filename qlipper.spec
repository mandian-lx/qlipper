Summary:	Lightweight clipboard history
Name:		qlipper
Version:	2.0.1
Release:	2
License:	GPLv2
Group:		Text tools
Url:		http://code.google.com/p/qlipper
Source0:	http://qlipper.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:	FindQxt.cmake
Source2:	FindQtSingleApplication.cmake
Patch0:		%{name}-2.0.1-qxt_qtsa.patch
BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	libqxt-devel
BuildRequires:	qtsingleapplication-devel

%description
Lightweight and cross-platform clipboard history applet.

%prep
%setup -q
mkdir cmake
cp %{SOURCE1} cmake
cp %{SOURCE2} cmake
%patch0 -p0
rm -rf qxt qtsingleapplication

%build
%cmake_qt4 -DCMAKE_BUILD_TYPE=release -DUSE_SYSTEM_QXT=ON -DUSE_SYSTEM_QTSINGLEAPPLICATION=ON
%make

%install
%makeinstall_std -C build

install -d -D -m 755 %{buildroot}%{_datadir}/pixmaps
install -d -D -m 755 %{buildroot}%{_iconsdir}

install -D src/icons/%{name}.png %{buildroot}%{_iconsdir}
convert %{buildroot}%{_iconsdir}/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.*
%{_datadir}/pixmaps/%{name}.*

