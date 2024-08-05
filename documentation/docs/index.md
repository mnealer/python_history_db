# Welcome to Python History Database

This project allows you to store data indexed by date into a database, where data is stored in multiple files.
The idea is that analysis of larger data items can be split into multiple processes, where each examines a single
file and then the combined data is returned to the user.

It should be noted that PyHD is designed to be an OLAP type database. It has no ACID protection layer and as such
is not transaction safe. It is built to take in new records in batches, assuming that most actions will be reads, 
performing analysis on the said data.

In this way, its is something like a NoSQL Data Warehouse. The application is not built to work over multiple 
instances though, so cannot be seen as a replacement for a warehouse dealing with terabytes or petabytes of data.

The focus of the system is to create an Analysis warehouse for applications where the core application has to deal
with the OTLP type actions, and running report analysis on the central database causes performance issues.

It also allows for historical data to be stored in smaller data warehouses, but without the need to design
and maintain a full data warehouse.


