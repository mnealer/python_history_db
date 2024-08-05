# Writing records out to files

Writing to the database means that each record Must contain certain fields and meet selected requirements.

I need to work out what those are before we can write the write modules.

SO we need a date field that one is obvious and it needs to be formated into [yyyy][mm][dd]

Do we want to force a model name or record type on the records? No, the user will need to define this one for 
themselves. If we have a base system with a pydantic class to define the record, they can update that before
its passed to the save record format. I think stay away from any other formatting. Its down to the users to define
the records they want to save, as it will alter the performance they need.


So we need a record 

yyyy,mm,dd,{record}

