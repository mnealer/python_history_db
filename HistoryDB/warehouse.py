from query import Query


class CreateWarehouse:
    def __init__(self, db_path: str, db_file_directory: str, db_file_count: str) -> None:
        pass


class Warehouse:
    def __init__(self, db_path: str) -> None:
        pass

    def report(self, query: Query) -> list:
        pass

    def report_to_file(self, query: Query, report_file: str) -> bool:
        pass