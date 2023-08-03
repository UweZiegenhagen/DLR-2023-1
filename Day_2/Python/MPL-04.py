# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:36:05 2023

@author: Uwe
"""


## https://stackoverflow.com/questions/60140070/how-to-put-pgf-preamble-into-an-mplstyle-style
## https://stackoverflow.com/questions/76371558/matplotlib-pgf-backend-adjusting-preamble


import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np


pgf_with_latex = {                      # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],                   # blank entries should cause plots 
    "font.sans-serif": [],              # to inherit fonts from the document
    "font.monospace": [],
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
plt.text(30, .025, r'$\mu=100,\ \sigma=15$ \SI{1132156465}{\second\­per\meter}')
plt.text(5, 50, r'$-\frac{p}{2} \pm \sqrt{ \left(\frac{p}{2}\right)^2 -q }$ \LaTeX')
#plt.savefig("myImagePDF.pdf", format="pdf", bbox_inches="tight")
plt.savefig('figure.pdf', backend='pgf')
#plt.show()
