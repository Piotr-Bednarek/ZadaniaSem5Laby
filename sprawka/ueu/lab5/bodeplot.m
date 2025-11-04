s=tf('s');

R=20e3;
C1=22e-6;
C2=44e-6;

a=1/(R^2*C1*C2);

H1=a/(s^2+(2/(R*C2))*s+a);

ltiview(H1)

C=22e-6;
R1g=20e3;
R2g=10e3;

%H2=s^2/(s^2+2/(R1g*C)*s+1/(R1g*R2g*C^2))

%ltiview(H2)

%%

% Load all three datasets
%data1 = readmatrix('data/1.csv', 'NumHeaderLines', 2);
%data5 = readmatrix('data/5.csv', 'NumHeaderLines', 2);
%data10 = readmatrix('data/10.csv', 'NumHeaderLines', 2);


% Create figure
figure;

% Magnitude comparison
subplot(2,1,1)
semilogx(data1(:,1), data1(:,2), 'b-', 'LineWidth', 2, 'DisplayName', 'Rp= 1kOhm')
hold on
semilogx(data5(:,1), data5(:,2), 'g-', 'LineWidth', 2, 'DisplayName', 'Rp= 5kOhm')
semilogx(data10(:,1), data10(:,2), 'r-', 'LineWidth', 2, 'DisplayName', 'Rp= 10kOhm')
grid on
xlabel('Frequency (Hz)')
ylabel('Gain (dB)')
title('Magnitude Response - Comparison')
legend('Location', 'best')
hold off

% Phase comparison
subplot(2,1,2)
semilogx(data1(:,1), data1(:,3), 'b-', 'LineWidth', 2, 'DisplayName', 'Rp= 1kOhm')
hold on
semilogx(data5(:,1), data5(:,3), 'g-', 'LineWidth', 2, 'DisplayName', 'Rp= 5kOhm')
semilogx(data10(:,1), data10(:,3), 'r-', 'LineWidth', 2, 'DisplayName', 'Rp= 10kOhm')
grid on
xlabel('Frequency (Hz)')
ylabel('Phase (degrees)')
title('Phase Response - Comparison')
legend('Location', 'best')
hold off



