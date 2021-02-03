# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:25:33 2021

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

a=1000
b=1450

shortened_x = x[a:b]
shortened_y = y[a:b]

for i in range(len(shortened_y)):
    if shortened_y[i] ==0:
        shortened_y +=1
#Converting Channel Number to energy value

energy = 0.3736*shortened_x - 5.155

f=s.data.fitter()
f.set_functions('-a*x+b + c*erf(x-d)','a=-5,b=15, c = -5, d=400')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(energy, shortened_y, np.sqrt(shortened_y))
f.fit()