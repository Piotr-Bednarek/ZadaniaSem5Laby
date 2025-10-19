A=[2,0;4,-3];
B=[5;0];
C=[1,0];
D=[0];

s=ctrb(A,B);
o=obsv(A,C);

rank(s)
rank(o)

A1=[1,0,2;0,1,0;0,0,-3];
B1=[0;1;0];
C1=[2,0,-1];
D1=[3];

s1=ctrb(A1,B1);
o1=obsv(A1,C1);

rank(s1)
rank(o1)


[num,den]=ss2tf(A1,B1,C1,D1)


sys2ss=tf2ss(num,den)


%%


syms R L k J b real

A=[-R/k,-k/L;k/J,-b/J];
B=[1/L;0];
C=[0,1];
D=0;

P=[b/k,J/k;1,0];











