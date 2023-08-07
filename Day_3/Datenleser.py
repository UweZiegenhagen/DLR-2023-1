# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:39:01 2023

@author: Uwe
"""

import numpy as np
import pandas as pd

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)
from pandas_datareader import data as pdr

df = pdr.get_data_yahoo('AAPL', start='2023-8-1')

df.to_latex('aapl.tex')