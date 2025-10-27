import numpy as np  
import matplotlib.pyplot as plt 
import scipy.signal as sp
import numpy.linalg as nplin

from scipy.integrate import odeint
from plotfunc import plot_sets


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
    sys3=sp.StateSpace(A,B,C2,D)

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
    

def zad2_1_sys1():
    A,B,C,D,_=zad1_1_1() 

    P=np.hstack([B,A@B]) #rank 2 wiec taki wzor

    A_c = nplin.inv(P) @ A @ P
    B_c = nplin.inv(P) @ B
    C_c = C @ P
    D_c = D

    sys=sp.StateSpace(A_c,B_c,C_c,D_c)

    #printCtrl(A,B,C,D,A_c,B_c,C_c,D_c)

    return sys


def zad2_1_sys2():
    A,B,C,D,_,K=zad1_1_2()

    ev=nplin.eigvals(K)
    print(ev)


    A_s=np.array([0,1,0],[0,0,1],[ev[0],ev[1],ev[2]])
    B_s=np.array([[0],[0],[1]])


    P=np.hstack([B,A@B,A@A@B])@np.hstack([B_s,A_s@B_s,A_s@A_s@B_s])

    A_c = nplin.inv(P) @ A @ P
    B_c = nplin.inv(P) @ B
    C_c = C @ P
    D_c = D

    printCtrl(A,B,C,D,A_c,B_c,C_c,D_c)

    return A_c,B_c,C_c,D_c


def zad2_1_sys3():
    A,B,C,D,_=zad1_1_3()

    P=np.hstack([B,A@B,A@A@B])

    A_c = nplin.inv(P) @ A @ P
    B_c = nplin.inv(P) @ B
    C_c = C @ P
    D_c = D

    #printCtrl(A,B,C,D,A_c,B_c,C_c,D_c)

def printCtrl(a,b,c,d,a1,b1,c1,d1):
    print(f"A regular: {a}\n A sterowalna: {a1}")
    print(f"B regular: {b}\n B sterowalna: {b1}")
    print(f"C regular: {c}\n C sterowalna: {c1}")
    print(f"D regular: {d}\n D sterowalna: {d1}")

def zad2_2():
    _,_,_,_,sysOG=zad1_1_1()
    sysSterowalne=zad2_1_sys1()

    t1,y1=sp.step(sysOG)
    t2,y2=sp.step(sysSterowalne)

    plot_sets("porownanie odpowiedzi z reprezentacji sterowalnej i jakiejkolwiek innej",
              [t1,y1,"og postac"],
              [t2,y2,"postac sterowalna"]
              )
    
    # zgodnie z zalozeniami postaci sie poktywaja kto by sie spodzieal to przeciez tylko inne liniowe reprezentacje tego samego pozdro

def zad3_3():
    A,B,C,D=zad2_1_sys2()

    K=np.hstack([B,A@B,A@A@B])

    print(K)
    #odpuszczam sobie to jest na 2 laby nie musze miec wszystkiego gotowego teraz 
    ev=nplin.eigvals(K)
    print(f"eigenvalues K systemu2: {ev}")

def plotsys2():
    A,B,C1,C2,C3,D,sys1,sys2,sys3,K=zad1_1_2() #sys1,3 to to samo tylko rozne c 

    t1,y1,_=sp.lsim(sys1,u3,T=t)
    t2,y2,_=sp.lsim(sys2,u3,T=t)
    t3,y3,_=sp.lsim(sys3,u3,T=t)

    plot_sets("Wykresy przebiegów zmiennych stanu",[t1,y1,"x1"],[t2,y2,"x2"],[t3,y3,"x3"])

def main():
    plotsys2()

if __name__=="__main__":
    main()