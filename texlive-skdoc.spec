%global tl_name skdoc
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5e
Release:	%{tl_revision}.1
Summary:	Documentation and extraction for packages and document classes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/skdoc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skdoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skdoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class provides the functionality and implementation of packages and
document classes. It is loosely based on the ydoc and ltxdoc classes,
but has a number of incompatible differences. The class defines a
MacroCode environment which offers an alternative to the usual docstrip
method of installing packages. It has the ability to generate both
documentation and code in a single run of a single file.

