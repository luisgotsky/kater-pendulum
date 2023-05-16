import numpy as np
import matplotlib.pyplot as plt

file = open("Data\\data.txt", "r")

x, y, ex, ey = [], [], [], []

for linea in file:
    
    l = linea.split()
    x.append(float(l[1]))
    y.append(float(l[0]))
    ex.append(float(l[3]))
    ey.append(float(l[2]))
    
aprox = np.polyfit(x, y, 1)
t = np.linspace(min(x), max(x))
a, b = round(aprox[0], 1), round(aprox[1], 0)

plt.figure(figsize=(9, 6))
plt.errorbar(x, y, xerr=ex, yerr=ey ,fmt="o", ecolor="black", capsize=5)
plt.plot(t, np.polyval(aprox, t), "--")
plt.grid()
plt.ylabel("$h_{1}^{2} - h_{2}^{2} \\ (cm^{2})$")
plt.xlabel("$T_{1}^{2}h_{1} - T_{2}^{2}h_{2} \\ (cm*s^{2})$")
plt.text(t[30], y[0], "y = " + str(a) + "x" + str(b) + "\n $R^{2} = 0.9967$",
         horizontalalignment="center")
#plt.savefig("Todos.png", dpi=1200)

#Discriminación por cota

file2 = open("Data\\cota.txt", "w")
x2, y2, ex2, ey2 = [], [], [], []

for i in range(len(x)):
        
    xi, yi = x[i], y[i]
    g = (np.pi**2)*4*yi/xi
        
    if 880 < g < 1080:
            
        x2.append(xi)
        y2.append(yi)
        ex2.append(ex[i])
        ey2.append(ey[i])
        file2.write(str(xi) + "    " + str(yi) + "\n")
            
file2.close()

aprox2 = np.polyfit(x2, y2, 1)
t2 = np.linspace(min(x2), max(x2))
a2, b2 = round(aprox2[0], 1), round(aprox2[1], 0)

plt.figure(figsize=(9, 6))
plt.errorbar(x2, y2, xerr=ex2, yerr=ey2 ,fmt="o", ecolor="black", capsize=5)
plt.plot(t2, np.polyval(aprox2, t2), "--")
plt.grid()
plt.ylabel("$h_{1}^{2} - h_{2}^{2} \\ (cm^{2})$")
plt.xlabel("$T_{1}^{2}h_{1} - T_{2}^{2}h_{2} \\ (cm*s^{2})$")
plt.text(t2[30], 2000, "y = " + str(a2) + "x+" + str(b2) +
         "\n $R^{2} = 0.9931$",
         horizontalalignment="center")
#plt.savefig("Cotado.png", dpi=1200)

file3 = open("Data\\recta.txt", "w")

x3, y3, ex3, ey3 = [], [], [], []

for i in range(len(x)):

    d = np.sqrt((np.array([x[i]]*len(t)) - t)**2 + (np.array([y[i]]*len(t))
                                          - np.polyval(aprox, t))**2)
    
    if min(d) < 2*np.sqrt(ey[i]**2 + ex[i]**2):
        
        x3.append(x[i])
        y3.append(y[i])
        ex3.append(ex[i])
        ey3.append(ey[i])
        file3.write(str(x[i]) + "    " + str(y[i]) + "\n")
        
file3.close()

t3 = np.linspace(min(x3), max(x3), 1000)
aprox3 = np.polyfit(x3, y3, 1)
a3, b3 = round(aprox3[0], 1), round(aprox3[1], 0)

plt.figure(figsize=(9, 6))
plt.errorbar(x3, y3, xerr=ex3, yerr=ey3 ,fmt="o", ecolor="black", capsize=5)
plt.plot(t3, np.polyval(aprox3, t3), "--")
plt.grid()
plt.ylabel("$h_{1}^{2} - h_{2}^{2} \\ (cm^{2})$")
plt.xlabel("$T_{1}^{2}h_{1} - T_{2}^{2}h_{2} \\ (cm*s^{2})$")
plt.text(t3[700], 1000, "y = " + str(a3) + "x" + str(b3) +
         "\n $R^{2} = 0.9963$",
         horizontalalignment="center")
#plt.savefig("Recta.png", dpi=1200)

xd = [1, 2]
yd = [9.9, 9.804972]
eyd = [0.2, 0.000079]
td = np.linspace(1, 2, 2)
ydr = [9.804972]*2

plt.figure(figsize=(9, 6))
plt.errorbar(xd, yd, yerr=eyd, fmt="o", ecolor="black", capsize=5)
plt.plot(td, ydr, "--")
plt.xlabel("Valores")
plt.ylabel("$g (\\frac{m}{s^{2}})$")
plt.savefig("Datos.png", dpi=1200)