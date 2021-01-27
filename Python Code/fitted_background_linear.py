# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import spinmob as s
import mcphysics as mcp
import matplotlib.pyplot as plt
import numpy as np

#Loading and reformatting data
summed_databox = mcp.data.load_chns(combine=True)

x = summed_databox[0]
y = summed_databox[1]

a = 1600
b = 1900

#This is by channel
shortened_x = np.array(x[a:b])
#This is counts
shortened_y = y[a:b]

#Converting Channel Number to energy value

energy = 0.374*shortened_x - 4.8

f=s.data.fitter()
f.set_functions('a*exp(-(x-b)**2/(2*c**2))+d-m*x','a=76,b=655,c=21, d = 53, m = 0.0775')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(energy,shortened_y, np.sqrt(shortened_y))
f.fit()





#plt.plot(x,y)
#plt.plot(shortened_x, shortened_y)

