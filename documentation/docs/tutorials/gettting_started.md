# Getting Started

## installation

PyHD can be installed via pip

```shell
pip install python-historical-database
```

## Creating your first warehouse

To create your first PyHD warehouse, You need to decide the name and location of the central warehouse file, plus
how many data files you want to spread the data over.

```python
from pyhd import create_wharehouse

create_wharehouse(warehouse="/path/to/warehouse/mywarehouse.json", data_files=10)
```

## Connecting to your warehouse

```python
from pyhd import warehouse

my_warehouse = warehouse("/path/to/my/warehouse/json")
```


## Running your first query

```python
from pyhw import Warehouse, Query, DateRange, Annotate
from pyhw import Count
from datetime import datetime


my_warehouse = Warehouse("/path/to/my/warehouse/mywarehouse/json")
query_dates = DateRange(datetime("2021", "05", "01"), datetime("2022", "05", "01"))
my_query = Query(daterange=query_dates, filter=["${type}='classchange' and ${class}== '2bc'"],
                 fields=["teacher", "class"], aggregates=[Count("pupil", "Pupil Count")])

my_report = my_warehouse.query(my_query)

```
This will return a data similar to this

| Teacher  | Class  | Pupil Count |
| -------- | ------ | ----------- |
| Mr. Doe  | 1A     | 25          |
| Ms. Smith| 2B     | 30          |
| Mr. Grey | 3C     | 28          |
| Ms. Jones| 4D     | 27          |
| Mr. Black| 5E     | 31          |

!!! note ""
    If any of the filter fields, annotation fields or selected fields don't exist in the record, they
    will not be included in the results.

## Queries

Queries are made up of four components, all of which MUST exist.

* DateRange Object. This is the start and end dates used for analysis
* filter:  Text object that will be rendered and evaluated against each record. Fields should be placed in ${}
* fields: A list of fields that are used to group the records.
* Aggregates: A list of PyHD annotation objects that are used to create the Aggregates.

## Annotations

You can create calculated fields by passing one or more functions using the ```annotations``` parameter. See
Annotations for details on how to create them. Note that if the created field is not included in the *fields*
or *aggregates* list, then they will have not effect. If the Annotation functions fails it will result in the
said record not being included.


## Writing to the database

!!! warning 
    Reading and writing to the database can occur at the same time, but you cannot multiple write actions to the database
    at the same time. There is no ACID protection. Multiple write actions are likely to result in lost data

Records are written to the warehouse using the WarehouseWrite() class. Records are added to a log in the class using 
write(), or write_many() and then saved using the save() method.

All records are saved in the warehouse by date. You can pass your own date by adding a record_date field as a datetime
object, or if not supplied the current date is used. "record_date" is not saved in the actual record, only used to 
create the index for saving the record, thus you cannot filter on "record_date".

When the save() method is run, the prepared rceords are added to a queue and passed to the co-routines for saving to 
one of the files. There is no control over which file the records are saved in.

```python
from pyhw.writer import WarehouseWriter
from pathlib import Path
from datetime import datetime


wr = WarehouseWriter(Path("/path/to/my/warehouse/mywarehouse.json"))

record ={"type": "registration", "name": "bob", "record_date": datetime.now().date()}

wr.write(record)
wr.save()

records = [{"type": "registration", "name": "bob", "record_date": datetime.now().date()},
           {"type": "registration", "name": "bob", "record_date": datetime.now().date()}]

wr.write_many(records)
wr.save()

```

