%global tl_name tikz-ladder
%global tl_revision 62992

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Draw ladder diagrams using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-ladder
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-ladder.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-ladder.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The tikz-ladder package contains a collection of symbols for typesetting
ladder diagrams (PLC program) in agreement with the international
standard IEC-61131-3/2013. It includes blocks (for representing
functions and function blocks) besides contacts and coils. It extends
the circuit library of TikZ and allows you to draw a ladder diagram in
the same way as you would draw any other circuit.

