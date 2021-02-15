# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:03:16 2021

@author: Yacine Benkirane
"""

import spinmob as s
import mcphysics as mcp
import matplotlib.pyplot as plt
import numpy as np

angles = np.array([55.0, 65.0, 75.0, 85.0, 95.0, 105.0, 125.0, 135.0, 220.0, 230.0, 240.0, 250.0, 260.0, 280.0, 300.0, 310.0])

#sigma_T = np.array([70.0, 56.0, 54.0, 47.0, 43.8, 43.5, 44.7, 48.7, 56.5, 48.7, 47.1, 45.5, 44.4, 49.0, 61.0, 64.0])
sigma_T = np.array([1774.0, 1900.0, ])

unc_sig = np.array([2.0, 2.0, 1.0, 1.0, 1.0, 0.9, 0.8, 0.8, 0.9, 1.5, 0.8, 0.9, 0.9, 1.0, 2.0, 2.0])


f=s.data.fitter()
#f.set_functions('(1.0/((m_e)**(2.0))) * (1.0 +(cos(radians(x-z)))**2.0) * (k)','k = 1.0 , m_e =510.0, z=180.0')
f.set_functions('r * (1.0 +(cos(radians(x-z)))**2.0)','r =40.0, z=180.0')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(angles, sigma_T, unc_sig)
f.fit()
