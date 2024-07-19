# Python History DB

the idea of this project is to create something like a hadoop file structure holding json
data stored in msgpack. This allows smaller apps to have a fast OLAP type database to
run analysis on outside of the primary RDB.

Warehouses are unnormalized, but I intend this system to hold data as documents indexed
by date, and of course spread over multiple files. 

There will be NO ACID layer or protection on this system, but write tools will be made 
available, It will be up to the user to ensure that multiple write don't occur at the same
time and that writes are successful


