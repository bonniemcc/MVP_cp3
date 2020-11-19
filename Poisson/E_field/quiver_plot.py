import numpy as np 
import matplotlib.pyplot as plt 

U = np.loadtxt('E_x.dat')
V = np.loadtxt('E_y.dat')

E = np.zeros((len(U),len(U)))

for i in range(len(U)):
    for j in range(len(U)):
        E[i,j] = np.sqrt((U[i,j])**2 + (V[i,j])**2)

x = np.arange(1,len(U)+1,1)
y = np.arange(1,len(U)+1,1)

U = U/E
V = V/E

X,Y = np.meshgrid(x,y)

plt.quiver(Y, X, U, V)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
