"""
Ilana Bromberg
PHY341 HW5
"""
import matplotlib.pyplot as plt
import math as m

i = 0 # index variable
X = 0.6774979120958966 # mass fraction for H from HW2
Y = 0.2667119003681898 # mass fraction for He from HW2
Z = 0.01392290116087761021 # metals from HW2
n = 10000 # temperature increment
qmin = 10**3

rho_H = [] # hydrogen density
rho_He = [] # helium density
T = []

def rhoH(T9):
    q = (2.4e4 * X**2 * m.exp(-3.38/T9**(1/3)) / T9**(2/3)) + (4.4e25 * X * Z * 
        m.exp(-15.228/T9**(1/3)) / T9**(2/3)) # adds pp and CNO
    return qmin/q
    
def rhoHe(T8):
    q = 5.09e11 * Y**3 * T8**(-3) * m.exp(-44.027/T8)
    return m.sqrt(qmin/q)

for i in range (0,100000):
    T.append(9.99e6 + n) # T works between 10^7 and 10^9 
    n = n + 10000
    
    rho_H.append( rhoH(T[i]/10**9) ) # add value to H array
    rho_He.append( rhoHe(T[i]/10**8) ) # add value to He array

plt.yscale('log')
plt.xscale('log')
plt.xlabel("Log(Temperature)")
plt.ylabel("Log(Density)")
plt.title("AST341 HW5")

plt.plot(T,rho_H,label = "rhoH")
plt.plot(T,rho_He,label = "rhoHe")
plt.plot([15.7e6],[1.5e5], marker='o',markersize=3,color="red") # sun
plt.legend()
plt.show()


