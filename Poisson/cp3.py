'''Checkpoint 3: Partial Differential Equations'''

import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from poisson import Poisson

def main():

    if len(sys.argv) != 5:
        print('User input: python3 cp3.py #sweeps n method(j/gs) tolerance/error')
        quit()

    #user inputs lattice size, # of sweeps
    
    nsweeps = int(sys.argv[1]) 
    n = int(sys.argv[2])
    method = sys.argv[3]
    tolerance = float(sys.argv[4])

    z = Poisson(n)
    z.set_boundary()
    
    z.update(method, nsweeps, tolerance)
    #print(z.lattice)

    phi_slice = z.get_potential_slice()
    xgrad,ygrad = z.get_electric_field_slice()
    #xgrad,ygrad = z.magnetic_field()
    
    np.savetxt('phi_slice.dat',phi_slice)
    #np.savetxt('phi_slice_B.dat',phi_slice)
    np.savetxt('E_x.dat',xgrad)
    np.savetxt('E_y.dat',ygrad)
    #np.savetxt('B_x.dat',xgrad)
    #np.savetxt('B_y.dat',ygrad)

main()
