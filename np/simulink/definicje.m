%% Parametry
Ra = 3.0;
La = 10e-3;
kfi = 1.4;
J   = 25e-3;
Tl  = 0.0;
Ua  = 100;
b1  = 0.06;
tau = La/Ra;

% Uruchomienie symulacji
sim('untitled');

out.ia.time
out.ia.signals.values

t = out.ia.time;
ia_vec = out.ia.signals.values;
omega_vec = out.omega.signals.values;


% Pobranie danych z macierzy (ARRAY)


figure;

% --- Prędkość (lewa oś Y) ---
yyaxis left
plot(t, omega_vec, 'b', 'LineWidth', 2, color='[0.3010, 0.7450, 0.9330]');
ylabel('prędkość obrotowa \omega_r (obr/min)', color='[0.3010, 0.7450, 0.9330]', FontSize=14);
xlim([0.9 1.3])

ylim([0, 1.1*max(omega_vec)]);   % lekkie powiększenie zakresu

% --- Prąd (prawa oś Y) ---
yyaxis right
plot(t, ia_vec, 'r', 'LineWidth', 2, color = '[0.8500, 0.3250, 0.0980]');
ylabel('prąd twornika i_a (A)', color='[0.8500, 0.3250, 0.0980]', FontSize=14);
ylim([0, 1.1*max(ia_vec)]);

% --- Oś X i tytuł ---
xlabel('czas t (s)', FontSize=14);
title('Przebieg prędkości obrotowej oraz prądu twornika', FontSize=16);

% --- Legenda ---
legend('prędkość', 'prąd');

grid on;