%the input vector (experiment):
x = [0;1;2;3;4;5;6];
y = [0.2;0.5;0.9;1.51;2.2;2.5;2.9];
%calculating the 'b' coefficient from model equation: y = bx 
% B = (X^T X)^(-1)(X^T Y); 
b =  (x'*y)/(x'*x);

%calculating b1 and b0
Xp = [ones(length(x),1) x];
Bp = Xp\y;
b0 = Bp(1);
b1 = Bp(2);

f(1) = figure(1);
clf;
ttext = sprintf('regression y = %.2fx',b); 
plot(x,y,'r*');
hold on;
yp = b*x;
plot(x,yp,'b');
xlabel('independent variable x (-)');
ylabel('dependent variable y (-)');
xlim([0 max(x)]);
ylim([0 max([y;yp])]);
legend('measured data points',ttext,'Location','Best');

f(2) = figure(2);
clf;
ttext2 = sprintf('regression y = %.2fx + %.2f',b1,b0); 
plot(x,y,'r*');
hold on;
yp2 = b1*x + b0;
plot(x,yp2,'b');
xlabel('independent variable x (-)');
ylabel('dependent variable y (-)');
xlim([0 max(x)]);
ylim([0 max([y;yp2])]);
legend('measured data points',ttext2,'Location','Best');

f(3) = figure(3);
clf;
plot(x,yp);
hold on;
plot(x,yp2);
xlabel('independent variable x (-)');
ylabel('dependent variable y (-)');
xlim([0 max(x)]);
ylim([0 max([yp;yp2])]);
legend(ttext,ttext2,'Location','Best');

SetFigureDimensionsAndPosition(f,500,250);

