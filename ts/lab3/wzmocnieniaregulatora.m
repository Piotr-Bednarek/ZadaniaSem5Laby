tend=10;

R=3;
La=0.05;
km=2;
J=0.11;
c=0;

A=[-R/La,-km/La;km/J,c/J];
B=[1/La;0];
C=[0,1];
kappa=0.05;

ksi= -log(kappa)/(sqrt(pi^2+log(kappa)^2))

omega = 1/(ksi*5)*log(1/(0.01*sqrt(1-ksi^2)))

wc= 20;

%P= roots([1, 2*ksi*omega, omega^2]);
P=[-2*wc -2*wc];
K=acker(A,B,P)

H=A-B*K;

% Calculate the closed
kstat = C*(-H)^-1*B

