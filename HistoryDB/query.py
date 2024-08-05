from pydantic import BaseModel, model_validator, ValidationError, BeforeValidator
from datetime import datetime
from mako.template import Template
from exceptions import *
from aggregates import Aggregate
from annotations import Annotation
from typing import Annotated, List, Union



class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def date_range(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date is before start date")
        else:
            return self


class Filter:

    def __init__(self, filter):
        self.filter = filter
        self.filter_log = []
        try:
            self.template = Template(filter)
        except CompileException as e:
            raise FilterCompileException(e.__str__())
        except SyntaxException as e:
            raise FilterSyntaxException(e.__str__())
        except Exception as e:
            raise FilterOtherException(e.__str__())

    def filter_row(self, row, filename, counter):
        try:
            cmd = self.template.render(row)
        except Exception:
            self.filter_log.append(f"Render failed {filename}, {counter}")
            return False
        try:
            result = eval(cmd)
        except Exception:
            self.filter_log.append(f"evaluation failed: filename:{filename}, counter{counter}")
            return False
        if isinstance(result, bool):
            return result
        else:
            self.filter_log.append(f"evaluation failed to return a boolean: filename {filename}, counter{counter}")
            return False


def create_filter(value):
    if not isinstance(value, str):
        raise ValidationError("Filter must be a string")
    try:
        result = Filter(value)
    except:
        ValidationError("Failed to create Filter Object")
    return result


class QueryModel(BaseModel):
    date_range: DateRange
    filter : Annotated[Filter, BeforeValidator(create_filter)]
    fields: List[str]
    aggregates: List[Aggregate]
    annotations: Union[List[Annotation], None]




class Query:
    def __init__(self, daterange: DateRange, fields: list, filter: str, aggregates: list, annotation = None):
        self.query_model = QueryModel(date_range=daterange,
                                      fields=fields,
                                      filter=filter,
                                      aggregates=aggregates,
                                      annotation=annotation)
