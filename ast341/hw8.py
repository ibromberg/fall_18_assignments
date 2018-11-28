
import matplotlib.pyplot as plt

t_eff = []
lumin = []
age = []

history_file = open("history_simple.out","r")

for line in history_file:
    if line.startswith('#'):
        continue
    else:             
        row = line.rstrip('\n')
        row = row.split()
        age.append(row[0])
        t_eff.append(row[2])
        lumin.append(row[4])
        
plt.xlabel("temperature")
plt.ylabel("luminosity")
plt.title("Homework??")

plt.plot(t_eff[0:50],lumin[0:50])
plt.show()
