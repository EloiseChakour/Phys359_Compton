# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:15:19 2021

@author: elois
"""

import spinmob as s
import mcphysics as mcp
import matplotlib.pyplot as plt
import numpy as np

#Loading and reformatting data
summed_databox = mcp.data.load_chns(combine=True)

#Channel Number
x = np.array(summed_databox[0])

#Counts
y = np.array(summed_databox[1])

#Number of runs:
runs = 5

#Total time is 30*runs THIS IS IN SECONDS
time = runs*30

#Find the total counts
count = 0
for i in range(len(y)):
    count += y[i]
    
print(count)

#Find the Counts/second

M = count/time

print(M)