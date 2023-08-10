\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{uweziegenhagen}[2023/07/30 Meine eigene Klasse]

\renewcommand\normalsize{%
   \@setfontsize\normalsize{10.5pt}{12pt}
   \abovedisplayskip 10\p@ \@plus2\p@ \@minus5\p@
   \abovedisplayshortskip \z@ \@plus3\p@
   \belowdisplayshortskip 6\p@ \@plus3\p@ \@minus3\p@
   \belowdisplayskip \abovedisplayskip
   \let\@listi\@listI}\normalsize

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\newcommand{\hello}{Hallo Welt}


