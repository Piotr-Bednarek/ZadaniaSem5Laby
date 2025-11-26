%THIS IS AN EXAMPLE SCRIPT THAT LOAD AND PROCESS DATA FROM 
%TEKTRONIX OSCILLOSCOPES SAVED IN CSV TABLE

%v4 -- version fits 'readmatrix' function procesed in Matlab 2022
%'readmatrix' is used in 'Load_CSV_MSO23_M22' and differs in 'header_size' variable.

%Set 'filtering_option' value to select signal to filter.
%Filtering results are presented in the figure 4. 
  %1 -- speed
  %2 -- current
  %3 -- voltage
  filtering_option = 3;
  
%select proper channel order (according to the real connection):
current_channel = 1;
speed_channel   = 2;
voltage_channel = 3;
  
  
%figure 1 -- simulation results saved previously in .mat file 
%figure 2 -- experimental waveform taken from TEK DSO4000 oscilloscope 
%fiGure 3 --    -||-               taken from TEK MSO23 oscilloscope
load('out'); %it base on the previously 
%saved workspace variables by using 
%"save('out','out')" command

f(1) = figure(1); %load figure number 1 and read its handle
clf; %clear figure (if existed before)

%cutoff the waveform in time base:
time_start = 0.05;
time_end = 0.4;
start_stop_subindex = cutoff_in_time_scale(out.tout, time_start, time_end);

yyaxis left;
plot(out.tout(start_stop_subindex), out.speed(start_stop_subindex), 'b-', 'LineWidth',1);
xlabel('czas t (s)');
ylabel('prêdkoœæ obrotowa \omega_r (rpm)');

yyaxis right;
plot(out.tout(start_stop_subindex), out.current(start_stop_subindex), 'r-', 'LineWidth',1);
ylabel('pr¹d twornika i_a (A)');

grid on;
xlim([time_start, time_end]);
 legend('prêdkoœæ','pr¹d','Location', 'Best');
 
%loads data from CSV in DSO4000 format 
data = Load_CSV_DSO4000('test.csv',2);
data_len = length(data);

f(2) = figure(2); %load figure number 2 and read its handle
clf; %clear figure (if existed before)
yyaxis left;
plot(data(:,1),data(:,2)*1000, 'b-', 'LineWidth',1);
xlabel('czas t (s)');
ylabel('prêdkoœæ obrotowa \omega_r (rpm)');

yyaxis right;
plot(data(:,1),data(:,3)*10, 'r-', 'LineWidth',1);
ylabel('pr¹d twornika i_a (A)');
grid on;
legend('prêdkoœæ','pr¹d','Location', 'Best');

%loads data from CSV in column format of MSO23 
data = Load_CSV_MSO23_M22('50v_ALL.csv',3);
%set the time offset to zero:
data(:,1)=data(:,1)-data(1,1);

f(3) = figure(3); %load figure number 3 and read its handle
clf; %clear figure (if existed before)
plot(data(:,1),data(:,current_channel+1)*4, 'LineWidth',1);
hold on;
plot(data(:,1),data(:,speed_channel+1)*4, 'LineWidth',1);
hold on;
plot(data(:,1),data(:,voltage_channel+1), 'LineWidth',1);
legend('pr¹d 2,5 A/V','prêdkoœæ 250 rpm/V','napiêcie 100 V/V');
xlabel('czas t (s)');
ylabel('pr¹d, prêdkoœæ, napiêcie');
grid on;


%compute order:
  %smaple rate:
     fs = length(data)/(data(end,1)-data(1,1));
  %object dynamic:
     fo = 10e+3;
  %filter order:
     Nf = round(fs/fo);


f(4) = figure(4); %load figure number 4 and read its handle
clf; %clear figure (if existed before)
switch filtering_option
    %speed
    case 1 
%speed input data:
speed_data = data(:,speed_channel+1).*1000;
plot(data(:,1),speed_data, 'LineWidth',3);

speed_data_mflt = medfilt1(speed_data,Nf);
hold on;
plot(data(:,1),speed_data_mflt, 'LineWidth',2);
speed_data_sgflt = sgolayfilt(speed_data_mflt,1,13*Nf);
hold on;
plot(data(:,1),speed_data_sgflt, 'LineWidth',1);
legend('RAW','MEDF','SGF');
xlabel('czas t (s)');
ylabel('prêdkoœæ \omega_r (obr/min)');
grid on;
    %current
    case 2
current_data = data(:,current_channel+1).*10;
plot(data(:,1),current_data, 'LineWidth',1);
%current_data_mflt = medfilt1(current_data,Nf);
current_data_mflt = hampel(current_data,Nf);
hold on;
plot(data(:,1),current_data_mflt, 'LineWidth',1);
current_data_sgflt = sgolayfilt(current_data_mflt,1,201*Nf);
hold on;
plot(data(:,1),current_data_sgflt, 'LineWidth',3); % <--- FIXED
%fcoeff = ones(1, 201*Nf)/(201*Nf);
%current_data_mavgflt = filter(fcoeff, 1, current_data_mflt);
%hold on;
%plot(data(:,1)-(100*Nf)/fs,current_data_mavgflt, 'LineWidth',1);
legend('RAW','MEDF','SGF'); %'MAVR');
xlabel('czas t (s)');
ylabel('pr¹d twornika i_a (A)');
grid on;
    %voltage
    case 3
voltage_data = data(:,voltage_channel+1).*100;
plot(data(:,1),voltage_data, 'LineWidth',1);
%current_data_mflt = medfilt1(current_data,Nf);
voltage_data_mflt = hampel(voltage_data,Nf);
hold on;
plot(data(:,1),voltage_data_mflt, 'LineWidth',1);
voltage_data_sgflt = sgolayfilt(voltage_data_mflt,1,201*Nf);
hold on;
plot(data(:,1),voltage_data_sgflt, 'LineWidth',3);
hold on;
plot(data(:,1),560*sin((data(:,1)-0.0034).*2*pi()*50));
%fcoeff = ones(1, 201*Nf)/(201*Nf);
%current_data_mavgflt = filter(fcoeff, 1, current_data_mflt);
%hold on;
%plot(data(:,1)-(100*Nf)/fs,current_data_mavgflt, 'LineWidth',1);
legend('RAW','MEDF','SGF'); %'MAVR');
xlabel('czas t (s)');
ylabel('napiêcie twornika U_a (V)');
grid on;
end       
        
        
SetFigureDimensionsAndPosition(f,500,250);

 