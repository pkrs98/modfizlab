import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

# adatfájlok beolvasása:
db=7
txt_names = []
for i in range(db):
	print(str(i)+". txt file name?:")
	txt_names = np.append(txt_names, input())

# függvény gauss görbe illesztéshez
def func(x,a,b,c,d):
	y = a + (b-a)*np.exp(-(x-c)*(x-c)/(2*d*d))
	return y

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "brown"]

# nyers adatpontok ábrázolása:
for i in range(len(txt_names)):
	df = pd.read_fwf(txt_names[i],header=None)
	a = np.array(df.iloc[0,:].values)
	b = np.array(df.iloc[1,:].values)
	c = np.array(df.iloc[2,:].values)
	d = np.array(df.iloc[3,:].values)
	xFit = np.arange(100,900,0.5)
	yFit = func(xFit, a, b, c, d)
	plt.plot(xFit, yFit, '--', color=colors[i], label="t"+str(i)+" görbe")


# grafikon egyéb dolgai:
plt.grid()
plt.legend()
plt.xlabel("x tengely [pixel]")
plt.ylabel("y tengely [pixel]")
plt.title("Illesztett görbék különböző időpillanatokban")
plt.show()