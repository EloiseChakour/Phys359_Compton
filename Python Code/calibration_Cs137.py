# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:35:10 2021

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
shortened_x = x[1400:2200]
#This is counts
shortened_y = y[1400:2200]

f=s.data.fitter()
f.set_functions('a*exp(-(x-b)**2/(2*c**2))+ 33 - 0.0166*x','a=80,b=1745,c=58')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(shortened_x,shortened_y, np.sqrt(shortened_y))
f.fit()





#plt.plot(x,y)
plt.plot(shortened_x, shortened_y)
