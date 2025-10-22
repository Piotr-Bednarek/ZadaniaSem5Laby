import numpy as np  
import matplotlib.pyplot as plt 
import scipy.signal as sp
import numpy.linalg as nplin

from scipy.integrate import odeint
from plotfunc import plot_sets


def zad1_1_1():
    R1=2
    R2=1
    C1=1/2
    C2=4

    A=np.array([[-1/(R1*C1),0],[0,-1/(R2*C2)]])
    B=np.array([[1/(R1*C1)],[1/(R2*C2)]])
    C=[1,0]
    D=0

    K=np.hstack([B,A@B])
    if nplin.matrix_rank(K)==K.shape[0]:
        res="sterowalna"
    else:
        res="nie sterowalna"
    print(f'Rank= {nplin.matrix_rank(K)}, n = {K.shape[0]}, {res}')
    sys=sp.StateSpace(A,B,C,D)

    return A,B,C,D,sys

def zad1_1_2():
    R1=R2=R3=1
    C1=1
    C2=2
    C3=3

    A=np.array([[-1/(R1*C1),0,0],[0,-1/(R2*C2),0],[0,0,-1/(R3*C3)]])
    B=np.array([[1/(R1*C1)],[1/(R2*C2)],[1/(R3*C3)]])
    C=[1,0,0]
    D=0

    K=np.hstack([B,A@B,A@A@B])
    if nplin.matrix_rank(K)==K.shape[0]:
        res="sterowalna"
    else:
        res="nie sterowalna"

    print(f'Rank= {nplin.matrix_rank(K)}, n = {K.shape[0]}, {res}') #rank =2 a n=3 wiec nie jest sterowalna 
    sys=sp.StateSpace(A,B,C,D)

    return A,B,C,D,sys

def zad1_1_3():
    R=1
    L=0.1
    C=0.1

    A=np.array([[0,1/L,0,0],[-1/C,-1/(R*C),0,-1/(R*C)],[0,0,0,1/L],[0,-1/(R*C),-1/C,-1/(R*C)]])
    B=np.array([[0],[1/(R*C)],[0],[1/(R*C)]])
    C=[1,0,0,0]
    D=0

    K=np.hstack([B,A@B,A@A@B,A@A@A@B])
    if nplin.matrix_rank(K)==K.shape[0]:
        res="sterowalna"
    else:
        res="nie sterowalna"

    print(f'Rank= {nplin.matrix_rank(K)}, n = {K.shape[0]}, {res}') #rank = a n=4 wiec nie jest sterowalna 
    sys=sp.StateSpace(A,B,C,D)

    return A,B,C,D,sys

def zad1_1_4():
    R1=2
    R2=1
    L1=0.5
    L2=1
    C=3

    A=np.array([[-R1/L1,0,-1/C],[0,0,1/L2],[1/C,-1/C,-1/(R2*C)]])
    B=np.array([[1/L1],[0],[0]])
    C=[1,0,0]
    D=0

    K=np.hstack([B,A@B,A@A@B])
    if nplin.matrix_rank(K)==K.shape[0]:
        res="sterowalna"
    else:
        res="nie sterowalna"
    print(f'Rank= {nplin.matrix_rank(K)}, n = {K.shape[0]}, {res}') #rank =2 a n=3 wiec nie jest sterowalna 
    sys=sp.StateSpace(A,B,C,D)

    return A,B,C,D,sys


def zad1_3():
    t=np.arange(0,20,0.01)
    u2=np.full(len(t),2)
    u3 = np.sin(t) * (t >= 0) - 0.5

    _,_,_,_,sys1=zad1_1_1()
    _,_,_,_,sys2=zad1_1_2()
    _,_,_,_,sys3=zad1_1_3()
    _,_,_,_,sys4=zad1_1_4()

    t1,y1=sp.step(sys1)
    t2,y2=sp.step(sys2)

    t1p,y1p,_=sp.lsim(sys1,u2,T=t)
    t2p,y2p,_=sp.lsim(sys2,u2,T=t)

    t1s,y1s,_=sp.lsim(sys1,u3,T=t)

    plot_sets("systemy",[t1,y1,"system 1"],
              [t2,y2,"system2"],
              [t1p,y1p,"system 1 2u(t)"],
              [t2p,y2p,"system 2 2u(t)"]
              )
    
    plot_sets("systems with sine input",[t1s,y1s,"system 1 with sine input"])


def main():
    zad1_3()

if __name__=="__main__":
    main()