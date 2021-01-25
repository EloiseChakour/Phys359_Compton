# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:34:58 2021

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

#This is by channel
shortened_x = x[300:400]
#This is counts
shortened_y = y[300:400]


f=s.data.fitter()
f.set_functions('a*exp(-(x-b)**2/(2*c**2)) + d*exp(-(x-e)**2/(2*c**2)) + 2500 - 4.10*x','a=14697,b=354,c=15.6, d= 1106, e= 388.8')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(shortened_x,shortened_y, np.sqrt(shortened_y))
f.fit()





#plt.plot(x,y)
plt.plot(shortened_x, shortened_y)
