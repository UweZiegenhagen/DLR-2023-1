# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:36:05 2023

@author: Uwe

Fehler


File C:\Python311\Lib\site-packages\matplotlib\backends\backend_pgf.py:358 in

ValueError: Error measuring \rmfamily\fontsize{10.000000}{12.000000}\selectfont \(\displaystyle \mu=100,\ \sigma=15\) \SI{1132156465}{\second\­per\meter}
LaTeX Output:
! Undefined control sequence.
<argument> \second \­
           per\meter 
<*> ...gma=15\) \SI{1132156465}{\second\­per\meter}}
                                                  \typeout{\the\wd0,\the\ht0...

 867 words of node memory still in use:
   6 hlist, 2 rule, 2 dir, 4 math, 14 glue, 8 kern, 1 penalty, 31 glyph, 14 att
ribute, 52 glue_spec, 14 attribute_list, 1 temp, 1 write, 3 pdf_colorstack node
s
   avail lists: 2:4,3:10,4:1,5:2,8:10,9:1,11:1
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on texput.log.




"""


## https://stackoverflow.com/questions/60140070/how-to-put-pgf-preamble-into-an-mplstyle-style
## https://stackoverflow.com/questions/76371558/matplotlib-pgf-backend-adjusting-preamble


import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np


pgf_with_latex = {                      # setup matplotlib to use latex for output
    "pgf.texsystem": "lualatex",        # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    #"font.family": "serif",
    "font.serif": ['LM Roman 10'],                   # blank entries should cause plots 
    "font.sans-serif": ['LM Roman 10'],              # to inherit fonts from the document
    "font.monospace": ['LM Roman 10'],
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "font.size": 10,
    "legend.fontsize": 8,               # Make the legend/label fonts 
    "xtick.labelsize": 8,               # a little smaller
    "ytick.labelsize": 8,
    #"figure.figsize": figsize(0.9),     # default fig size of 0.9 textwidth
    "pgf.preamble": "\n".join([ # plots will use this preamble
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[detect-all,locale=DE]{siunitx}",
        ])
    }

mp.rcParams.update(pgf_with_latex)

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.text(30, .025, r'$\mu=100,\ \sigma=15 \SI{1132156465}{\second\meter} $')
plt.text(5, 50, r'$-\frac{p}{2} \pm \sqrt{ \left(\frac{p}{2}\right)^2 -q }$ \LaTeX')
#plt.savefig("myImagePDF.pdf", format="pdf", bbox_inches="tight")
plt.savefig('figure.pdf', backend='pgf')
#plt.show()
