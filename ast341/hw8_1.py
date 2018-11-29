"""
HW8
"""
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

# ------------- question 1 -------------
G = 6.67e-8 # gravitational constant - cm3 / (g*s2)

# M1 is 0.8 solar masses and M2 is 0.2 solar masses; scale in terms of that
M1 = 0.8
M2 = 0.2 
a = 1.0 # separation between the stars
R1 = -0.5 # choosing locations for 1 and 2 to calculate the center of mass
R2 = 0.5

i = 0 # index variable
phi = [] # Y axis array
x = np.linspace(-3,3,num=100) # X axis array

Mt = M1 + M2 # total mass
cm = (M1*R1 + M2*R2)/Mt # center of mass
omega_sq = G * Mt / a**3 # rotational frequency

# loop over every point in X, assign s1, s2, and r, and calculate Y
for i in range(0,len(x)):
    s1 = abs(R1-x[i])
    s2 = abs(R2-x[i])
    r = abs(cm-x[i])
    phi.append( (-G*(M1/s1 + M2/s2) - 0.5*omega_sq*r**2) / (G*Mt/a) )
        # phi in terms of G Mt/a

# create plot
plt.plot(x,phi,color="black")
plt.scatter([cm],[0.0], marker='o',color="black",label="Center of Mass")
plt.title("AST341 HW8 Q1")
plt.xlabel("x [a]")
plt.ylabel("Φ [G(M₁+M₂)/a]")
plt.ylim((-10,1))
plt.legend()

# ------------- question 3 -------------
c = 3e10 # speed of light, cm/s
Ms = 1.99e33 # grams

Ledd = 3.2e4 * 10e-4 * 3.9e33 # eddington lumin in erg/s, kes = k

# calculate nuclear energy generated
energy_per_rxn = 0.03 * 1.67e-24 * c**2 # energy released in 4H -> He
num_H = 10**(-4)*Ms / 1.67e-24
energy = num_H / 4 * energy_per_rxn # total energy: number of hydrogen atoms
    # in this mass, divided by 4 because 4 H used per rxn, times energy per rxn
    
time_s = energy / Ledd # find time span - energy/Ledd gives units of seconds
time_y = time_s / 3.154e+7 # convert seconds to years
print('%.2E' % Decimal(time_y) + " years")
