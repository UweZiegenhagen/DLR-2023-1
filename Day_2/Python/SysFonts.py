# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:04:35 2023

@author: Uwe
"""

import matplotlib as mp

# not working
# mp.font_manager._rebuild()


# https://stackoverflow.com/questions/37920935/matplotlib-cant-find-font-installed-in-my-linux-machine
# nope
#import matplotlib.font_manager;
#matplotlib.font_manager._rebuild() 


#import shutil
#import matplotlib
#shutil.rmtree(matplotlib.get_cachedir())


fonts = mp.font_manager.get_font_names()
fonts.sort()

for i in fonts:
    print(i)
    

