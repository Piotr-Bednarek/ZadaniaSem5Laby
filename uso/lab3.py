import numpy as np  
import matplotlib.pyplot as plt 
import scipy.signal as sp
import numpy.linalg as nplin

from scipy.integrate import odeint
from plotfunc import plot_sets


def zad1_1_1():
    A=np.array([[-1/2,0],[0,-1/2]])
    B=np.array([[1/2],[1/2]])
    C=[1,0]
    D=0

    K1=np.hstack([B,A@B])
    print(nplin.matrix_rank(K1))
    sys=sp.StateSpace(A,B,C,D)

    return A,B,C,D,sys

def zad1_1_2():
    A=np.array([[-1,0,0],[0,-1/2,0],[0,0,-1/3]])
    B=np.array([[1],[1/2],[1/3]])
    C=[1,0,0]
    D=0

    K1=np.hstack([B,A@B])
    print(nplin.matrix_rank(K1)) #rank =2 a n=3 wiec nie jest sterowalna 
    sys=sp.StateSpace(A,B,C,D)

    return A,B,C,D,sys

def zad1_1_3():
    pass

def zad1_1_4():
    pass

def zad1_3():
    t=np.arange(0,20,0.01)
    u2=np.full(len(t),2)
    _,_,_,_,sys1=zad1_1_1()
    _,_,_,_,sys2=zad1_1_2()

    t1,y1=sp.step(sys1)
    t2,y2=sp.step(sys2)

    t1p,y1p,_=sp.lsim(sys1,u2,T=t)
    t2p,y2p,_=sp.lsim(sys2,u2,T=t)

    plot_sets([t1,y1,"system 1"],
              [t2,y2,"system2"],
              [t1p,y1p,"system 1 2u(t)"],
              [t2p,y2p,"system 2 2u(t)"]
              )


def main():
    zad1_3()

if __name__=="__main__":
    main()