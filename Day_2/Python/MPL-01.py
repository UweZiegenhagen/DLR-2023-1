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


plt.rcParams.update({"text.usetex": True, 
                     'text.latex.preamble': r'\usepackage{siunitx}', 
                     'pgf.preamble': r'\usepackage{siunitx}', 
                     'pgf.texsystem': 'lualatex',
                     'font.family':'serif',
                     'font.serif' : 'cm'})

plt.rcParams["text.latex.preamble"].join([
        r"\usepackage{siunitx}\usepackage{sansmath}",              
        r"\setmainfont{Audiowide}",
])

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
