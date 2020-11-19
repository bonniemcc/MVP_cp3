'''Checkpoint 3: Partial Differential Equations'''

import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from cahnhilliard import CahnHilliard 

def main():

    if len(sys.argv) != 6:
        print('User input: python3 cp3.py #sweeps n phi0 dx dt')
        quit()

    #user inputs lattice size, # of sweeps
    
    nsweeps = int(sys.argv[1]) 
    n = int(sys.argv[2])
    phi0 = float(sys.argv[3])
    dx = float(sys.argv[4])
    dt = float(sys.argv[5])

    a = 0.1
    M = 0.1
    k = 0.1
    e = 0.1

    z = CahnHilliard(n,phi0,dx,dt,a,M,k,e)

    #set up animation (pass lattice to plot)
    '''fig = plt.figure()
    im=plt.imshow(z.lattice, animated=True)#, cmap = 'rainbow')
    plt.colorbar()
    plt.title("")'''

    free_energy_list = []

    for i in range(nsweeps):
        z.update_phi()
        if i%500 == 0:
            free_energy_list.append(z.free_energy())
        '''if i > 100 and i%100 == 0:
            print(i)
            plt.cla()
            im=plt.imshow(z.lattice, animated=True)#, cmap = 'rainbow')
            plt.title("")
            plt.draw()
            plt.pause(0.0001)'''

    np.savetxt('free_energy_phi_0.dat',np.asarray(free_energy_list))
    t = np.linspace(0,nsweeps,(nsweeps/500)+1)
    plt.plot(t,free_energy_list)
    plt.xlabel('Time/ Frames')
    plt.ylabel('Free Energy')
    plt.title('phi0 = ',phi0)
    plt.savefig('free_energy_phi_0.png')

main()
