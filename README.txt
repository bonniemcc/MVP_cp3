Checkpoint3

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Part1: Cahn Hilliard

input parameters:
# of sweeps = 100,000
n = 50
phi0 = 0.0, 0.5
dx = 1
dt = 2

note: 
    points were plotted every 500 sweeps

output files: 
    free_energy_phi_0.dat
    free_energy_phi_half.dat
    free_energy_phi_0.png
    free_energy_phi_half.png

data files contain a list of free energy values for intervals of 500 sweeps

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Part2: Poisson

input parameters:
# of sweeps = 10,000
n = 50
method = gs
tolerance = 0.0001

E field:

output files:
    phi_slice.dat
    phi_slice.png
    E_x.dat
    E_y.dat
    E_field.png
    E_field_normalised.png

B field:

output files:
    phi_slice.dat
    phi_slice.png
    B_x.dat
    B_y.dat
    B_field.png
    B_field_normalised.png

data files contain n x n arrays of values

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

SOR:

output files:
    SOR.dat
    SOR.png

note:
    for SOR # of sweeps was changed to 1,000
    for SOR the data file values are the convergence times (in sweeps) 
	which correspond to omega values of [1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]