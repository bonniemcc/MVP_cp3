import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

phi = np.loadtxt('phi_slice.dat')

plt.imshow(phi, cmap='rainbow')
plt.gca().invert_yaxis()
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([0,10,20,30,40,49],[0,10,20,30,40,50])
plt.yticks([0,10,20,30,40,49],[0,10,20,30,40,50])
plt.show()
