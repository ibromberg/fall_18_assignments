"""
Reading Class Assignment
Advection Code

a = 0 if x < 1/3
  = 1 if 1/3 <= x < 2/3
  = 0 if 2/3 <= x
  
  u_i^n = u(x_i,t^n)
  
"""
import matplotlib.pyplot as plt

# ------- variables ----------
C = 0.8 # CFL number
u = 1.0 # advection speed
nc = 100 # number of zones
xmax = 1.0
xmin = 0.0
# loop variables
i = 0
t = 0

#x = np.linspace(-1,1,num=nc) # array of x values - includes ghost cell
x = []
f_th = [] # tophat
f_new = []

dx = (xmax-xmin)/nc # grid interval
dt = dx*C / u # time interval
tmax = (xmax-xmin)/u # maximum time
max_step = tmax/dt # total number of time steps
x_3 = (xmax-xmin) / 3.0 # split grid into thirds for top hat

# make the grid
for i in range (0,nc):
    x.append( xmin + float(i)*dx )
    
# create top hat by splitting grid
for i in range (0,nc):
    f_th.append(0.0)
    if(x[i]>x_3 and x[i]<2*x_3):
        f_th.append(1.0)
f_th.append(f_th[0]) # add ghost cell

# go through time
for t in range(0,int(max_step)):
    # loop through mesh to get soln after one dt time step
    for i in range(0,nc):
        f_new.append(f_th[i] - (C*(f_th[i] - f_th[i-1]))) # upwind
        # f_new.append( f_th[i] - (0.5*C*(f_th[i+1] - f_th[i-1])) ) # FTCS
    f_new.append(f_new[0])
    
# plot time
    
plt.plot(x,f_th)
