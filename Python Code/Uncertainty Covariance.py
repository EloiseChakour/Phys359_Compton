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



import mcphysics as mcp
import numpy as np
#Loading and reformatting data
#summed_databox = mcp.data.load_chns(combine=True)
summed_databox = mcp.data.load_chns(combine=True)
x = summed_databox[0]
y = summed_databox[1]

a=75
b=120

shortened_x = x[a:b]
shortened_y = y[a:b]

A=np.cov([shortened_y])

print(A**0.5)