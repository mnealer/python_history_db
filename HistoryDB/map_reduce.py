from typing import List, Dict, Any
from aggregates import Aggregate


class Reduce:
    def __init__(self, fields: List[str]):
        self.fields: List[str] = fields
        self.group_by: Dict[str, Dict[str, Any]] = {}
        self.default_dict = None

    def add(self, record: Dict[str, Any]) -> None:
        if not self.default_dict:
            self._create_default_dict(record)
        key = self._create_key(record)
        if key not in self.group_by:
            self.group_by[key] = self.default_dict.copy()
        for k, v in record.items():
            if k in self.fields:
                self.group_by[key] = v
            else:
                self.group_by[key][k].append(v)

    def _create_key(self, record: Dict[str, Any]) -> str:
        key = " ".join([str(record[k]) for k in self.fields])
        return key

    def _create_default_dict(self, record: Dict[str, Any]) -> None:
        self.default_dict = {}
        for k, v in record.items():
            if k not in self.default_dict:
                if k in self.fields:
                    self.default_dict[k] = v
                else:
                    self.default_dict[k] = []

    def results(self) -> List[Dict[str, Any]]:
        return [v for v in self.group_by.values()]


class ReduceFields:

    def __init__(self, fields: List[str] , aggregates: list[Aggregate]) -> None:
        self.fields: list = fields + [ag.field for ag in aggregates]
        self.results: list = []

    def add(self, record: dict):
        new_record = {k: v for k, v in record.items() if k in self.fields}
        self.results.append(new_record)



