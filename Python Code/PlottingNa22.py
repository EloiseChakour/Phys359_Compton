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

l = 1200
r = 1550

shortened_x = x[l:r]
#This is counts
shortened_y = y[l:r]


f=s.data.fitter()
f.set_functions('a*exp(-(x-b)**2/(2*c**2))+d-m*x','a=171,b=1367,c=48, d=58, m=0.0324')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(shortened_x,shortened_y, np.sqrt(shortened_y))
f.fit()





#plt.plot(x,y)
plt.plot(shortened_x, shortened_y)
