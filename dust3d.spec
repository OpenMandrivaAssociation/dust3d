Summary:	Dust3D 3D modeling software
Name:		dust3d
Version:	1.0.0
Release:	1
License:	MIT
Url:		https://dust3d.org/
Source0:	https://github.com/huxingyi/dust3d/archive/dust3d-%{version}-beta.21.tar.gz

BuildRequires:	qmake5
BuildRequires:	cmake(CGAL)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libglvnd)

%description
Dust3D is a brand new 3D modeling software. It helps you create a 3D watertight model in seconds. Use it to speed up your character modeling in game making, 3D printing, and so on.


%prep
%setup -qn %{name}-%{version}-beta.21

%build
%qmake_qt5
%make_build

%install
mkdir -p %{buildroot}%{_bindir}/ %{buildroot}%{_datadir}/applications/
install -m 0755 %{name} %{buildroot}%{_bindir}/
install -m 0644 ci/dust3d.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
