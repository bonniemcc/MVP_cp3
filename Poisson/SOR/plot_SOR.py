import matplotlib.pyplot as plt
import numpy as np

w = np.linspace(1,2,11)

f = np.loadtxt('SOR.dat')

plt.xlabel('omega')
plt.ylabel('convergence time/sweeps')
plt.plot(w,f)
plt.show()
