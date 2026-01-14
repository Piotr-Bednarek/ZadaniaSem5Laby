% Charakterystyka hamowania silnika DC - T_H = f(omega_r)
clear all; close all; clc;

% Folder zapisu
if ~exist('../pdf', 'dir'), mkdir('../pdf'); end

% Stała silnika
k_phi = 1.8;

%% Układ Obcowzbudny - T_H = I_a * k_phi
data_obco = readtable('../dane/charakterystyka-hamowania-obcowzbudny.csv');
omega_r_obco = data_obco.omega_r * pi / 30;  % RPM -> rad/s
T_H_obco = data_obco.Ia * k_phi;

f1 = figure('Name', 'Hamowanie Obco', 'NumberTitle', 'off', 'Position', [100, 100, 600, 450]);
hold on; grid on;
plot(omega_r_obco, T_H_obco, 'bs', 'MarkerFaceColor', 'b', 'DisplayName', 'Dane pomiarowe');

% Regresja liniowa
coeffs = polyfit(omega_r_obco, T_H_obco, 1);
x_fit = linspace(min(omega_r_obco), max(omega_r_obco), 100);
plot(x_fit, polyval(coeffs, x_fit), 'b--', 'LineWidth', 1.5, 'DisplayName', sprintf('Regresja: y = %.5fx + %.2f', coeffs(1), coeffs(2)));

title('Hamowanie obcowzbudne: T_H = f(\omega_r)', 'FontSize', 14);
xlabel('\omega_r [rad/s]', 'FontSize', 12); ylabel('T_H [Nm]', 'FontSize', 12);
set(gca, 'FontSize', 11);
legend('Location', 'best', 'FontSize', 10);
exportgraphics(f1, '../pdf/char_hamowania_obco.pdf', 'ContentType', 'vector');

%% Układ Samowzbudny - T_H = P / omega_r
data_samo = readtable('../dane/charakterystyka-hamowania-samowzbudny.csv');
omega_r_samo = data_samo.omega_r * pi / 30;  % RPM -> rad/s
T_H_samo = data_samo.P ./ omega_r_samo;

f2 = figure('Name', 'Hamowanie Samo', 'NumberTitle', 'off', 'Position', [150, 150, 600, 450]);
hold on; grid on;
plot(omega_r_samo, T_H_samo, 'ro', 'MarkerFaceColor', 'r', 'DisplayName', 'Dane pomiarowe');

% Regresja (linia przerywana bez legendy)
coeffs_samo = polyfit(omega_r_samo, T_H_samo, 2);
x_fit_samo = linspace(min(omega_r_samo), max(omega_r_samo), 100);
plot(x_fit_samo, polyval(coeffs_samo, x_fit_samo), 'r--', 'LineWidth', 1.5, 'HandleVisibility', 'off');

title('Hamowanie samowzbudne: T_H = f(\omega_r)', 'FontSize', 14);
xlabel('\omega_r [rad/s]', 'FontSize', 12); ylabel('T_H [Nm]', 'FontSize', 12);
set(gca, 'FontSize', 11);
legend('Location', 'best', 'FontSize', 10);
exportgraphics(f2, '../pdf/char_hamowania_samo.pdf', 'ContentType', 'vector');
