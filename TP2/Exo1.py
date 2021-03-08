import numpy as np
import numpy.random as sim
import matplotlib.pyplot as plt

T=4;n=1000;N=1 # nombre de trajectoirs
pas =T/n

S0=10;sig=0.2;nu=0.08
B=np.zeros((n+1,N))
#Bt0=0 déja initialisé avec la matrice B.zero

for j in range(N):
    for i in range(1,n+1):
        B[i,j]=B[i-1,j]+np.sqrt(pas)*sim.randn()

dates=np.linspace(0,T,n+1) # n+1 dates
graph=plt.plot(dates,B)
plt.show()