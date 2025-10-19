import numpy as np  
import matplotlib.pyplot as plt 
import scipy.signal as sp

from scipy.integrate import odeint

from plotfunc import plot_sets

kp = 2
T = 10

def zad2():
    # G(s) = kp/(T*s + 1)
    num = [kp]
    den = [T, 1]
    system = sp.TransferFunction(num, den)
    t, y = sp.step(system)
    title= "Transfer function"

    return t,y,title 
    
    '''
    print(f"Transfer function: {system}")
    print(f"Final value: {y[-1]:.3f}")
    print(f"Time constant (T): {T}s")
    '''

def zad2_3():
    A=-1/T
    B=kp/T
    C=1
    D=0

    G = sp.StateSpace(A,B,C,D)
    t, y = sp.step(G)
    title="State space"

    return t,y,title

def model(y,t): #zad2_4
    u=1.0
    dydt=(kp*u-y)/T
    return dydt

def zad2_5():
    title="diff eq"
    y0=0

    t=np.arange(0, 70, 0.01)
    ydot=odeint(model, y0, t)

    return t,ydot,title



def PlotStepResponse():
    t1,y1,title1=zad2_3() #state space 
    t2,y2,title2=zad2() # transfer function 
    t3,y3,title3=zad2_5()# diff eq


    plt.figure(figsize=(10, 6))
    plt.plot(t1, y1, 'b-', linewidth=10, label=f'{title1}')
    plt.plot(t2,y2,'r-', linewidth=5, label=f'{title2}')
    plt.plot(t3,y3,'g-', linewidth=2, label=f'{title3}')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.title('Step response of the same system in diffrent notations')
    plt.legend()
    plt.show()

    plot_sets([t1,y1,title1])

    #odpowiedzi takie same (kto by sie spodziewal)
    #forma reprezentacji nie zmienia wyjscia system reaguje tak samo na jednakowe pobudzenia 

R=12
L=1
c=100e-6

def zad3_1():
    num=[1,0]
    dem=[L,R,1/c]
    sys=sp.TransferFunction(num,dem)
    
    t,y=sp.step(sys)
    title="transfer function"

    return t,y,title,sys

def zad3_2():
    A=np.array([[0,1],[-1/(L*c),-R/L]])
    B=np.array([[0],[1/L]])
    C=np.array([[0,1]])
    D=np.array([[0]])

    G = sp.StateSpace(A,B,C,D)
    t, y = sp.step(G)
    title="State space"

    return t,y,title,G

def zad3_3():
    t1,y1,title1,sys1=zad3_1()
    t2,y2,title2,sys2=zad3_2()

    print(f'RLC circut in original tf: {sys1}')

    sys2tf=sp.ss2tf(sys2)

    print(f'RLC circut in tf from state space : {sys2tf}')

    print(f'RLC circut in original state space: {sys2}')

    sys1ss=sp.tf2ss(sys1)

    print(f'RLC circut in state space from tf: {sys1ss}')

#bron boze nie sa przeciez to kombinacje liniowe 
#da sie bo to kombinacje liniowe pozdro 

def PlotRlcResponse():
    t1,y1,title1,sys1=zad3_1()
    t2,y2,title2,sys2=zad3_2()

    plt.figure(figsize=(10, 6))
    plt.plot(t1, y1, 'b-', linewidth=5, label=f'{title1}')
    plt.plot(t2,y2,'r-', linewidth=2, label=f'{title2}')
    #plt.plot(t3,y3,'g-', linewidth=2, label=f'{title3}')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(left=0)
    #plt.ylim(bottom=0)
    plt.title('Step response of the same system model in TF and state space')
    plt.legend()
    plt.show()


def zad4_1():
    L=0.5
    m=1
    d=0.1

    J=(1/3) * m * L**2

    A=np.array([[0,1],[0,-d/J]])
    B=np.array([[0],[1/J]])
    C=np.array([[1,0]])
    D=np.array([[0]])

    sys=sp.StateSpace(A,B,C,D)

    t,y=sp.step(sys,None,np.arange(0,50,0.01))

    title="manipulator response"
    return t,y,title,sys

def PlotManipulatorStepResponse():
    t1,y1,title1,sys1=zad4_1()

    plt.figure(figsize=(10, 6))
    plt.plot(t1, y1, 'b-', linewidth=5, label=f'{title1}')
    #plt.plot(t2,y2,'r-', linewidth=2, label=f'{title2}')
    #plt.plot(t3,y3,'g-', linewidth=2, label=f'{title3}')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(left=0)
    #plt.ylim(bottom=0)
    plt.title('Step response of manipulator')
    plt.legend()
    plt.show()

def zad4_2():
    _,_,_,sys=zad4_1()

    t=np.arange(0,50,0.01)
    tau=np.arange(0,50,0.01)

    t,res,x=sp.lsim(sys,tau,t,X0=None,)

    title="ramp response"

    return t,res,title

def PlotManipulatorRampResponse():
    t,y,title=zad4_2()

    plt.figure(figsize=(10, 6))
    plt.plot(t, y, 'b-', linewidth=5, label=f'{title}')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(left=0)
    #plt.ylim(bottom=0)
    plt.title('Step response of manipulator')
    plt.legend()
    plt.show()

def PlotBodeCharacteristic():
    t,y,title,sys=zad4_1()

    w,mag,phase=sp.bode(sys)

    plt.semilogx(w, mag)
    plt.semilogx(w, phase)
    plt.grid(True)
    plt.xlabel("frequency[Hz]")
    plt.ylabel("Amplitude[dB]")
    plt.show()


def main():
    PlotStepResponse()
    #PlotRlcResponse()
    #PlotManipulatorStepResponse()
    #PlotManipulatorRampResponse()
    #PlotBodeCharacteristic()
    pass

if __name__=="__main__":
    main()
