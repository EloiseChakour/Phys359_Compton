# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:39:04 2021

@author: elois
"""

import spinmob as s
import mcphysics as mcp
import matplotlib.pyplot as plt
import numpy as np

#Loading and reformatting data
summed_databox = mcp.data.load_chns(combine=True)

x = summed_databox[0]
y = summed_databox[1]

a = 550
b = 850

#This is by channel
shortened_x = np.array(x[a:b])
#This is counts
shortened_y = np.array(y[a:b])

for i in range(len(shortened_y)):
    if shortened_y[i] ==0:
        shortened_y +=1
#Converting Channel Number to energy value

energy = 0.3736*shortened_x - 5.155

f=s.data.fitter()
f.set_functions('(a/(c * sqrt(2 * pi)))* exp(-0.5* (x - b)**2/(c**2)) + d*(-0.043*x + 20.35 - 1.385*erf(x-b))','a=1873, b=253.8, c=13.8 , d=2.0')
#f.set_functions('(a/(c * sqrt(2 * pi)))* exp(-0.5* (x - b)**2/(c**2)) + 15','a=2200, b=250.8, c=16')

#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(energy,shortened_y, np.sqrt(shortened_y))
values = f.get_fit_values()
f.fit()