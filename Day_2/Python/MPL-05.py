# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:06:52 2023

@author: Uwe

https://tex.stackexchange.com/questions/391074/how-to-use-the-siunitx-package-within-python-matplotlib
"""

import matplotlib as mpl
mpl.use('pgf')
mplparams = {"pgf.rcfonts": False}
mpl.rc('text', usetex=True)
mpl.rcParams.update(mplparams)
import matplotlib.pyplot as plt


pgf_with_latex = {                      # setup matplotlib to use latex for output
    "pgf.texsystem": "lualatex",        # change this if using xetex or lautex
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
mpl.rcParams.update(pgf_with_latex)


X = [0, 1, 2, 3, 4, 5]
Y = [-2, 7 , 3 , 8 , 7, 5]
plt.plot(X, Y)
plt.text(3, 0, r'$\mu=100,\ \sigma=15$ \SI{123444567}{\meter}')
#plt.text(5, 50, r'$-\frac{p}{2} \pm \sqrt{ \left(\frac{p}{2}\right)^2 -q }$ \LaTeX')
#plt.xlabel(r'Distance \SI{1}{\meter}')# (\si{\meter})')
plt.savefig('uwe.pgf')