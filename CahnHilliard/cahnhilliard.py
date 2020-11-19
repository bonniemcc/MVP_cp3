'''Cahn Hillard class:
defines all useful functions for the model'''
import numpy as np

class CahnHilliard(object):

    def __init__(self,n,phi0,dx,dt,a,M,k,noise):
        self.n = n
        self.phi0 = phi0
        self.dx = dx
        self.dt = dt
        self.M = M
        self.a = a 
        self.k = k
        self.lattice = np.random.normal(phi0, noise, (n,n))

    def calc_mu(self,i,j):
        c1 = -self.a*(self.lattice[i,j]) + self.a*(self.lattice[i,j])**3
        c2 = -(self.k/self.dx**2.)*(self.lattice[(i+1)%self.n,j]+self.lattice[(i-1)%self.n,j]+self.lattice[i,(j+1)%self.n]+self.lattice[i,(j-1)%self.n]-4*self.lattice[i,j])
        return  c1+c2  

    def update_phi(self):
        newlattice = np.zeros([self.n,self.n])
        for i in range(self.n):
            for j in range(self.n):
                newlattice[i,j] = self.lattice[i,j] + ((self.dt*self.M)/(self.dx**2))*(self.calc_mu((i+1)%self.n,j)+self.calc_mu((i-1)%self.n,j)
                +self.calc_mu(i,(j+1)%self.n)+self.calc_mu(i,(j-1)%self.n) - 4*(self.calc_mu(i,j)))
        self.lattice = np.copy(newlattice)

    def free_energy(self):
        f_list = [] 
        #f = 0.0
        gx,gy = np.gradient(self.lattice)
        for i in range(self.n):
            for j in range(self.n):
                f = -(self.a/2)*(self.lattice[i,j]**2) +(self.a/4)*(self.lattice[i,j]**4) +(self.k/2)* ((np.sqrt((gx[i])**2 +(gy[j])**2))**2)
                f_list.append(f)
        return np.sum(f_list)