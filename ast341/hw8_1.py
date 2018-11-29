"""
HW8
"""
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

G = 6.67e-8 # cm3 / (g*s2)
Rs = 6.96e10 # cm



M1 = 0.8
M2 = 0.2 

a = 1.0 
i = 0
phi = []
R1 = -0.5
R2 = 0.5

Mt = M1 + M2 # total mass
cm = (M1*R1 + M2*R2)/Mt # center of mass
omega_sq = G * Mt / a**3

x = np.linspace(-3,3,num=100)

for i in range(0,len(x)):
    s1 = abs(R1-x[i])
    s2 = abs(R2-x[i])
    r = abs(cm-x[i])
    phi.append( (-G*(M1/s1 + M2/s2) - 0.5*omega_sq*r**2) / (G*Mt/a) )

#    PLOT

plt.plot(x,phi,color="black")
plt.scatter([cm],[0.0], marker='o',color="black",label="Center of Mass")
plt.xlabel("x [a]")
plt.ylabel("Φ [G(M₁+M₂)/a]")
plt.title("AST341 HW8 Q1")
plt.legend()
plt.ylim((-20,1))


# -------- q3 -------
c = 3e10 # speed of light, cm/s
Ms = 1.99e33 # g

Ledd = 3.2e4 * 10e-4 * 3.9e33 # eddington lumin in erg/s, kes = k
energy_per_rxn = 0.03 * 1.67e-24 * c**2 # energy released in 4H -> He

# nuclear energy
num_H = 10**(-4)*Ms / 1.67e-24

energy = num_H/4 * energy_per_rxn # total energy: number of hydrogen atoms
    # in this mass, divided by 4 because 4 H used per rxn, times energy per rxn
time_s = 1/Ledd * energy
time_y = time_s / 3.154e+7
print('%.2E' % Decimal(time_y) + " years")