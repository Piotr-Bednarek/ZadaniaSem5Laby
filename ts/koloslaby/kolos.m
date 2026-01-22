% Parametry przykładowe (np. masa-sprężyna-tłumik) [cite: 13]
m = 1; k = 1; b = 2;

A = [0 1; -k/m -b/m];
B = [0; 1/m];
C = [1 0];
D = 0;

sys = ss(A, B, C, D);

figure;
subplot(2,1,1); step(sys); title('Odpowiedź skokowa'); grid on;
subplot(2,1,2); initial(sys, [1; -5]); title('Odpowiedź na warunki początkowe'); grid on;

%%

% trzeba sobie zdefiniowac wlasne macierze A B C D 

% Macierze sterowalności i obserwowalności 
S = ctrb(A, B);
O = obsv(A, C);

% Sprawdzanie rzędu 
n = size(A, 1);
rzad_S = rank(S);
rzad_O = rank(O);

%% 


[num, den] = ss2tf(A, B, C, D);
G = tf(num, den);
disp('Transmitancja operatorowa G(s):');
printsys(num, den);

% nie wiem do konca o co w tym chodzi ale sie dowiem

% Diagonalizacja - postać Jordana [cite: 137, 142]
[M, A_jordan] = jordan(A); % M to macierz modalna (wektory własne)
[V, D_eig] = eig(A);       % Inna metoda wyznaczania wartości własnych

% Współczynniki wielomianu charakterystycznego [cite: 128]
wielomian = poly(A);

%%

% 1. Projektowanie regulatora (sprzężenie od stanu) [cite: 186, 243]
% Zadane bieguny układu zamkniętego (np. z pasma przenoszenia wc) [cite: 242]
wc = 10;
P_reg = [-wc, -wc]; % Dla układu 2 rzędu
K = acker(A, B, P_reg);

% 2. Projektowanie obserwatora Luenbergera [cite: 205, 256]
% Obserwator powinien być szybszy niż regulator (np. wo = 5-10 * wc) [cite: 270]
wo = 60;
P_obs = [-wo, -wo];
L = acker(A', C', P_obs)'; % Transpozycja wynika ze wzoru na Ho=A-LC [cite: 205, 256]


%%

% Wzmocnienie statyczne układu zamkniętego H = A - B*K [cite: 188, 246]
H = A - B*K;
k_stat = C * inv(-H) * B; % [cite: 246, 319]

% Współczynnik korygujący dla wartości zadanej r [cite: 250, 319]
k_inv = 1 / k_stat;

% Rozszerzenie układu o człon całkujący (eliminacja uchybu) [cite: 332, 360]
% Tworzenie macierzy rozszerzonych dla acker() [cite: 360]
n = size(A, 1);
A_rozsz = [A, zeros(n, 1); -C, 0];
B_rozsz = [B; 0];
P_rozsz = [-wc, -wc, -1.5*wc]; % Potrzebne 3 bieguny dla układu 2+1 rzędu

K_q = acker(A_rozsz, B_rozsz, P_rozsz);
K_new = K_q(1:end-1); % Wzmocnienia od stanu [cite: 360]
ki = -K_q(end);        % Wzmocnienie całkujące [cite: 360]