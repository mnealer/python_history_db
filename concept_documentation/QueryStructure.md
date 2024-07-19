# Query Structure

All data will be historical and stored in the database in a date index, spread
over multiple files, thus records for a single date can be pulled from multiple 
locations. at the same time.

As such the first argument on a query will be a date or datetime range. This is used
to find the exact records from the db files

The next argument is going to be the filter arguments that need to be applied to these 
records. This cuts down the records before the move to the reduce phase.

Next will be the fields we will be grouping the data by. The fields from each record
we maintain in the records and are used for reducing the records down and pulling values 
together.

The last will be a set of aggregate functions that will be used to create the aggregates.


