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
* aggregates

Aggregates will be a list, so would fields.

Using Eval with mako to create filter. Take in a text line, Run through Mako and then eval against the database
records

```python
from filters import FilterEval

filter = FilterEval("${field1} > 45 and ${field1} < 90")
```

This would work based on the Idea of using Mako as a template language to alter the filter template to 
text and then eval

