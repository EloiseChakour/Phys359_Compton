

import spinmob as s
import matplotlib.pyplot as plt
import numpy as np


angles = np.array([-105.0, -95.0, -85.0, -75.0, -55.0, -45.0, 40.0, 50.0, 60.0, 70.0, 80.0, 100.0])


angles_rad = angles*(1.0/(2.0*np.pi))
"""
angles_cosine = np.cos(angles_rad)

angle_term = 1- angles_cosine
"""

peak_00 = np.array([654.04, 650.73, 654.7, 650.73, 652.37, 654.04, 651.32, 650.73, 654.04, 654.7, 652.98, 650.95])

peak_00_errors = np.array([0.34, 0.3, 0.34, 0.3, 0.3, 0.34, 0.3, 0.3, 0.34, 0.34, 0.32, 0.31])

peak_04 = np.array([647.04, 650.39, 649.25, 650.39, 649.66, 647.04, 648.6, 650.39, 647.04, 649.25, 650.99, 650.17])

peak_04_errors = np.array([0.32, 0.31, 0.31, 0.31, 0.32, 0.32, 0.32, 0.31, 0.32, 0.31, 0.32, 0.31])

peak = peak_00 - peak_04

error = peak_00_errors + peak_04_errors


#energy_diff = peaks_energies - 661.657

f=s.data.fitter()
f.set_functions('m*x + b','m = -0.0047, b = 3.42')
#Gaussian Function with guessed value for parameter a,b,c 
#Data point with error as the last parameter
#f.set_data(x, y, 0.1) 
f.set_data(angles, peak, error)
f.fit()

#s.plot.xy.data(angles, peak, eydata = error, exdata = 0.5)
