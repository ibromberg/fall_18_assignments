# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:45:43 2018

@author: ilana
"""
import matplotlib.pyplot as plt
import numpy as np

n = 1 # the n in the lane emden eqn
i = 0 # loop index

x = [] # xi - some very small number, very close to 0, so that there isn't a divide by zero error
y = [] # theta, and y(0)=1
z = [] # theta' = dtheta/dxi, y'(0)=0

x[0] = 1e-7
y[0] = 1.0
z[0] = 0.0

dx = 0.001 # h = step size

#dy/dx = z
#dz/dx = -2z/x -y^n
# RK: y_n+1 = y_n + 1/6(k1+2k2+2k3+k4), t_n+1 = tn+h

for i in range(0,1000000):
    z.append( z[i] + dx*(-2*z[i]/x[i] - y[i]^n) )   
    y.append( y[i] + dx * z[i] )
    x.append( x[i] + dx)

plt.xlabel("Xi")
plt.ylabel("Theta")
plt.title("Lane Emden: AST341 HW4")

plt.plot(x,y)
plt.show()
