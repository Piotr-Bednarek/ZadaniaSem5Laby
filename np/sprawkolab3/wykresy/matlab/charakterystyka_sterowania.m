% Charakterystyka sterowania silnika DC
clear all; close all; clc;

% Folder zapisu
if ~exist('../pdf', 'dir'), mkdir('../pdf'); end

%% Wczytanie danych
data1 = readtable('../dane/charakterystyka-sterowania-1.csv');
data2 = readtable('../dane/charakterystyka-sterowania-2.csv');

% Przeliczenie omega_r z RPM na rad/s
data1.omega_r = data1.omega_r * pi / 30;
data2.omega_r = data2.omega_r * pi / 30;

%% Wykres zbiorczy
f = figure('Name', 'Charakterystyki sterowania', 'NumberTitle', 'off', 'Position', [100, 100, 800, 600]);
hold on; grid on;

% Seria 1 (bez obciążenia)
plot(data1.Ua, data1.omega_r, 'ro', 'MarkerSize', 6, 'MarkerFaceColor', 'r', 'DisplayName', 'Dane pomiarowe (T_e = 0)');
coeffs1 = polyfit(data1.Ua, data1.omega_r, 1);
x_fit1 = linspace(min(data1.Ua), max(data1.Ua), 100);
plot(x_fit1, polyval(coeffs1, x_fit1), 'r--', 'LineWidth', 1.5, 'DisplayName', sprintf('Regresja (T_e = 0): y = %.2fx + %.2f', coeffs1(1), coeffs1(2)));

% Seria 2 (z obciążeniem 3.6)
plot(data2.Ua, data2.omega_r, 'bo', 'MarkerSize', 6, 'MarkerFaceColor', 'b', 'DisplayName', 'Dane pomiarowe (T_e = 3.6)');
coeffs2 = polyfit(data2.Ua, data2.omega_r, 1);
x_fit2 = linspace(min(data2.Ua), max(data2.Ua), 100);
plot(x_fit2, polyval(coeffs2, x_fit2), 'b--', 'LineWidth', 1.5, 'DisplayName', sprintf('Regresja (T_e = 3.6): y = %.2fx + %.2f', coeffs2(1), coeffs2(2)));

title('Charakterystyka sterowania: \omega_r = f(U_a) dla różnych obciążeń', 'FontSize', 14);
xlabel('U_a [V]', 'FontSize', 12); ylabel('\omega_r [rad/s]', 'FontSize', 12);
set(gca, 'FontSize', 11);
legend('Location', 'best', 'FontSize', 10);

exportgraphics(f, '../pdf/char_sterowania_zbiorcza.pdf', 'ContentType', 'vector');
