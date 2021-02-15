# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:39:04 2021

@author: elois
"""

import spinmob as s
import mcphysics as mcp
#import matplotlib.pyplot as plt
import numpy as np

#Loading and reformatting data
#This is the data w/ scattering rod (02)
print("Choose the scattering data, ie the 02 file")
summed_databox = mcp.data.load_chns(combine=True)

#This is the data for background before (01)
print("Choose the before background data, ie the 01 file")
summed_databox2=mcp.data.load_chns(combine=True)

#This is the data for the background after (03)
print("Choose the before background data, ie the 03 file")
summed_databox3=mcp.data.load_chns(combine=True)

#The data from the scattering experiment
channels_data = summed_databox[0]
counts_data = summed_databox[1]


#The background data
counts_background_before = summed_databox2[1]
counts_background_after = summed_databox3[1]

#Bounds on the channels (in channel numbers)
a = 500
b = 700


#This is by channel for the data
shortened_channels_data = np.array(channels_data[a:b])
#This is counts for the data
shortened_counts_data = np.array(counts_data[a:b])

#Shortened Arrays for the background
shortened_background_before = np.array(counts_background_before[a:b])

shortened_background_after= np.array(counts_background_after[a:b])


diff = ((shortened_background_before + shortened_background_after)*0.5)
#Subtracting the Background

subtracted_counts = shortened_counts_data - diff


minimum = min(subtracted_counts)

pos_counts = subtracted_counts + minimum +1.0


    
#Converting Channel Number to energy value

#energy = 0.3736* subtracted_counts - 5.155
energy = 0.3736* shortened_channels_data - 5.155


f=s.data.fitter()
#f.set_functions('(a/(c * sqrt(2 * pi)))* exp(-0.5* (x - b)**2/(c**2)) - d*x + e','a=1873, b=220.8, c=13.8 , d=0.5, e = 20')
f.set_functions('a/(c * sqrt(2 * pi))*exp(-(x-b)**2/(2*c**2)) + d - e*erf(x-b)','a=1774,b=222,c=12, d=5, e=0.8')

#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(energy, pos_counts, np.sqrt(pos_counts))
values = f.get_fit_values()
f.fit()