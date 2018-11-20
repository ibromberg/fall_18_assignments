# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:40:52 2018

@author: ilana
"""

import matplotlib.pyplot as plt
import math as m

T = 1 # 5778/10^9 # T_9 temperature for the sun in Kelvin
X = 0.6774979120958966 # mass fraction for H
Z = 0.01392290116087761021 # metals from homework 2
f = 100000 #final index value
i = 0 # index value for plot

qpp = [] # proton-porton chain reaction over density * 1/rho
qcno =  [] # CNO chain rxn over density * 1/rho
q3a = [] # triple alpha process for He
Temp = []
for T in range (1,f):
    qpp.append(2.4e4 * X**2 * m.exp(-3.38/T**(1/3)) / T**(2/3))
    qcno.append(4.4e25 * X * Z * m.exp(-15.228/T**(1/3)) / T**(2/3))
    Temp.append(T)

plt.yscale('log')
plt.xlabel("Temperature")
plt.ylabel("q/rho")
plt.title("AST341 HW2 Q1")

plt.plot(Temp,qpp,label = "qpp")
plt.plot(Temp,qcno,label="qcno")
plt.legend()
plt.show()