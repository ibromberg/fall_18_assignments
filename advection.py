"""
Reading Class Assignment
Advection Code

a = 0 if x < 1/3
  = 1 if 1/3 <= x < 2/3
  = 0 if 2/3 <= x
  
  u_i^n = u(x_i,t^n)
  
"""
import matplotlib.pyplot as plt
import numpy as np
# ------- variables ----------
C = 0.8 # CFL number
u = 1.0 # advection speed
nc = 100 # number of zones
xmax = 1.0
xmin = 0.0
# loop variables
i = 0
t = 1

#x = np.linspace(-1,1,num=nc) # array of x values - includes ghost cell
x = []
f_th = [] # tophat

f_old = np.empty(nc+1)
f_new = np.empty(nc+1)

dx = (xmax-xmin)/nc # grid interval
dt = dx*C / u # time interval
tmax = (xmax-xmin)/u # maximum time
max_tstep = tmax/dt # total number of time steps
x_3 = (xmax-xmin) / 3.0 # split grid into thirds for top hat

# make the grid
for i in range (0,nc+1):
    x.append( xmin + float(i)*dx )
    
# create top hat by splitting grid
for i in range (0,nc):
    if(x[i]>x_3 and x[i]<2*x_3):
        f_th.append(1.0)
    else:
        f_th.append(0.0)
f_th.append(f_th[0]) # add ghost cell

# advect through time
f_old = np.zeros(int(max_tstep)) 
for t in range(1,int(max_tstep)):
    # loop through mesh to get soln after one dt time step
    for i in range(0,nc):
        f_new.append( f_old[i] - (C * (f_old[i] - f_old[i-1]) ) ) # upwind
        #f_new.append( f_old[i] - (0.5 * C * (f_old[i+1] - f_old[i-1]) ) ) # FTCS
   
    f_old[:] = f_new[:] 
    
f_new.append(f_new[0]) # add ghost cell
# plot 
    
plt.plot(x,f_th)
plt.plot(x,f_new)
