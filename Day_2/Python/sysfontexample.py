# -*- coding: utf-8 -*-
"""
https://scentellegher.github.io/visualization/2018/05/02/custom-fonts-matplotlib.html
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'perc': pd.Series([45, 35, 10, 5, 3, 2], index=['A', 'B', 'C','D','E','F'])})

# specify the custom font to use
#plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Latin Modern Roman'

fig, ax = plt.subplots(figsize=(7,4))
df.iloc[::-1].plot(kind='barh', legend = False, ax=ax)
ax.set_xlabel('Percentage',fontsize=15)
ax.set_ylabel('Type',fontsize=15)
