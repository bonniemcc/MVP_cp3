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
        omega = np.linspace(1,2,11)
        w = []
        for m in range(len(omega)):
            #reset lattice
            self.lattice = np.zeros((self.n,self.n,self.n))
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
                                #self.lattice[i,j,k] = newlattice[i,j,k]
                                #SOR
                                #diff = newlattice[i,j,k] - self.lattice[i,j,k]
                                #self.lattice[i,j,k] = self.lattice[i,j,k] + omega[m]*diff
                                self.lattice[i,j,k] = ((1-omega[m])*self.lattice[i,j,k]) + (omega[m]*newlattice[i,j,k])
                if method == 'j':
                    self.lattice = np.copy(newlattice)
                #sum old lattice, sum new lattice, then take absolute difference
                c = abs(np.sum(oldlattice) - np.sum(self.lattice))
                if c <= tolerance:
                    print(x)
                    break
            w.append(x)
        return w



