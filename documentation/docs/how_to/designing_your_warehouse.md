# Designing your Warehouse

PyHW requires less time spent on design than a full data warehouse, but it does require some thought put into 
design and managing.

A the core of PyHW, data is stored in message Pack binary blobs that need to be read in as a dictionary and then
processed. Spreading records over multiple files allows PyHW to process data using async processsing, but there
are certain elements you must consider. With fewer, larger files, each proccess will take up more memory and take a 
little longer to extract and read the file data. Thus having too few and too large files will cause slow processing and
memory usage.

If you have a lot of smaller files, then you will also have performance issues, as each process still needs to access 
files and extract the data. too many files results in a lot of wasted time on IO. You also need to consider the amount 
on Async processors you allow to run at the same time. too many processes will cause large memory usage, while too small
will slow down the read.

Basically, for optimized performance, you need to consider file sizes, number of files and the number of processes
running at the same time. 

its also worth considering that this system is not slowed down by ACID protections. Read actions are much faster than
with an rdb. With an RDB, processing very large amounts of files has a decreased level of performance. With PyHW, 
processing is spread over a number of co-routines, where data is filtered and compressed for each file before the
final calculations are done. This multistage processing allows for accessing much larger numbers of records without
causing your server to have a meltdown.

