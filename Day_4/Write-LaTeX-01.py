# -*- coding: utf-8 -*-

# write LaTeX file and execute it
import os
from datetime import datetime
now = datetime.now()

time = now.strftime("%H:%M:%S")

with open('HalloWelt.tex','w') as o:
    o.write('\\documentclass{scrartcl}\n')
    o.write('\\begin{document}\n')
    o.write(f'Hallo {time}\n')
    o.write('\\end{document}\n')

try:
    result = os.system('pdflatex -interaction=batchmode HalloWelt.tex')
except Exception as e:
    print(e)