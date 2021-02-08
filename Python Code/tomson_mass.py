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

#counts/second
M = np.array([203.38, 210.69, 219.49, 227.71, 297.85, 397.37, 513.78, 337.71, 289.59, 257.91, 241.27, 222.85])


# e_0 = 8.854

f=s.data.fitter()
f.set_functions('( (2*a * 4 * pi * )/(r*(1 + (cos(radians(x-z)))**2 )*(sin(radians(x-z)))) )','a=200, r=2.81, z=180')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(angles, M , np.sqrt(M))
values = f.get_fit_values()
f.fit()