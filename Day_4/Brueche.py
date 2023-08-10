import os
import random

 
head = """
\\documentclass[14pt, twocolumn]{scrartcl}
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}
\\pagestyle{empty}
 
\\begin{document}
 
\\begin{itemize}"""
 
foot = """
\\end{itemize}
\\end{document}
"""
 
def create_bruch():
    zahlen = list(range(1,13))
    zaehler = random.choice(zahlen)
    zahlen.remove(zaehler)
    nenner = random.choice(zahlen)
    return '\\item \\( \\frac{'+ str(zaehler) + '}{' + str(nenner) + '} \\)\\vspace{1em}'
 
 
with open("Brueche.tex", "w") as document:
    document.write(head);
    for i in range(30):
        document.write(create_bruch());
    document.write(foot);
    document.close();
 
os.system("pdflatex Brueche.tex")
os.unlink("Brueche.log")
os.unlink("Brueche.aux")
os.unlink("Brueche.tex")