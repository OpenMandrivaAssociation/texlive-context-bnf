# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-bnf
# catalog-date 2008-08-18 23:54:09 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-bnf
Version:	20080818
Release:	7
Summary:	A BNF module for Context
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-bnf
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-bnf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-bnf.doc.tar.xz
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
%{_texmfdistdir}/tex/context/third/bnf/t-bnf.tex
%doc %{_texmfdistdir}/doc/context/third/bnf/NEWS
%doc %{_texmfdistdir}/doc/context/third/bnf/README
%doc %{_texmfdistdir}/doc/context/third/bnf/t-bnf.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080818-2
+ Revision: 750489
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080818-1
+ Revision: 718124
- texlive-context-bnf
- texlive-context-bnf
- texlive-context-bnf
- texlive-context-bnf

