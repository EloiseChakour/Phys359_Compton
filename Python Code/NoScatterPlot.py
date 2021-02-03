# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:18:37 2021

@author: Yacine Benkirane
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

a=550
b=840

shortened_x = x[a:b]
#This is counts
shortened_y = y[a:b]


f=s.data.fitter()
f.set_functions('a*x+b','a=-5,b=5')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(shortened_x,shortened_y, np.sqrt(shortened_y))
f.fit()





#plt.plot(x,y)
plt.plot(shortened_x, shortened_y)