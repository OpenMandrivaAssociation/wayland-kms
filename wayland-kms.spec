%define major 0
%define libname %mklibname wayland-kms
%define devname %mklibname wayland-kms -d

Name: wayland-kms
Version: 1.6.0
Release: 2
Source0: https://github.com/renesas-rcar/wayland-kms/archive/refs/heads/rcar-gen3.tar.gz
Summary: Wayland module for running on KMS devices
URL: https://github.com/renesas-rcar/wayland-kms
License: GPL
Group: System/Libraries
BuildRequires: autoconf automake make
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(egl)

%description
Wayland module for running on KMS devices

%package -n %{libname}
Summary: Wayland module for running on KMS devices
Group: System/Libraries

%description -n %{libname}
Wayland module for running on KMS devices

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n %{name}-rcar-gen3
autoheader
%configure

%build
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
