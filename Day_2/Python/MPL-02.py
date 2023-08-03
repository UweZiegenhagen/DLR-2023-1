# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:06:52 2023

@author: Uwe
"""

import matplotlib as mpl
mpl.use("pgf")
preamble = r'\usepackage{siunitx}'
mpl.rcParams.update({
    "pgf.texsystem": 'lualatex',
    "pgf.preamble": preamble,
    'text.latex.preamble': preamble,
    'text.usetex': True,
    'font.size': 9,
    'lines.markersize' : 3
})

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(4.5, 2.5))
ax = fig.gca()
ax.plot(range(5))
ax.set_xlabel(u"µ is not $\\mu$")
fig.tight_layout()
fig.savefig("test.pdf")

mpl.font_manager.g