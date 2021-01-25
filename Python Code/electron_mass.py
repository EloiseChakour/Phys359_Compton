# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:02:14 2021

@author: elois
"""

import spinmob as s
import matplotlib.pyplot as plt
import numpy as np

angles = np.array([255.0, 265.0, 275.0, 285.0, 305.0, 315.0, 40.0, 50.0, 60.0, 70.0, 80.0, 100.0])

angles_rad = angles*(1.0/(2.0*np.pi))

angles_cosine = np.cos(angles_rad)

angle_term = 1- angles_cosine

peaks_channels = np.array([690, 750, 827, 914, 1135, 1274, 1359, 1223, 1103, 980, 884, 729])

peaks_energies = 2.67*peaks_channels + 13

energy_diff = peaks_energies - 661.657

f=s.data.fitter()
f.set_functions('m*x + b','m = 2.67, b=13')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(peaks_channels, angle_term, 0.5)
f.fit()
