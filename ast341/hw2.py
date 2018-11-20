# AST HW 2 Problem 3 Ilana Bromberg

Element = ['H', 'He', 'O', 'C', 'Ne', 'N', 'Mg', 'Si', 'Fe', 'S']
A = [12.00, 10.99, 8.93, 8.56, 8.09, 8.05, 7.58, 7.55, 7.54, 7.21]
# in order: H, He, O, C, Ne, N, Mg, Si, Fe, S
# index variables
i = 0 
j = 0 
k = 0 
q = 0
f = 10 #total number of elements
numatom_totalatom = [] # number fraction wrt H and later factoring that in
sum_x = 0 # sum of all the xi/xh
xH = 0 # variable to correct for xh=1 later on
n = 8.97e56 # number of atoms total
avo = 6.02e23 # avogadro's number
m_sol = 2e33 # solar mass

Xi = [] # mass fractions
AWei = [1, 4, 16, 12, 20, 14, 24, 28, 56, 32] # atomic weight
Z = [1, 2, 8, 6, 10, 7, 12, 14, 26, 16] # atomic number (number of protons)
mu_i_inv = 0 # inverted mu_ions
mu_e_inv = 0 # inverted mu_electrons
mu_inv = 0 # inverted mu_total

#calculate mass fractions
for i in range(0,f):
    numatom_totalatom.append(10**(A[i] - 12.00) * A[i] / 12.00)
    sum_x += numatom_totalatom[i]

sum_x -= 1.0 # assume that X_H = 1, normalize the rest
xH = 1.0 - sum_x # finding the mass fraction of H
numatom_totalatom[0] = xH # set index variable to correct mass fraction for H

# calculate mass fraction from number fraction
for j in range(0,f):
    Xi.append((numatom_totalatom[j] * n)/avo * (AWei[j]/m_sol))

#print out final mass fractions
print("Mass fractions:")
for k in range(0,f):
    print("X_",Element[k],": ",Xi[k])
    
# calculate mu values
for q in range (0,f):
    mu_i_inv += Xi[q]/AWei[q]
    mu_e_inv += Xi[q] * Z[q] / AWei[q]
    
mu_inv = mu_i_inv + mu_e_inv

mu_i = 1/mu_i_inv
mu_e = 1/mu_e_inv
mu = 1/mu_inv

print("mu_ions = ",mu_i)
print("mu_e = ",mu_e)
print("mu_total = ",mu)
