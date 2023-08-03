# -*- coding: utf-8 -*-
"""
https://stackoverflow.com/questions/40290004/how-can-i-configure-matplotlib-to-be-able-to-read-fonts-from-a-local-path

"""


#!/usr/bin/env python3
# Imports
import os
import re
import shutil
from glob import glob
from matplotlib import matplotlib_fname
from matplotlib import get_cachedir

# Copy files over
dir_source = 'C:/Windows/Fonts'
dir_data = os.path.dirname(matplotlib_fname())
dir_dest = os.path.join(dir_data, 'fonts', 'ttf')
print(f'Transfering .ttf and .otf files from {dir_source} to {dir_dest}.')
for file in glob(os.path.join(dir_source, '*.[ot]tf')):
    if not os.path.exists(os.path.join(dir_dest, os.path.basename(file))):
        print(f'Adding font "{os.path.basename(file)}".')
        shutil.copy(file, dir_dest)

# Delete cache
dir_cache = get_cachedir()
for file in glob(os.path.join(dir_cache, '*.cache')) + glob(os.path.join(dir_cache, 'font*')):
    if not os.path.isdir(file): # don't dump the tex.cache folder... because dunno why
        os.remove(file)
        print(f'Deleted font cache {file}.')