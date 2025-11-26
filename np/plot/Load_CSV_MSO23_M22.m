%*************************************************************************
%*This function will load a Hantek DSO4048 encoded CSV File              *
%*************************************************************************
function data_out = Load_CSV_MSO23_M22(filename, channels_to_load)

header_size = 12;

if isfile(filename)
   data = readmatrix(filename);
   data_len = length(data)-header_size;
   data_out = zeros(data_len,channels_to_load+1);
   %time column:
   data_out(:,1) =  data(header_size+1:header_size+data_len,1);
    
   for channel_no=1:channels_to_load
        data_out(:,1+channel_no) =  data(header_size+1:header_size+data_len,2+(channel_no-1)*3);
   end
else
        data_out = [];
end
end