# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:35:40 2021

@author: elois
"""


import spinmob as s
import mcphysics as mcp
import matplotlib.pyplot as plt
import numpy as np


#Angles given by the physical display (in degrees)
angles = np.array([75.0, 85.0, 95.0, 105.0, 125.0, 135.0, 220.0, 230.0, 240.0, 250.0, 260.0, 280.0])

#area measured
area = np.array([54.0, 47.0, 43.8, 43.5, 44.7, 48.7, 56.5, 48.7, 47.1, 45.5, 44.4, 49.0])
errors = np.array([1.0, 1.0, 1.0, 0.9, 0.8, 0.8, 0.9, 1.5, 0.8, 0.9, 0.9, 1.0])



# e_0 = 8.854

f=s.data.fitter()
f.set_functions('(1.0/((m_e)**(2))) * (1.0 +(cos(radians(x-z)))**2)(k)','k =3, m_e =1, z=180.0')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(angles, area ,errors)
values = f.get_fit_values()
f.fit()