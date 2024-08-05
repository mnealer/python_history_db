from pydantic import BaseModel, model_validator, ValidationError
from datetime import datetime
from pathlib import Path


class HistoryRecord(BaseModel):
    year: str
    month: str
    day: str
    record: dict

    @model_validator(mode="before")
    @classmethod
    def date_index(cls, data: any):
        if not "record_date" in data:
            record_date = datetime.now()
        elif isinstance(data["record_date"], datetime):
            record_date = data["record_date"]
        else:
            raise ValidationError("Record Date passed but is not a valid datetime object")
        data["year"] = str(record_date.year)
        data["month"] = str(record_date.month)
        data["day"] = str(record_date.day)
        return data


class WarehouseWrite:

    def __init__(self, db_path: Path) -> None:
        if not isinstance(db_path, Path):
            raise TypeError("db_path must be a Path object")
        if not db_path.exists():
            raise FileNotFoundError("db_path file does not exist")
        self.db_path = db_path
        self.write_log = list()

    def write(self, record:dict) -> None:
        self.write_log.append(HistoryRecord(**record.dict()))
        return

    def write_many(self, records:list) -> None:
        [self.write_log.append(HistoryRecord(**r)) for r in records]
        return

    def save(self):
        # write records to the write log
        pass
