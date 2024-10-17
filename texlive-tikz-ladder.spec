Name:		texlive-tikz-ladder
Version:	62992
Release:	2
Summary:	Draw ladder diagrams using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tikz-ladder
License:	lppl1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-ladder.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-ladder.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tikz-ladder package contains a collection of symbols for
typesetting ladder diagrams (PLC program) in agreement with the
international standard IEC-61131-3/2013. It includes blocks
(for representing functions and function blocks) besides
contacts and coils. It extends the circuit library of TikZ and
allows you to draw a ladder diagram in the same way as you
would draw any other circuit.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-ladder
%doc %{_texmfdistdir}/doc/latex/tikz-ladder

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
