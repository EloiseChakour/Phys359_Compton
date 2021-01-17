# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:45:56 2021

@author: Yukuan Zhao
"""

  
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import mcphysics as k
import spinmob as s
import numpy as np

D=k.data.load_chns(combine=True) #loading data and putting it in a parameter D
f=s.data.fitter()
f.set_functions('a*exp(-(x-b)**2/(2*c**2))','a=90,b=50,c=12')
#Gaussian Function with guessed value for parameter a,b,c 
f.set_data(D[0],D[1], 0.1) #Data point with error as the last parameter
f.fit()

