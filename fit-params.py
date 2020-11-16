# 2020-11-16
# programkód, ami elvégzi a fittelést egy beolvasott txt fájlra,
# majd a fittelt paramétereket elmenti egy másik txt fájlba

#importok
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

#adatbekérések
print("Path of the txt data file?:")
input_name = input()
print("Path of the NEW txt file (fitted params)?:")
output_name = input()
print("Do you want to define the p0 values?: (y/n)")
answ = input()
if answ == "y":
	print("a?:")
	p0_a = int(input())
	print("b?:")
	p0_b = int(input())
	print("c?:")
	p0_c = int(input())
	print("d?:")
	p0_d = int(input())
	p0 = [p0_a, p0_b, p0_c, p0_d]
else:
	p0 = [138.0, 512.0, 529.0,  -44.0]


# gauss görbét illesztő függvény
def func(x, a, b, c, d):
	y = a + (b-a)*np.exp(-(x-c)*(x-c)/(2*d*d))
	return y


# függvény fájlba íráshoz
def params_to_txt(name, data):
	with open(name, "a") as f:
		for i in range(len(data)):
			f.write(str(data[i])+"\n")


# adatok beolvasása a megadott fájlból:
df = pd.read_fwf(input_name, header=None)
x = df.iloc[:,:1].values
y = df.iloc[:,1:].values

x = np.array([float(i) for i in x])
y = np.array([float(i) for i in y])

# fittelés
popt, pcov = curve_fit(func, x, y, p0=p0)
xFit = np.arange(100,900,0.5)

# ábrázolás (jó látni rögtön, hogy mi a fittelés eredménye - mert mi van, ha rossz..?)
plt.plot(x,y,'*--', label="Adatpontok")
plt.plot(xFit,func(xFit, *popt), 'r', label="Illesztett görbe")

# illesztett paraméterek kiírása fájlba
params_to_txt(output_name, popt)
# illesztett paraméterek megjelenítése konzolon is
print(popt)

# grafikon egyéb dolgai:
plt.grid()
plt.legend()
plt.xlabel("x tengely [pixel]")
plt.ylabel("y tengely [pixel]")
plt.title("Gauss görbe illesztése az adatpontokra")
plt.show()
