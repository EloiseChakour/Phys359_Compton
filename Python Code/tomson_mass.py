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
area = np.array([53.7, 47.3, 43.8, 43.46, 44.7, 48.67, 56.52, 48.7, 47.05, 45.49, 44.39, 49.1])
#Errors 




# e_0 = 8.854

f=s.data.fitter()
f.set_functions('( (a)/((r**2)*(1 + (cos(radians(x-z)))**2 )) )','a=200, r=2.81, z=180')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(angles, area , np.sqrt(area))
values = f.get_fit_values()
f.fit()