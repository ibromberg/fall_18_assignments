"""
Prof. Calder Reading Class Assignment
Fall 2018
Advection Code

a = 0 if x < 1/3
  = 1 if 1/3 <= x < 2/3
  = 0 if 2/3 <= x
  
  u_i^n = u(x_i,t^n)
  
"""
import matplotlib.pyplot as plt
import numpy as np

# constants
C = 0.8 # CFL number
u = 1.0 # advection speed
nc = 100 # number of zones (number of cells = nc)
xmax = 1.0 # maximum bound
xmin = 0.0 # minimum bound

# loop variables
i = 0
t = 1

# array variables
f_th = [] # array to hold tophat
f_old = np.empty(nc+1) # 'old' values
f_new = np.empty(nc+1) # 'new' values
x = np.empty(nc+1) # x axis

# generated constant variables
dx = (xmax-xmin)/nc # grid interval
dt = dx*C / u # time interval
tmax = (xmax-xmin)/u # maximum time
max_tstep = tmax/dt # total number of time steps
x_3 = (xmax-xmin) / 3.0 # split grid into thirds for top hat

# fill x array
for i in range (0,nc+1):
    x[i] = xmin + float(i)*dx 
    
# create top hat by splitting grid
for i in range (0,nc):
    if(x[i]>x_3 and x[i]<2*x_3):
        f_old[i] = 1.0
    else:
        f_old[i] = 0.0
        
f_old[-1] = f_old[nc] # add ghost cell
f_th = f_old.copy() # make a copy of the old array so that the tophat can be
    # referenced even when f_old is changed in the next part

# advect through time
for t in range(1,int(max_tstep)):
    for i in range(0,nc):
        f_new[i] = f_old[i] - C*(f_old[i] - f_old[i-1]) #upwind
        #f_new[i] = f_old[i] - 0.5*C*(f_old[i] - f_old[i-1]) # ftcs
        
    f_new[-1] = f_new[nc-1] # ghost cell
    f_old[:] = f_new[:] # update the soln on the old grid for the next step

# plot 

plt.plot(x,f_new,label="Upwind Scheme",color='black')
plt.plot(x,f_th,label="Top Hat",color='red')

plt.xlabel("Time")
plt.ylabel("Space?")
plt.title("Advection Scheme")
plt.legend()