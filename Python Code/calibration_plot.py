# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:08:40 2021

@author: elois
"""

import spinmob as s
import matplotlib.pyplot as plt
import numpy as np


energy= [34.987, 80.9979, 122.06, 136.47, 356.0129, 511.0, 661.657]

channel = [95.744, 243.96, 354.243, 392.9, 966.98, 1361.67, 1743.38]

errors_energy = [0.0, 0.0011, 0.12, 0.29, 0.0007, 0.0, 0.003]

errors_channel = [0.042, 0.21, 0.056, 1.0, 0.4, 0.39, 0.63]

errors = [9.3, 16.93, 15.78, 15.78, 44.61, 47.7, 55.87]

errors2 = [4.7, 8.5, 7.9, 7.9, 22, 24, 28]


f=s.data.fitter()
f.set_functions('m*x + b','m = 2.76, b=5.03')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(energy, channel, errors_channel)
f.fit()
