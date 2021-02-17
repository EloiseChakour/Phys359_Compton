# -- coding: utf-8 --
"""
Created on Mon Feb  8 16:39:04 2021

@author: elois
"""

import spinmob as s
import mcphysics as mcp
#import matplotlib.pyplot as plt
import numpy as np

#Loading and reformatting data
summed_databox = mcp.data.load_chns(combine=True) # Raw data for compton scattering
summed_databox2=mcp.data.load_chns(combine=True)  # Background (before)
summed_databox3=mcp.data.load_chns(combine=True)  ## Background (After)

x = summed_databox[0]  #Bin values
y = summed_databox[1]  # Raw data number of counts
z = summed_databox2[1]  #Background (Before)
k = summed_databox3[1]  #Background (After)

#Bounds
a = 500
b = 700

#Data Corresponding to the Bounds
shortened_x = np.array(x[a:b])

shortened_y = np.array(y[a:b])

shortened_z = np.array(z[a:b])

shortened_k= np.array(k[a:b])

z=shortened_y-(shortened_z+shortened_k)*0.5 # Raw data minus the average of background before and after


#Taking care of any 0 value and seting it to 1
for i in range(len(shortened_y)):
    if shortened_y[i] ==0:
        shortened_y +=1
        
        
#Converting Channel Number to energy value

energy = 0.3736*shortened_x - 5.155


#Fitting fucntion
f=s.data.fitter()
f.set_functions('a*exp(-(x-b)**2/(2*c**2))+d-e*x','a=60,b=220,c=15,d=0.5,e=0.55')
#Gaussian Function with guessed value for parameter a,b,c,d, and e 


#f.set_functions('(a/(c * sqrt(2 * pi)))* exp(-0.5* (x - b)2/(c2)) + d(-0.043x + 20.35 - 1.36*erf(x-b))','a=1873, b=276.8, c=13.8 , d=2.0')


f.set_data(energy,shortened_y, np.sqrt(shortened_y))
values = f.get_fit_values()
f.fit()