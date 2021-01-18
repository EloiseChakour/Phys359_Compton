
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:30:25 2021
@author: eloise
"""



import mcphysics as mcp

#Loading and reformatting data
summed_databox = mcp.data.load_chns(combine=True)

x = summed_databox[0]
y = summed_databox[1]

a=1200
b=1550

shortened_x = x[a:b]
shortened_y = y[a:b]


avg = sum(shortened_y )/len(shortened_y )

squares=[]
for n in shortened_y:
    squares.append(n**2)
print(squares)

var=abs((sum(squares)/len(squares))-avg**2)

std=(var)**(1/2)

error=std/(len(shortened_y))**(0.5)


print(error)