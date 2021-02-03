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

a = 600
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
f.set_functions('a*exp(-(x-b)**2/(2*c**2)) + d*(-0.1525*x + 50.6 - 1.375*erf(x-b))','a=45, b=270, c=18 , d=1.6')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(energy,shortened_y, np.sqrt(shortened_y))
values = f.get_fit_values()
f.fit()





#plt.plot(x,y)
#plt.plot(shortened_x, shortened_y)

