import numpy as np
import matplotlib.pyplot as plt

def f(x,A,v):
    return A/((x-v)**2+25)

# adatok; Ab, vb: benzol adatparok. Ad, vd: deuterizalt b. adatparok
Ab = [74.25, 46.646, 46.641, 6.639, 6.631, 3.381, 3.377]
vb = [694.57, 3197.86, 3197.86, 1524.41, 1524.78, 1066.43, 1066.82]
Ad = [40.009, 3.439, 3.444, 1.394, 1.393, 0.005, 0.001, 0.001, 26.23, 26.094, 0.003]
vd = [510.06, 830.77, 830.88, 1373.28, 1393.57, 2348.46, 2349.07, 2368.18, 2368.64, 2380.64]

# spektrum
x = np.linspace(400,4000,4000)

benzol = f(x,Ab[0],vb[0])
deut = f(x,Ad[0],vd[0])
for i in range(1,len(Ab)-1):
    benzol = benzol+f(x,Ab[i],vb[i])
    deut = deut+f(x,Ad[i],vd[i])

benzolN = benzol/max(benzol)
deutN = deut/max(deut)

fig, axs = plt.subplots(2)
fig.suptitle('Benzol és deuterizált benzol IR spektruma')
axs[0].plot(x, benzolN, label='benzol')
axs[1].plot(x, deutN, label='deuterizált\nbenzol')
fig.text(0.5, 0.04, 'hullámszám [cm^-1]', ha='center', va='center')
fig.text(0.06, 0.5, 'Abszorpció [%]', ha='center', va='center', rotation='vertical')
axs[0].legend()
axs[1].legend()
axs[0].grid()
axs[1].grid()
plt.savefig('IRspekt.png')