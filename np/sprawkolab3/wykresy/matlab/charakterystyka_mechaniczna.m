% Charakterystyka mechaniczna silnika DC
clear all; close all; clc;

% Folder zapisu
if ~exist('../pdf', 'dir'), mkdir('../pdf'); end

% Stała maszynowa k*phi
k_phi = 1.8;

%% Ua = 150V
data150 = readtable('../dane/charakterystyka-mechaniczna-150V.csv');
% Przeliczenie prądu na moment elektromagnetyczny Te = k_phi * Ia
data150.Te = k_phi * data150.Ia;

f1 = figure('Name', 'Mechaniczna 150V', 'NumberTitle', 'off', 'Position', [100, 100, 600, 450]);
hold on; grid on;
% Wykres omega_r = f(Te)
plot(data150.Te, data150.omega_r, 'mo', 'MarkerFaceColor', 'm', 'DisplayName', 'Pomiar 150V');
coeffs150 = polyfit(data150.Te, data150.omega_r, 1);
plot(data150.Te, polyval(coeffs150, data150.Te), 'k-', 'LineWidth', 1.5, 'DisplayName', sprintf('Regresja: y = %.2fx + %.2f', coeffs150(1), coeffs150(2)));

title('Charakterystyka mechaniczna: \omega_r = f(T_e) dla U_a = 150V', 'FontSize', 13);
xlabel('Moment elektromagnetyczny T_e', 'FontSize', 12); 
ylabel('\omega_r [rad/s]', 'FontSize', 12); 
legend('Location', 'best', 'FontSize', 10);
set(gca, 'FontSize', 11);
exportgraphics(f1, '../pdf/char_mechaniczna_150V.pdf', 'ContentType', 'vector');

%% Ua = 200V
data200 = readtable('../dane/charakterystyka-mechaniczna-200V.csv');
% Przeliczenie prądu na moment elektromagnetyczny Te = k_phi * Ia
data200.Te = k_phi * data200.Ia;

f2 = figure('Name', 'Mechaniczna 200V', 'NumberTitle', 'off', 'Position', [150, 150, 600, 450]);
hold on; grid on;
% Wykres omega_r = f(Te)
plot(data200.Te, data200.omega_r, 'co', 'MarkerFaceColor', 'c', 'DisplayName', 'Pomiar 200V');
coeffs200 = polyfit(data200.Te, data200.omega_r, 1);
plot(data200.Te, polyval(coeffs200, data200.Te), 'k-', 'LineWidth', 1.5, 'DisplayName', sprintf('Regresja: y = %.2fx + %.2f', coeffs200(1), coeffs200(2)));

title('Charakterystyka mechaniczna: \omega_r = f(T_e) dla U_a = 200V', 'FontSize', 13);
xlabel('Moment elektromagnetyczny T_e', 'FontSize', 12); 
ylabel('\omega_r [rad/s]', 'FontSize', 12); 
legend('Location', 'best', 'FontSize', 10);
set(gca, 'FontSize', 11);
exportgraphics(f2, '../pdf/char_mechaniczna_200V.pdf', 'ContentType', 'vector');
