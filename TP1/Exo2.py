import numpy as np
import numpy.random as sim
import matplotlib.pyplot as plt


def F(u):  # F=Fx^-1
    y = 1 * (u < 1 / 5) + 2 * (1 / 5 <= u) * (u < 7 / 10) + 3 * (7 / 10 <= u) * (u < 19 / 20) + 4 * (u > 19 / 20)
    return y


def G(u):  # F=FY^-1nssemble de définition
    x = np.where(u > 1, 0,u)
    return -np.log(1 - x) / 2


N = 10  # la taille de l'echantillon

U = sim.ranf((N,))  # loi uniforme sur [0,1]
print(U)
X = F(U)
print(X)
V = sim.ranf((N,))  # loi uniforme sur [0,1]

Y = G(V)
Z = Y ** X

frq = np.arange(0, 4, dtype=float)
for i in range(0, 4):
    frq[i] = np.sum(1 * (X == i + 1)) / N

larg = 0.8  # lar rectangles
ax1 = np.array([1, 2, 3, 4])
hoistX = plt.bar(ax1, frq, larg, color='b')
plt.show()

ME = np.mean(Z)
print(ME)