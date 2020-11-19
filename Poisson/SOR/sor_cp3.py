'''Checkpoint 3: Partial Differential Equations'''

import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sor_poisson import Poisson

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
    
    SOR = z.update(method, nsweeps, tolerance)

    np.savetxt('SOR.dat',SOR)
    

main()