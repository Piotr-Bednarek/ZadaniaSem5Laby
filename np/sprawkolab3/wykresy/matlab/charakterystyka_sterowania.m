% Charakterystyka sterowania silnika DC
clear all; close all; clc;

% Folder zapisu
if ~exist('../pdf', 'dir'), mkdir('../pdf'); end

%% Seria 1
data1 = readtable('../dane/charakterystyka-sterowania-1.csv');
f1 = figure('Name', 'Charakterystyka sterowania 1', 'NumberTitle', 'off', 'Position', [100, 100, 600, 450]);
hold on; grid on;
plot(data1.Ua, data1.omega_r, 'ro', 'MarkerSize', 6, 'MarkerFaceColor', 'r', 'DisplayName', 'Dane pomiarowe');
coeffs = polyfit(data1.Ua, data1.omega_r, 1);
x_fit = linspace(min(data1.Ua), max(data1.Ua), 100);
plot(x_fit, polyval(coeffs, x_fit), 'k-', 'LineWidth', 1.5, 'DisplayName', sprintf('Regresja: y = %.2fx + %.2f', coeffs(1), coeffs(2)));
title('Charakterystyka sterowania 1: \omega_r = f(U_a) dla T_e = const = 0', 'FontSize', 14);
xlabel('U_a [V]', 'FontSize', 12); ylabel('\omega_r [rad/s]', 'FontSize', 12);
set(gca, 'FontSize', 11);
legend('Location', 'best', 'FontSize', 10);
exportgraphics(f1, '../pdf/char_sterowania_1.pdf', 'ContentType', 'vector');

%% Seria 2
data2 = readtable('../dane/charakterystyka-sterowania-2.csv');
f2 = figure('Name', 'Charakterystyka sterowania 2', 'NumberTitle', 'off', 'Position', [150, 150, 600, 450]);
hold on; grid on;
plot(data2.Ua, data2.omega_r, 'bo', 'MarkerSize', 6, 'MarkerFaceColor', 'b', 'DisplayName', 'Dane pomiarowe');
coeffs2 = polyfit(data2.Ua, data2.omega_r, 1);
x_fit2 = linspace(min(data2.Ua), max(data2.Ua), 100);
plot(x_fit2, polyval(coeffs2, x_fit2), 'k-', 'LineWidth', 1.5, 'DisplayName', sprintf('Regresja: y = %.2fx + %.2f', coeffs2(1), coeffs2(2)));
title('Charakterystyka sterowania 2: \omega_r = f(U_a)', 'FontSize', 14);
xlabel('U_a [V]', 'FontSize', 12); ylabel('\omega_r [rad/s]', 'FontSize', 12);
set(gca, 'FontSize', 11);
legend('Location', 'best', 'FontSize', 10);
exportgraphics(f2, '../pdf/char_sterowania_2.pdf', 'ContentType', 'vector');
