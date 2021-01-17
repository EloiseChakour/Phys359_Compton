# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:30:25 2021

@author: eloise
"""

import spinmob as s
import mcphysics as mcp
import matplotlib.pyplot as plt

#Loading and reformatting data
summed_databox = mcp.data.load_chns(combine=True)

x = summed_databox[0]
y = summed_databox[1]


shortened_x = x[1000:2048]
shortened_y = y[1000:2048]

f=s.data.fitter()
f.set_functions('a*exp(-(x-b)**2/(2*c**2))','a=180,b=1350,c=64')
#Gaussian Function with guessed value for parameter a,b,c 
f.set_data(shortened_x,shortened_y, 0.1) #Data point with error as the last parameter
f.fit()






plt.plot(shortened_x, shortened_y)





