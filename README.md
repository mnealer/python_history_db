# Python History DB

the idea of this project is to create something like a hadoop file structure holding json
data stored in msgpack. This allows smaller apps to have a fast OLAP type database to
run analysis on outside of the primary RDB.

Warehouses are unnormalized, but I intend this system to hold data as documents indexed
by date, and of course spread over multiple files. 

There will be NO ACID layer or protection on this system, but write tools will be made 
available, It will be up to the user to ensure that multiple write don't occur at the same
time and that writes are successful.

## Basic Idea

I want a system that can deal with large amounts of records and query them using async Co-routines. I also
want to have a Query structure that is not SQL based, and aimed at only running Data warehouse type queries. The
system will use a MapReduce type format to find records, filter, remove duplicate, reduce and then finally merge to
calculate aggregates. 

Taking an idea from TinyDB, data will be stored in a JSON type format, but using msgpack instead of the python 
json library. Data will also be index by dat, but each file will have its own index, so two records with the same date
can be in two different files.

Data from the co-routines will also be streamed back to the main process via queues, thus the main process can work
towards removing duplicates that occur from multiple processes and map results ready to create aggregates.

There will also be the ability to create your own aggregate classes, thus create custom calculations on values.


In the end, the user will be able to control the speed and system impact of a query by setting the amount of files the
data will be spread over, and the amount of concurrent processes.

When all this is done, we should end up with something like a data warehouse, but will far less development
and set-up time needed, thus allowing the system to be used for smaller applications.

# Setting Up

Right now most of this is conceptual and still working through idea and what needs to be there. 

# Contributing
Ideas would be great at this point. I have lots of conceptual ideas and some code, but the whole concept is 
not quite there yet, so it's hard to move forward with the coding



