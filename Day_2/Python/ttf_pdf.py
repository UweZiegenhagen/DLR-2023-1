# -*- coding: utf-8 -*-
"""
https://www.tutorialspoint.com/how-to-embed-fonts-in-pdfs-produced-by-matplotlib
"""

import numpy as np
from matplotlib import pyplot as plt, font_manager as fm

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.rcParams['pdf.fonttype'] = 42

fig, ax = plt.subplots()
x = np.random.rand(100)
y = np.random.rand(100)

ax.scatter(x, y, c=y, marker="v")

# fprop = fm.FontProperties(fname='C:\Windows\Fonts\FREESCPT.TTF')
fprop = fm.FontProperties(fname='C:\Windows\Fonts\lmroman12-bold.otf')


# 

ax.set_title('Scatter Plot With Random Points',
            fontproperties=fprop, size=20, fontweight="bold")

plt.savefig("demo.pdf")