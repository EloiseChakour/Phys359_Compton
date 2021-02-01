# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:04:21 2021

@author: elois
"""

import matplotlib.pyplot as plt
import numpy as np





x =  np.array([75.0, 85.0, 95.0, 105.0, 125.0, 135.0, 220.0, 230.0, 240.0, 250.0, 260.0, 280.0])

y = 1.0 / ( (1.0/661.0) - (1.0/510.0) * ( 1.0 - np.cos(np.radians(x-180.0)) ) )

plt.plot(x, y)