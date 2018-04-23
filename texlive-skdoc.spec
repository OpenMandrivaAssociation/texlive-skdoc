# revision 32278
# category Package
# catalog-ctan /macros/latex/contrib/skdoc
# catalog-date 2013-11-28 23:56:30 +0100
# catalog-license lppl1.3
# catalog-version 1.4a
Name:		texlive-skdoc
Version:	1.5a
Release:	1
Summary:	Documentation and extraction for packages and document classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/skdoc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skdoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skdoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skdoc.source.tar.xz
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
%{_texmfdistdir}/tex/latex/skdoc/skdoc.cls
%doc %{_texmfdistdir}/doc/latex/skdoc/README
%doc %{_texmfdistdir}/doc/latex/skdoc/skdoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/skdoc/skdoc.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
