# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:11:47 2021

@author: elois
"""

import spinmob as s
import mcphysics as mcp
import matplotlib.pyplot as plt

#Loading and reformatting data
summed_databox = mcp.data.load_chns(combine=True)

x = summed_databox[0]
y = summed_databox[1]

#This is by channel
shortened_x = x[1200:1550]
#This is counts
shortened_y = y[1200:1550]

f=s.data.fitter()
f.set_functions('a*exp(-(x-b)**2/(2*c**2))+32 - 0.014*x','a=170,b=1360,c=50')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(shortened_x,shortened_y, 0.174)
f.fit()





#plt.plot(x,y)
plt.plot(shortened_x, shortened_y)