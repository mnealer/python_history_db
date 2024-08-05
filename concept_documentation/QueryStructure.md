# Query Structure

Looking at the way queries are run on data warehouses, the follow a simple patten. 

* fields you want to group by
* filters
* aggregates

I am going to assume that because this is a history database, a date range will be required for any report.

That means a Query for the database will need

* daterange
* fields
* filters
* annotate 
* aggregate

Aggregates will be a list, so would fields.

Using Eval with mako to create filter. Take in a text line, Run through Mako and then eval against the database
records

```python
from filters import FilterEval

filter = FilterEval("${field1} > 45 and ${field1} < 90")
```

This would work based on the Idea of using Mako as a template language to alter the filter template to 
text and then eval. The fields would have to exist in the database and each record. if not there, then they 
should return false. The filter would only be applied to a given record and the coroutine isolated, so any
nasty eval won't work.


so the order of work is 

* get a list of all the relevant fields required
* find records by date range index.
* check the record with the filter and collection is passed
* calculate any annotations and add to the record
* remove any fields that are not stated in fields, and aggrigates
* reduce the records 
* calculate  aggregates function 1
* pass back to core
* redunce records
* calculate aggregate function 2

## Stage 1. getting a list if all fields

from the query, we have fieldnames stated in field, agreegates and the ones created in annotations. If the
query has a list of the fields, thats easy to get. annotations need to state the final field they will create, along
with a text string that will be evaluated to create the new value. 

Aggregates need to state a single field they are aggregating. The basee model for annotations and agregates need to
include a property or method to obtain the field name. Data will be returned as dictionaries, so order of the  
fields will not be relevant. Actually if the annotated field is not in an aggregate, then its not going to be
in the final data, so we just need fields from fields and aggregates.

## Stage 2 date filters
We need to change the dates into ranges that we can pull from the database. Year - month - day
check each date in the data using
value = dict1.get("year", {}).get("month", {}).get("day",[])

then merge the results

# stage 3 filtering

the string should have been put through the template. Each record will be passed to the filter object where it 
will be run against the eval and return a record or not. Failure results in not

## stage 4 annotations

pass the record to the annotation class and save the results, In the class it changes the text to match the
right fields and then does an eval where the fields are matched to the record passed. Result to be placed in the
annotation field. i.e add a key

## stage 5.1 Reduce
 delete fields in each record that are not needed.

## stage 5.2 reduce

* create keys based on the fields passed
* for each key create a dictionary with the other fields in it where the value of the other fields is []
* go through each record, match to the key and add the values to the relevant fields

Working this out. 

If we have a group_by class that creates a group_by dictionary, and is
given the fields.

1 create a class for the group by where the fields are passed, and an example
record is also passed
The class creates an example dictionary with the fields staying as they 
are and the rest set to []

Each record checks to see if their key exists and creats one if not.
it then adds the values to the lists

The class will need to know, which are the group by fields and
which are the reduce fields. The dictrionaies are then pulled out and returned





