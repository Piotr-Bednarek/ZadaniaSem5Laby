import numpy as np  
import matplotlib.pyplot as plt 
import scipy.signal as sp
import numpy.linalg as nplin

from scipy.integrate import odeint
from plotfunc import plot_sets
from scipy.signal import place_poles

def zad1_1_1():
    R1=2
    R2=4
    C1=1
    C2=1/2

    A=np.array([[-1/(R1*C1),0],[0,-1/(R2*C2)]])
    B=np.array([[1/(R1*C1)],[1/(R2*C2)]])
    C=[1,0]
    D=0

    K=np.hstack([B,A@B])
    if nplin.det(K)!=0:
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
    C1=[1,0,0]
    C2=[0,1,0]
    C3=[0,0,1]
    D=0

    K=np.hstack([B,A@B,A@A@B])
    print(f"K: {K}")
    if nplin.det(K)!=0:
        res="sterowalna"
    else:
        res="nie sterowalna"

    print(f'Rank= {nplin.matrix_rank(K)}, n = {K.shape[0]}, {res}') #rank =2 a n=3 wiec nie jest sterowalna 
    sys1=sp.StateSpace(A,B,C1,D)
    sys2=sp.StateSpace(A,B,C2,D)
    sys3=sp.StateSpace(A,B,C3,D)

    return A,B,C1,C2,C3,D,sys1,sys2,sys3,K

def zad1_1_3():
    R=1
    L=0.1
    C=0.1

    A=np.array([[0,1/L,0,0],[-1/C,-1/(R*C),0,-1/(R*C)],[0,0,0,1/L],[0,-1/(R*C),-1/C,-1/(R*C)]])
    B=np.array([[0],[1/(R*C)],[0],[1/(R*C)]])
    C=[1,0,0,0]
    D=0

    K=np.hstack([B,A@B,A@A@B,A@A@A@B])

    if nplin.det(K)!=0:
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
    if nplin.det(K)!=0:
        res="sterowalna"
    else:
        res="nie sterowalna"
    print(f'Rank= {nplin.matrix_rank(K)}, n = {K.shape[0]}, {res}') #rank =2 a n=3 wiec nie jest sterowalna 
    sys=sp.StateSpace(A,B,C,D)

    return A,B,C,D,sys

t=np.arange(0,20,0.01)
u=np.full(len(t),1)
u2=np.full(len(t),2)
u3 = np.sin(t) * (t >= 0) - 0.5

def sysinit():
    _,_,_,_,sys1,_=zad1_1_1()
    _,_,_,_,sys2=zad1_1_2()
    _,_,_,_,sys3=zad1_1_3()
    _,_,_,_,sys4=zad1_1_4()

    return sys1,sys2,sys3,sys4

def zad1_3_u():
    sys1,sys2,sys3,sys4=sysinit()

    t1,y1,_=sp.lsim(sys1,u,T=t)
    t2,y2,_=sp.lsim(sys2,u,t)
    t3,y3,_=sp.lsim(sys3,u,t)
    t4,y4,_=sp.lsim(sys4,u,t)

    plot_sets("odpowiedzi na skok jednostkowy o amplitudzie 1",
              [t1,y1,"system 1"],
              [t2,y2,"system 2"],
              [t3,y3,"system 4"],
              [t4,y4,"system 4"]
              )

def zad1_3_2u():
    sys1,sys2,sys3,sys4=sysinit()

    t1,y1,_=sp.lsim(sys1,u2,T=t)
    t2,y2,_=sp.lsim(sys2,u2,T=t)
    t3,y3,_=sp.lsim(sys3,u2,T=t)
    t4,y4,_=sp.lsim(sys4,u2,T=t)

    plot_sets("odpowiedzi na skok jednostkowy o amplitudzie 2",
              [t1,y1,"system 1"],
              [t2,y2,"system 2"],
              [t3,y3,"system 4"],
              [t4,y4,"system 4"]
              )
    
def zad1_3_sin():
    sys1,sys2,sys3,sys4=sysinit()

    t1,y1,_=sp.lsim(sys1,u3,T=t)
    t2,y2,_=sp.lsim(sys2,u3,T=t)
    t3,y3,_=sp.lsim(sys3,u3,T=t)
    t4,y4,_=sp.lsim(sys4,u3,T=t)

    plot_sets("odpowiedzi na sin(t)-1/2",
              [t1,y1,"system 1"],
              [t2,y2,"system 2"],
              [t3,y3,"system 4"],
              [t4,y4,"system 4"]
              )
    



def printCtrl(a,b,c,d,a1,b1,c1,d1):
    print(f"A regular: {a}\n A sterowalna: {a1}")
    print(f"B regular: {b}\n B sterowalna: {b1}")
    print(f"C regular: {c}\n C sterowalna: {c1}")
    print(f"D regular: {d}\n D sterowalna: {d1}")

def zad2_2():
    _,_,_,_,sysOG=zad1_1_1()

    t1,y1=sp.step(sysOG)
    t2,y2=sp.step()

    plot_sets("porownanie odpowiedzi z reprezentacji sterowalnej i jakiejkolwiek innej",
              [t1,y1,"og postac"],
              [t2,y2,"postac sterowalna"]
              )
    
    # zgodnie z zalozeniami postaci sie poktywaja kto by sie spodzieal to przeciez tylko inne liniowe reprezentacje tego samego pozdro

def plotsys2():
    A,B,C1,C2,C3,D,sys1,sys2,sys3,K=zad1_1_2() #sys1,3 to to samo tylko rozne c 
    #sys1s,sys2s,sys3s=sys2sterowalna() #sys1,3 to to samo tylko rozne c 

    t1sin,y1sin,_=sp.lsim(sys1,u3,T=t)
    t2sin,y2sin,_=sp.lsim(sys2,u3,T=t)
    t3sin,y3sin,_=sp.lsim(sys3,u3,T=t)

    t1,y1,_=sp.lsim(sys1,u,T=t)
    t2,y2,_=sp.lsim(sys2,u,t)
    t3,y3,_=sp.lsim(sys3,u,t)

    t12,y12,_=sp.lsim(sys1,u2,T=t)
    t22,y22,_=sp.lsim(sys2,u2,t)
    t32,y32,_=sp.lsim(sys3,u2,t)


    plot_sets("Wykresy przebiegów zmiennych stanu dla pobudzenia skokiem jednostkowym",[t1,y1,"x1"],[t2,y2,"x2"],[t3,y3,"x3"])
    plot_sets("Wykresy przebiegów zmiennych stanu dla pobudzenia sinusem",[t1sin,y1sin,"x1"],[t2sin,y2sin,"x2"],[t3sin,y3sin,"x3"],)
    plot_sets("Wykresy przebiegów zmiennych stanu dla pobudzenia skokiem jednostkowym o amplitudzie 2",[t12,y12,"x1"],[t22,y22,"x2"],[t32,y32,"x3"])

def obiektsvsr():
    #A,B,C1,C2,C3,D,sys1,sys2,sys3,K=zad1_1_2() #sys1,3 to to samo tylko rozne c 
    _,_,_,sys1s,sys2s,sys3s,_,_,_,_=sys2sterowalna() #sys1,3 to to samo tylko rozne c 

    t1sin,y1sin,_=sp.lsim(sys1s,u3,T=t)
    t2sin,y2sin,_=sp.lsim(sys2s,u3,T=t)
    t3sin,y3sin,_=sp.lsim(sys3s,u3,T=t)

    t1,y1,_=sp.lsim(sys1s,u,T=t)
    t2,y2,_=sp.lsim(sys2s,u,t)
    t3,y3,_=sp.lsim(sys3s,u,t)

    t12,y12,_=sp.lsim(sys1s,u2,T=t)
    t22,y22,_=sp.lsim(sys2s,u2,t)
    t32,y32,_=sp.lsim(sys3s,u2,t)

    plot_sets("Wykresy przebiegów zmiennych stanu dla pobudzenia skokiem jednostkowym REPREZENTACJA STEROWALNA",[t1,y1,"x1"],[t2,y2,"x2"],[t3,y3,"x3"])
    plot_sets("Wykresy przebiegów zmiennych stanu dla pobudzenia sinusem REPREZENTACJA STEROWALNA",[t1sin,y1sin,"x1"],[t2sin,y2sin,"x2"],[t3sin,y3sin,"x3"],)
    plot_sets("Wykresy przebiegów zmiennych stanu dla pobudzenia skokiem jednostkowym o amplitudzie 2 REPREZENTACJA STEROWALNA",[t12,y12,"x1"],[t22,y22,"x2"],[t32,y32,"x3"])

def sys2sterowalna():
    A, B, C1, C2, C3, D, sys1, sys2, sys3, K = zad1_1_2()

    char_poly = np.poly(A)  # Returns [1, a_{n-1}, ..., a_1, a_0]
    
    # Extract coefficients (skip the leading 1)
    a = char_poly[1:]  # [a_{n-1}, a_{n-2}, ..., a_1, a_0]
    
    # Step 2: Build As and Bs matrices in controllable canonical form (eq. 6)
    n = len(a)
    As = np.zeros((n, n))

    for i in range(n-1): #diagonala 
        As[i, i+1] = 1
    
    As[-1, :] = -a[::-1]  # Reverse order: [-a_0, -a_1, ..., -a_{n-1}]
    
    Bs = np.zeros((n, 1))
    Bs[-1, 0] = 1
    
    # Build controllability matrix of original system
    K_original = np.hstack([np.linalg.matrix_power(A, i) @ B for i in range(n)])
    
    # Build controllability matrix of canonical system
    K_canonical = np.hstack([np.linalg.matrix_power(As, i) @ Bs for i in range(n)])
    
    # Calculate P^{-1} and then P
    P_inv = K_original @ nplin.inv(K_canonical)
    P = nplin.inv(P_inv)
    
    # Step 4: Transform system to controllable form (eq. 10)
    An = P @ A @ P_inv
    Bn = P @ B
    Cn1 = C1 @ P_inv
    Cn2 = C2 @ P_inv
    Cn3 = C3 @ P_inv
    
    # Create state-space systems in controllable form
    sys1_new = sp.StateSpace(An, Bn, Cn1, D)
    sys2_new = sp.StateSpace(An, Bn, Cn2, D)
    sys3_new = sp.StateSpace(An, Bn, Cn3, D)
    
    # Return both original and transformed systems for comparison (task 2.2)
    return sys1, sys2, sys3, sys1_new, sys2_new, sys3_new, A, B, An, Bn

def zad3():
    sys1, sys2, sys3, sys1_new, sys2_new, sys3_new, A, B, An, Bn=sys2sterowalna()

    desired=[-1,-2,-5]

    res = place_poles(A,B,desired)
    K=res.gain_matrix

    print("Using scipy.signal.place_poles:")
    print(f"K = {K}")
    print(f"Achieved poles: {res.computed_poles}")


def main():
    zad3()

if __name__=="__main__":
    main()