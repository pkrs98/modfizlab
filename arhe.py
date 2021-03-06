#2020-11-16
# terület és magasságszámítást megvalósító kódsor

import numpy as np
import pandas as pd
from sklearn import metrics

# adatfájlok beolvasása:
db=7
input_names = []
for i in range(db):
	print(str(i)+". txt file name?:")
	input_names = np.append(input_names, input())
print("Path of the NEW txt file?:")
output_name = input()

# függvény gauss görbe illesztéshez
def func(x,a,b,c,d):
	y = a + (b-a)*np.exp(-(x-c)*(x-c)/(2*d*d))
	return y

# függvény a kattintott koordináták txt fájlba való írásához
def write_txt(name, data1, data2):
	with open(name, "a") as f:
		f.write(str(data1)+"\t"+str(data2)+"\n")

# magasságok és területek kiszámítása
for i in range(len(input_names)):
	df = pd.read_fwf(input_names[i], header=None)
	a = np.array(df.iloc[0,:].values)
	b = np.array(df.iloc[1,:].values)
	c = np.array(df.iloc[2,:].values)
	d = np.array(df.iloc[3,:].values)
	x = np.arange(100,900,0.5)
	y = func(x, a, b, c, d)
	Height = float(max(y)-a)  	  #magasság (max y érték - alapvonal)
	area_tot = metrics.auc(x,y)   #teljes görbe alatti terület
	y_ = a*np.ones(len(x))        
	area_a = metrics.auc(x,y_)    #alapvonal alatti terület
	Area = area_tot - area_a
	write_txt(output_name, Area, Height)