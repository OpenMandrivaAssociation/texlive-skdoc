Name:		texlive-skdoc
Version:	56950
Release:	2
Summary:	Documentation and extraction for packages and document classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/skdoc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skdoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skdoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skdoc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides the functionality and implementation of
packages and document classes. It is loosely based on the ydoc
and ltxdoc classes, but has a number of incompatible
differences. The class defines a MacroCode environment which
offers an alternative to the the usual docstrip method of
installing packages. It has the ability to generate both
documentation and code in a single run of a single file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/skdoc
%doc %{_texmfdistdir}/doc/latex/skdoc
#- source
%doc %{_texmfdistdir}/source/latex/skdoc

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
