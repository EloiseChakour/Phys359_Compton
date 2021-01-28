# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:02:14 2021

@author: elois
"""

import spinmob as s
import matplotlib.pyplot as plt
import numpy as np


#Change these to actual angles!!! The actual conversion will become a variable & fit it 
angles = np.array([75.0, 85.0, 95.0, 105.0, 125.0, 135.0, 220.0, 230.0, 240.0, 250.0, 260.0, 280.0])



#angles_rad = angles*(1.0/(2.0*np.pi))
"""
angles_cosine = np.cos(angles_rad)

angle_term = 1- angles_cosine
"""

peaks_channels = np.array([690, 750, 827, 914, 1135, 1274, 1359, 1223, 1103, 980, 884, 729])

peaks_energies = 0.3736*peaks_channels - 5.155

#energy_diff = peaks_energies - 661.657

f=s.data.fitter()
f.set_functions(' 1.0/(1.0/E_0 - (1/m_e) * ( 1.0-cos( (pi/180.0)*(x-180.0) ) ) )','m_e = 510, E_0= 661 ')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(angles, peaks_energies, 10)
f.fit()

#s.plot.xy.data(angles_rad, peaks_energies, eydata = 1, exdata = 0.5)
