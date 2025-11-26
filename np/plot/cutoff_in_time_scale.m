function subindex = cutoff_in_time_scale(time_vector, time_start, time_end)

vlen = length(time_vector); %load how long is the time vector
start_index = find(time_vector>=time_start);
if isempty(start_index) 
    start_index = 1;
    disp('Subindex value at defined start time is empty. Setting time range to default.');
else 
    start_index = start_index(1);
end
stop_index = find(time_vector(start_index:vlen)>=time_end);
if isempty(stop_index) 
    stop_index = vlen;
   disp('Subindex value at defined start-stop time is empty. Setting time range to default.');
else
    stop_index = stop_index(1)+start_index-1;
    if stop_index>vlen
        stop_index=vlen;
    end
end

subindex = start_index:stop_index;