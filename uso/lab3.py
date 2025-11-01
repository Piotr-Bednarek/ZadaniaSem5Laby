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
    C=[1,0,0]
    D=0

    K=np.hstack([B,A@B,A@A@B])
    print(f"K: {K}")
    if nplin.det(K)!=0:
        res="sterowalna"
    else:
        res="nie sterowalna"

    print(f'Rank= {nplin.matrix_rank(K)}, n = {K.shape[0]}, {res}') #rank =2 a n=3 wiec nie jest sterowalna 
    sys1=sp.StateSpace(A,B,C,D)

    return A,B,C,D,sys1,K

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

    
def printCtrl(a,b,c,d,a1,b1,c1,d1):
    print(f"A regular: {a}\n A sterowalna: {a1}")
    print(f"B regular: {b}\n B sterowalna: {b1}")
    print(f"C regular: {c}\n C sterowalna: {c1}")
    print(f"D regular: {d}\n D sterowalna: {d1}")

def obiektsvsr():
    A,B,C1,C2,C3,D,sys1,sys2,sys3,K=zad1_1_2() #sys1,3 to to samo tylko rozne c 
    _,_,_,sys1s,sys2s,sys3s,_,_,_,_=sys2sterowalna() #sys1,3 to to samo tylko rozne c 

    t12,y12,xout=sp.lsim(sys1s,u2,T=t)
    t1og,y1og,xoutog=sp.lsim(sys1,u2,t)

    t12sin,y12sin,xoutsin=sp.lsim(sys1s,u3,T=t)
    t1ogsin,y1ogsin,xoutogsin=sp.lsim(sys1,u3,t)
    
    plot_sets("Przeboeg zmiennych stanu sterowalna reprezentacja",[t12,xout[:,0],"x1"],[t12,xout[:,1],"x2"],[t12,xout[:,2],"x3"],)
    plot_sets("Przebeiegi zmiennych stanu og reprezentacja",[t1og,xoutog[:,0],"x1"],[t1og,xoutog[:,1],"x1"],[t1og,xoutog[:,2],"x3"])

    plot_sets("Przeboeg zmiennych stanu sterowalna reprezentacja",[t12sin,xoutsin[:,0],"x1"],[t12sin,xoutsin[:,1],"x2"],[t12sin,xoutsin[:,2],"x3"],)
    plot_sets("Przebeiegi zmiennych stanu og reprezentacja",[t1ogsin,xoutogsin[:,0],"x1"],[t1ogsin,xoutogsin[:,1],"x1"],[t1ogsin,xoutogsin[:,2],"x3"])


def wyjsciasys2():
    A,B,C,D,sys1,K=zad1_1_2()  

    t1,y1,x=sp.lsim(sys1,u,T=t)

    plot_sets("Wykresy przebiegów wyjść dla pobudzenia skokiem jednostkowym reprezentacja sterowalna",[t1,x[:,0],"x1"],[t1,x[:,1],"x2"],[t1,x[:,2],"x3"])

def sys2sterowalna():
    A, B, C, D, sys1, K = zad1_1_2()

    char_poly = np.poly(A)  # Returns [1, a_{n-1}, ..., a_1, a_0]

    a = char_poly[1:]  # [a_{n-1}, a_{n-2}, ..., a_1, a_0]
    #print(a)

    n = len(a)
    As = np.zeros((n, n))

    for i in range(n-1): #diagonala 
        As[i, i+1] = 1
    
    As[-1, :] = -a[::-1]  # Reverse order: [-a_0, -a_1, ..., -a_{n-1}]
    
    Bs = np.zeros((n, 1))
    Bs[-1, 0] = 1

    K_original = np.hstack([np.linalg.matrix_power(A, i) @ B for i in range(n)])
    K_canonical = np.hstack([np.linalg.matrix_power(As, i) @ Bs for i in range(n)])
    
    P_inv = K_original @ nplin.inv(K_canonical)
    P = nplin.inv(P_inv)
    #print(f"P={P}")
    
    An = P @ A @ P_inv
    Bn = P @ B
    Cn = C @ P_inv

    print(An)
    print(Bn)

    sys1_new = sp.StateSpace(An, Bn, Cn, D)
    
    # Return both original and transformed systems for comparison (task 2.2)
    return sys1, sys1_new, A, B, An, Bn

def zad3(): #
    sys1, sys1_new, A, B, An, Bn=sys2sterowalna()

    desired=[-1,-2,-5]

    res = place_poles(An,Bn,desired)
    K=res.gain_matrix

    print("Using scipy.signal.place_poles:")
    print(f"K = {K}")
    print(f"Achieved poles: {res.computed_poles}")

    return K

def lokowanieplot():
    _, _, A, B, An, Bn = sys2sterowalna()
    K = zad3()  # Returns gain matrix K
    
    # Equation (12): closed-loop system matrix
    # ẋ = (A - BK)x
    A_closed = An - Bn @ K  # ✓ CORRECT
    
    # For FREE RESPONSE (initial condition response):
    # No external input, so B_closed can be zero or omitted
    B_closed = np.zeros((3, 1))  # No input for free response
    
    C = np.array([[0, 0, 1]])  # Output third state
    D = np.array([[0]])
    
    sys_closed = sp.StateSpace(A_closed, B_closed, C, D)
    
    # Simulate with initial conditions (no input u)
    t = np.linspace(0, 10, 1000)
    u = np.zeros_like(t)  # Zero input
    x0 = [1, 0.5, -0.5]  # Non-zero initial conditions
    
    t, y, x_out = sp.lsim(sys_closed, u, t, X0=x0)

    plot_sets("odpowiedz układu zamkniętego",[t,x_out[:,0],"x0"],[t,x_out[:,1],"x1"],[t,x_out[:,2],"x2"])

def main():
    lokowanieplot()

if __name__=="__main__":
    main()