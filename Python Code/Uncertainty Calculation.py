# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:54:14 2021

@author: I don't know
"""

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

a=75
b=120

shortened_x = x[a:b]
shortened_y = y[a:b]


avg = sum(shortened_y )/len(shortened_y )

squares=[]
for n in shortened_y:
    squares.append(n**2)
## print(squares)

var=(sum(squares)/len(squares))-avg**2

std=(var)**(1/2)

error=std/(len(shortened_y))