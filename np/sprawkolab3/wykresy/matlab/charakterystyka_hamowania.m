% Charakterystyka hamowania silnika DC 
clear all; close all; clc;

% Folder zapisu
if ~exist('../pdf', 'dir'), mkdir('../pdf'); end

%% Układ Obcowzbudny
data_obco = readtable('../dane/charakterystyka-hamowania-obcowzbudny.csv');
f1 = figure('Name', 'Hamowanie Obco', 'NumberTitle', 'off', 'Position', [100, 100, 600, 450]);
hold on; grid on;
plot(data_obco.omega_r, data_obco.Ia, 'bs', 'MarkerFaceColor', 'b', 'DisplayName', 'Dane pomiarowe');

% Regresja liniowa
coeffs = polyfit(data_obco.omega_r, data_obco.Ia, 1);
x_fit = linspace(min(data_obco.omega_r), max(data_obco.omega_r), 100);
plot(x_fit, polyval(coeffs, x_fit), 'b--', 'LineWidth', 1.5, 'DisplayName', sprintf('Regresja: y = %.5fx + %.2f', coeffs(1), coeffs(2)));

title('Hamowanie obcowzbudne: I_a = f(\omega_r)', 'FontSize', 14);
xlabel('\omega_r [rad/s]', 'FontSize', 12); ylabel('I_a [A]', 'FontSize', 12);
set(gca, 'FontSize', 11);
legend('Location', 'best', 'FontSize', 10);
exportgraphics(f1, '../pdf/char_hamowania_obco.pdf', 'ContentType', 'vector');

%% Układ Samowzbudny
data_samo = readtable('../dane/charakterystyka-hamowania-samowzbudny.csv');
f2 = figure('Name', 'Hamowanie Samo', 'NumberTitle', 'off', 'Position', [150, 150, 600, 450]);
hold on; grid on;
plot(data_samo.omega_r, data_samo.Ia, 'ro', 'MarkerFaceColor', 'r', 'DisplayName', 'Pomiar');
title('Hamowanie samowzbudne: I_a = f(\omega_r)', 'FontSize', 14);
xlabel('\omega_r [rad/s]', 'FontSize', 12); ylabel('I_a [A]', 'FontSize', 12);
set(gca, 'FontSize', 11);
legend('Location', 'best', 'FontSize', 10);
exportgraphics(f2, '../pdf/char_hamowania_samo.pdf', 'ContentType', 'vector');
