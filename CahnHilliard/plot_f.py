import matplotlib.pyplot as plt
import numpy as np

f = np.loadtxt('phi0_0_final.dat')
ff = np.loadtxt('phi0_half_final.dat')

print(len(f))
print(len(ff))

t = np.linspace(1,len(f)*500,len(f))

plt.xlabel('time/sweeps')
plt.ylabel('free energy')
plt.title('phi0 = 0')
plt.plot(t,f)
plt.show()


plt.xlabel('time/sweeps')
plt.ylabel('free energy')
plt.title('phi0 = 0.5')
plt.plot(t,ff)
plt.show()
