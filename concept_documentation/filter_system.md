# Filters

filters are added to sql using Where functions and in tinyDB using a not to pleasant language spec that allows for
them to be parsed.

What if we had filters as classes and can place them as children of each other in a tree

so a filter would look like
```python
between(field, value, value)
equal(field, value)
```
Then we can have logic filters

```python
from filters import between, gt, equal, where, filter_or, filter_and
or([between(field, value, value), equal(field, value)])
fand([equal(field, value), equal(field, value)])
where(fand(or(between(field, value, value), between(field, value, value)),equal(field, value), gt(field, value)))
```

Each object is initialized and bunched in the overall filter, and there is a standard method called to pass the
record to the filter object