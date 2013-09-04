Name:		qlipper
Version: 	2.0.1
Release: 	1
License:	GPLv2
Source0:	http://qlipper.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:	FindQxt.cmake
Source2:	FindQtSingleApplication.cmake
Patch0:		%{name}-2.0.1-qxt_qtsa.patch
URL:		http://code.google.com/p/qlipper
Group:		Text tools
Summary:	Lightweight clipboard history
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	cmake
BuildRequires:	libqxt-devel
BuildRequires:	imagemagick

%description
Lightweight and cross-platform clipboard history applet.

%prep
%setup -q
mkdir cmake
cp %{SOURCE1} cmake
cp %{SOURCE2} cmake
%patch0 -p0
%{__rm} -rf qxt qtsingleapplication

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
