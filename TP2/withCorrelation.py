import numpy as np
import numpy.random as sim # simulate r.v
import matplotlib.pyplot as plt # graphiques

T=3; alpha=0.75; theta=0.015; beta=0.15
r0=0.02
n=1000;pas=T/n; N=100
r=r0*np.ones((n+1,N))
integ=np.zeros((n+1,N))
coeffAct=np.ones((n+1,N))


S0=50
TildeS=S0*np.ones((n+1,N))
S=S0*np.ones((n+1,N))
PayoffAct=[]
MoyS=[]
K=S0/2
 # Cette variable sert a stocKé l'esperence de l'expenentiel de l'intégrale pour ensuite, calculer ça moyenne




def sig(t,x):
    y=0.2*np.sin(2*3.1415*t/T)+t+1/(1+x**2)
    return y

def call(x,K):
    return max(x-K,0)

for j in range(N):
    for i in range(1,n+1):
        r[i,j]=r[i-1,j]+alpha*(theta-r[i-1,j])*pas+beta*np.sqrt(abs(r[i-1,j]))*np.sqrt(pas)*sim.randn()
        integ[i,j]=pas*np.sum(r[:i-1,j])
        coeffAct[i,j]=np.exp(-integ[i,j])
        TildeS[i,j]=TildeS[i-1,j]+sig(pas*(i-1),TildeS[i-1,j])*TildeS[i-1,j]*np.sqrt(pas)*sim.randn()
        S[i,j]=TildeS[i,j]*np.exp(integ[i,j])
    MoyS.append(np.mean(S[:,j]))
    aux=call(MoyS[-1],K)
    aux1=aux*coeffAct[n,j]
    PayoffAct.append(aux1)

prix=np.mean(PayoffAct)
print("Prix=", prix)
