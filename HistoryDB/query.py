from pydantic import BaseModel, model_validator, ValidationError
from datetime import datetime


class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def date_range(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date is before start date")
        else:
            return self


class Query:
    def __init__(self, daterange: DateRange, fields: list, data_filters: list, aggregates: list):
        self.daterange = daterange
        self.fields = fields
        self.data_filters = data_filters
        self.aggregates = aggregates

