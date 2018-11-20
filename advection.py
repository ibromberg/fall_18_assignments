"""
Reading Class Assignment
Advection Code
"""
import matplotlib.pyplot as plt
import numpy as np

# ------- variables ----------
C = 0.8 # constant
u = 1.0 # advection speed
nc = 100 # number of cells
x = []
y = []

# ------------- make the 1d grid -------------------

def grid(nc):
    num_cells = nc
    x = np.linspace(0.0,1.0,num=num_cells)
    np.append(x,x[0])
    return x

# ---------- make the tophat ----------
    
def tophat(x,y,nc):    
    i = 0    
    num_cells = nc
    for i in range(0,num_cells):
        if x[i]>0.3 and x[i]<0.7:
            y.append(1.0)
        else:
            y.append(0.0)
                
    return (y)

# ------------- plotting ---------------

x = grid(nc)
y = tophat(x,y,nc)

plt.plot(x,y)
plt.title("Tophat")
