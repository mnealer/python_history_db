# Why PyHW

setting up and maintaining database servers is often a little bit of a chore. This is espeically true when the 
amount of records start going into the millions. Data Warehouses get around this by spreading data over multiple 
instances and use multiple processes to filter and compress data in separate processes and threads before they are merged
into a single result. RDB's generally don't do this. they try to process everything together.

PyHW was imspired by the development of TinyDB and the concepts of a data warehouse. TinyDB is a python only database
that has no ACID protection and stores data in a file, using json. It works wonderfully for small amounts of data
that need to be available for lots of reads. it does have the ability to do writes update and deletes as well.
Warehouse drop the idea of being ACID databases, where the number of writes are expected to be high and simultaeous.
they store historical data assuming that writes will most be adding new records to the database, with a new deletes.
All the focus is on faster reads.

I took the idea of storing data in simple files, but swapped to msgpack, as this compresses data and its read/writes are
faster than standard json. I also worked on the idea the data would be spread over multiple files. The multiple files
allows for much larger record storages that TinyDB could handle. TinyDB also index data using a documentID in a similar
way to NoSQL document databases. looking at the way data was extracted from data warehouses, I realised that having a
documentid would not really be of any use. Instead I decided to index the data by date, using three levels. year, month,
and day. So we select a date and using the standard dictionary we can access the records using database[year][month][day].

Hadoop base data warehouses also use a Map Reduce sequence. So using this, data is stored in multiple places. A process
is started on for each data portion on the relevant instance, then Map Reduce shrinks and compresses the data. I interepeted
this as the following.

* extract records for my dates
* filter the records to only the ones I'm interested in
* remove any fields that are not needed for the report
* compress the fields down into lists where they are going to be used for aggregates, so we have fewer records
* pass this data to the centeral server.
* merge the datasets together
* compress the data down again
* do the final aggregate calcuation
* return the report.

When we see the data being processed like this we can see that we can access very large amounts of records, without 
swamping your server. Since we can control and queue the processes, we can control the processing power needed. With 
each process Maping and reducing the data, the results from each process are far smaller that the original data, thus 
allowing dealing with data in chunks without swamping the memory. 

Using such a system, I can create a warehouse spread over 1000's of files and be able to process and create a report far 
faster and with less resources than an RDB.

### Warehouses for smaller apps.

One of the other elements that have pushed this idea for me, is the cost and time needed for a data warehouse. Data
warehouses are not easy to design and maintain. This puts them outside the resources for most SME's, but PyHW takes
less upkeep and design time than data warehouses do.


## Querying a warehouse.

When I looked at how a warehouse is used, I started to see a pattern.  They use a subset of SQL, but maintain the
overall look and feel of SQL. This is ok, but I saw that all queries had the same components. If i presented users
with these as those components, then querying a warehouse becomes somewhat simpler to understand.

However PyHW is not a full data warehouse and there are differences. the most important one is that it assumes
an index of the date the record assigned to the record. Using this Queries become easy to quantify into components.

### DateRange

All queries will have a date range that will be used as the first filter on the data pulled by the proccesses. Since
the data is index by this, pulling this data is very fast.

### Filters

A text based filter to define which of the records passed should be included. With PyHW, I have designed the system
to use the Mako template language. This allows values for the records to be placed in the filter text and evaluated.

### Fields

Queries are based on a set of fields that the data is grouped, for example region and city. These are used to 
create a set of distinct records.

### Distinct

This one is optional and to be used if there will be unwanted duplicates in the data. It will be applied to remove
duplicates from the data, based on the fields passed to it. It will assume that all fields mentioned in the
Fields setting are included, plus one or more additional fields. This will then be applied to remove duplicates. This 
action will be applied directly after the filter action has taken place and before the reduce.

What do I do if the duplicates are found across multiple records. It kinda means the Distinct has to be done twice
to remove duplicates, so the reduce to create lists for aggregates cannot be done at the file level, but at the
central level

### Aggregates

these take values from other fields and perform calcuations or transformations, such as Count(), mean() etc.

### Annotations

Annotations are optional. they will create calculated fields right after the filter stage, so the new field 
created by the annotation can be used in fields and aggregates.


## Aggregate classes

Aggregates require two functions to be defined. The first is used to process the list of values in each process. The
seccond is used when the values are merged together to produce the final result.  For example. average() will require
one calucation to produce the result in the process and a different one to merge a group of averages.



ok, Aggregates cannot be calculated in the file procedures, but they can be converted into namedtuples, which reduces 
memory size. once there the central system can remove duplicates and then extract the data to the mapping stage
creating dictionaries and deleting the tuples as it goes

