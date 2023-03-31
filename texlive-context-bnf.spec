Name:		texlive-context-bnf
Version:	47085
Release:	2
Summary:	A BNF module for Context
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-bnf
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-bnf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-bnf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The module provides a simple way to write good-looking BNF-
style grammars in ConTeXt. Grammars are written using the BNF
syntax right in your ConTeXt documents, so there is a clear
separation between content and layout. This allows the user to
decide exactly how the grammar is to be displayed, while also
allowing the gist of the grammar to be understood from simply
looking at the source ConTeXt document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/bnf
%doc %{_texmfdistdir}/doc/context/third/bnf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
