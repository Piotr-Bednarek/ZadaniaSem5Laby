s=tf('s');

R=20e3;
C1=22e-6;
C2=44e-6;

a=1/(R^2*C1*C2);

H1=a/(s^2+(2/(R*C2))*s+a);

ltiview(H)

C=22e-6;
R1g=20e3;
R2g=10e3;

%H2=s^2/(s^2+2/(R1g*C)*s+1/(R1g*R2g*C^2))

%ltiview(H2)

