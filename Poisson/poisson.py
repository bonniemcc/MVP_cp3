'''Poisson class:
defines all useful functions for the model'''
import numpy as np

class Poisson(object):

    def __init__(self,n):
        self.n = n
        self.dx = 1
        self.dt = 1/6
        self.lattice = np.zeros((n,n,n))
        #single charge at centre of box
        self.rho = np.zeros((n,n,n))
        self.rho[int(n/2),int(n/2),int(n/2)] =1
        #wire through centre of box
        #self.rho = np.zeros((n,n,n))
        #self.rho[int(n/2),int(n/2),:] =1

    def sum_nn(self,i,j,k):
        t1 = self.lattice[(i+1)%self.n,j,k]
        t2 = self.lattice[(i-1)%self.n,j,k]
        t3 = self.lattice[i,(j+1)%self.n,k]
        t4 = self.lattice[i,(j-1)%self.n,k]
        t5 = self.lattice[i,j,(k+1)%self.n]
        t6 = self.lattice[i,j,(k-1)%self.n]
        return t1+t2+t3+t4+t5+t6
        
    def set_boundary(self):
        self.lattice[0,:,:] = 0
        self.lattice[:,0,:] = 0
        self.lattice[:,:,0] = 0
        self.lattice[self.n-1,:,:] = 0
        self.lattice[:,self.n-1,:] = 0
        self.lattice[:,:,self.n-1] = 0

    def update(self,method, nsweeps, tolerance):
        for x in range(nsweeps):
            newlattice = np.zeros([self.n,self.n,self.n])
            oldlattice = np.copy(self.lattice)
            for i in range(1,self.n-1):
                for j in range(1,self.n-1):
                    for k in range(1,self.n-1):
                        t1 = self.sum_nn(i,j,k)
                        t2 = ((self.dx)**2)*(self.rho[i,j,k])
                        newlattice[i,j,k] = (1/6)*(t1+t2)
                        if method == 'gs':
                            self.lattice[i,j,k] = newlattice[i,j,k]
            if method == 'j':
                self.lattice = np.copy(newlattice)
            #sum old lattice, sum new lattice, then take absolute difference
            c = abs(np.sum(oldlattice) - np.sum(self.lattice))
            if c <= tolerance:
                print(x)
                break

    def get_potential_slice(self):
        return self.lattice[:,:,int(self.n/2)]

    def get_electric_field_slice(self):
        x,y = np.gradient(self.get_potential_slice())
        return x,y

    def magnetic_field(self):
        Bx = np.zeros((self.n,self.n))
        By = np.zeros((self.n,self.n))
        for i in range (self.n):
            for j in range(self.n):
                Bx[i,j] = ((self.get_potential_slice()[i,(j+1)%self.n]-self.get_potential_slice()[i,(j-1)%self.n]))/(2*self.dx)
                By[i,j] = -((self.get_potential_slice()[(i+1)%self.n,j]-self.get_potential_slice()[(i-1)%self.n,j])/(2*self.dx))
        return Bx,By





