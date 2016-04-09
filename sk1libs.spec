Name:		sk1libs
Version:	0.9.1
Release:	4
Summary:	Set of Python Non-GUI Extensions for sK1 Project
License:	GPLv2+ and LGPLv2+
Group:		Graphics
URL:		http://sk1project.org/
Source0:	http://sk1project.org/downloads/%{name}/%{name}-%{version}.tar.gz
# Fix / kludge for Tcl 8.6 (good old interp->result) - AdamW 2008/12
Patch0:		sk1libs-math-fix.diff
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(zlib)
Requires:	python2-imaging


%description
sk1libs is a set of python non-GUI extensions for sK1 Project. The package
includes multiplatform non-GUI extensions which are usually native extensions.

%prep
%setup -q
%patch0 -p1 -b .mfix
sed -i -e 's,tcl8.5,tcl%{tcl_version},g' setup.py
sed -i -e 's,tk8.5,tk%{tcl_version},g' setup.py

%build
%{__python2} ./setup.py build

%install
rm -fr %{buildroot}
%{__python2} setup.py install --root=%{buildroot} --compile --optimize=2


%files
%{py2_platsitedir}/*
