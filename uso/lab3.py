import numpy as np  
import matplotlib.pyplot as plt 
import scipy.signal as sp

from scipy.integrate import odeint
from plotfunc import plot_sets

def zad1_1_1():
    A=np.array([[-1/2,0],[0,-1/2]])
    B=np.array([[1/2],[1/2]])
    C=[1,0]
    D=0

    return A,B,C,D 

def zad1_1_2():
    pass

def zad1_1_3():
    pass

def zad1_1_4():
    pass

def zad1_2():
    A1,B1,C1,D1=zad1_1_1()
    K1=np.array([[B1,A1*B1]])
    print(K1)

def main():
    zad1_2()

if __name__=="__main__":
    main()