# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:02:14 2021

@author: elois
"""

import spinmob as s
#import matplotlib.pyplot as plt
import numpy as np


#Angles given by the physical display (in degrees)
angles = np.array([75.0, 85.0, 95.0, 105.0, 125.0, 135.0, 220.0, 230.0, 240.0, 250.0, 260.0, 280.0])

#Peaks found (in kev) from fitting
peaks = np.array([252.74, 274.63, 303.33, 334.03, 418.65, 470.92, 503.43, 452.6, 407.58, 361.91, 325.81, 267.71])

#Errors given on fitted peak parameter (in kev)
errors = np.array([0.32, 0.45, 0.39, 0.39, 0.41, 0.42, 0.4, 0.4, 0.42, 0.42, 0.41, 0.41])




f=s.data.fitter()
f.set_functions('  1.0 / ( (1.0/E_0) - (1.0/m_e) * ( 1.0 - cos(radians(x)) ) ) ','m_e = 510, E_0= 661 ')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(angles, peaks, errors)
f.fit()

#s.plot.xy.data(angles_rad, peaks_energies, eydata = 1, exdata = 0.5)
