\NeedsTeXFormat{LaTeX2e}[2022-06-01]
\ProvidesClass{uweziegenhagen}[2023-08-11]

\RequirePackage{xcolor}

\DeclareKeys{
color.code = \colorlet{foocol}{#1},
val.store = \fooval
}


\SetKeys{
color =black,
val=0
}

\ProcessKeyOptions

\setlength\textwidth{6cm}
\setlength\textheight{8cm}

\renewcommand\normalsize{\fontsize{10}{12}\selectfont}

