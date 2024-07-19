# overarching concept.

With a file based database, the issue is basically all on the size of the file and the db 
object in whatever form is in the file. The size directly effects speed and the amount of memory 
used.

## Using multiple files.

The original concept here is to create the database over lots of different files, each file 
can then be accessed via an async coroutine. This means a database spread over 100 files 
can be read quite easily and fast. There does have to be a balance between the size of the file
and the number of files. If the files are too small, the system wastes too much time opening
files and on IO functionality. if the files are too large, then we cam have issues with memory
consumption. We want to have a balance between the number of concurrent processes that are
happening against memory consumption. 

There is also the issue with the format used in storing records. I noticed that with tinydb,
a database with more records, but smaller ones, was faster than a larger, but less records.
The issue with this is the indexing of the records. TinyDB stored the database as a dictioary,
so just like a database, it can locate records faster using indexes, than it can with other
fields. 

TinyDB had only two levels to its data. table and document id. Since we are looking at very large
data collections for which we are reading from and ones we don't need to locate via
document Id for updates etc. I'm wondering if its possible to have multiple layers in
a dictionary and find results via path searches.

We will have a primary search field of a timestamp, which is really not going to be
indexable, so a routine to search and filter via time stamps will be required