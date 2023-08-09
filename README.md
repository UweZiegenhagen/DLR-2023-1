# DLR-2023-1

Public materials for my Advanced LaTeX Course at the DLR


## Course Dates

* Monday, 31.07.2023
* Thursday, 03.08.2023
* Monday, 07.08.2023
* Friday, 11.08.2023

Each date will consist of four hours, most likely from 10--12 and from 13--15.

## Necessary Prior Knowledge

This is not a course for first time users of LaTeX. You should have *some* 
at least basic experience with LaTeX.

## Topics

The final topics will be more or less fixated in the first session, we will
likely cover the following topics during the course.


* Writing letters and CVs
* Creating presentations
* Creating extended bibliographies
* Creating diagrams with TikZ
* Combining LaTeX and computing engines, e.g. Python
* Tables and how to tame them
* ...

From the participants I received the following topics, which I grouped into areas:

### Programming LaTeX

* Designing my own layout (for beamer or other documents) What tools do I need to have? ✓
* What do certain commands mean, like for instance "\makeatletter"? ✓
* Writing loops (like "if ... then ...") ✓
* In general writing more involved environments. Here I know only the basics like 
  \renewcommand or \DeclareMathOperator.
* Writing your own class and packages, and where should I save my own .cls or .sty files 
  so that they are centrally available for all .tex files on my computer?

### Taming LaTeX

* Maybe a more basic question is: How to get rid of "overful \hbox"? ✓
* Is it actually possible to have absolutely no "underfull/overfull hbox" warnings? ✓
* Forcing element (e.g. figure or footnote) positioning to be on specified page
* Using git-latexdiff (instead of latexdiff [options] old.tex new.tex > diff.tex and 
  having to manually download old.tex)
* Strategy when managing a large project: what makes a 'good' LaTeX project? 
  What are the dos-and-dont's (e.g. preamble in separate file, \input and \include, etc.) ?
* Formatting footnotes to be positioned inside the running text at the bottom 
  of the page (i.e. not below text but wrapped within text),
* Space between header numbering and header text
* Change between single column and multiple column style (e.g. abstract in 
  single column, remaining content in twocolumn style)
* Custom abstract (abstract header, indentation, size, etc.) 
* How does LaTeX know stuff?
* Graphics in LaTeX

### Document Types

* Creating presentations, where is the advantage if compared to PowerPoint? ✓


### Bibliographies

* Custom reference and bibliography styles
* bib styles for entries that aren’t yet published
* More on Bibliographies, e.g. in combination with EndNote

### Interactions 

* I am using R for analyses, how can I combine R and LaTeX?
* SQL and LaTeX



## Agenda

### Day 1

* Introduce ourselves ✓
* Curriculum of this course ✓
* Feedback culture: Please provide feedback, you can interrupt 
  me after each sentence. ✓
* Leichter TeXen mit Arara and Autohotkey ✓
* Presentations with LaTeX - Introduction ✓
* Overfull hboxes ✓ (UZ to check this) ✓
* Using git ✓
* Using LuaLaTeX ✓
* Presentations with LaTeX - Design your own Styles ✓

### Day 2

* Q & A for Day 1 ✓
* Creating custom designs for letters ✓
* Conditional typesetting: if/then, looping ✓
* Writing and maintaining your CV ✓
* Matplotlib and system fonts ✓
* LaTeX-Package in Matplotlib: uselatex in Python ✓
* Embedding Source Code ✓
* LaTeX and the rest of the world: Python I ✓
 
 
### Day 3

* Q & A for Day 2 ✓
* Structuring long documents: \input, \include und das subfiles Paket ✓
* Why you should use biblatex ✓
  https://tex.stackexchange.com/questions/87414/per-chapter-bibliographies-in-biblatex
* SVG in LaTeX ✓
* Fun with \write18 ✓
* LaTeX and the rest of the world: R, SQL/Python, etc. II ✓
* TikZ (with standalone) ✓
* Labeling existing graphics in LaTeX ✓
* Matplotlib und siunitx 


### Day 4

* Floats, Graphics and Tables
* Create posters for conferences
* Grafiken nur kompilieren, falls nicht verändert
* subfiles Example
* prettyref und andere Pakete
* citetitle und hyperlinks https://tex.stackexchange.com/questions/108344/biblatexhyperref-citetitle-citeauthor-and-get-hyperlink
* How to write your own package and class
* How to use document class variables
* The "Outer Rim" of LaTeX: What can be done outside the standard?
* Q & A session



