


import mcphysics as mcp

#Loading and reformatting data
summed_databox = mcp.data.load_chns(combine=True)

x = summed_databox[0]
y = summed_databox[1]

#Enter the range
a=1200
b=1550

shortened_x = x[a:b]
shortened_y = y[a:b]


avg = sum(shortened_y )/len(shortened_y )

squares=[]
for n in shortened_y:
    squares.append(n**2)

    
    #print(squares)

#Variance
var=abs((sum(squares)/len(squares))-avg**2)

#Standard Deviation
std=(var)**(1/2)

error=std/(10*len(shortened_y))**(0.5)


print(error)

##################################################

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

########################################
