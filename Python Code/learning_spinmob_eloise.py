# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import spinmob as s
import mcphysics
import matplotlib.pyplot as plt

#mcphysics.playground.fitting_statistics_demo()

#%%
#ctrl+enter to run cell

d = mcphysics.data.load_chns(combine=True)
#lt.plot(d[0],d[1])

x = d[0]
y = d[1]

plt.plot(x,y)

#%%
#mcphysics.data.plot_chns(combine=True)
