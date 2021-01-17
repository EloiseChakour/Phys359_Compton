# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:30:25 2021

@author: eloise
"""

import spinmob as s
import mcphysics as mcp
import matplotlib.pyplot as plt

# This imports a single databox and names it.If you type databox.h() into your console, you will get the header information

databox = mcp.data.load_chn()

#By using this you can load multiple files & sum them

summed_databox = mcp.data.load_chns(combine=True)

#You could plot the combined data by doing this:

#mcp.data.plot_chns(combine=True)

#But you can also decompose the data into arrays

x = summed_databox[0]
y = summed_databox[1]

plt.plot(x, y)








