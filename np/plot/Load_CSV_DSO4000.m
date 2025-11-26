%*************************************************************************
%*This function will load a Hantek DSO4048 encoded CSV File              *
%*************************************************************************
function data_out = Load_CSV_DSO4000(filename, channels_to_load)
%filename = 'test.csv';
channel_length = 4000;
%channels_to_load = 2;
header_size = 3;
data_out = zeros(channel_length,channels_to_load+1);

if isfile(filename)
   data = readmatrix(filename);
   
    data_out(:,1) =  data(1:channel_length,2);
   
    for channel_no=1:channels_to_load
        v_offset =  (channel_length+header_size)*(channel_no-1) + 1;
        start = v_offset;
        stop = v_offset+channel_length-1;
        data_out(:,1+channel_no) =  data(start:stop,3);
    end
else
        data_out = [];
end
end