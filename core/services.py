from swapi.core.report import Report
from swapi.data.data_storage import DataStore
from swapi.data.excel_worker import ExcelWorker


class Services:
    def __init__(self, excel_worker: ExcelWorker, data_store: DataStore):
        self.__excel_worker: ExcelWorker = excel_worker
        self.__data_store: DataStore = data_store

    @property
    def categories(self) -> Report:
        try:
            categories: list[str] = self.__data_store.existing_categories()
            return Report(True, "Ok", categories)
        except ConnectionError:
            return Report(False, "Couldn't get categories")

    def data_by_category(self, category: str) -> Report:
        try:
            data: list[dict] = self.__data_store.category(category)
            return Report(True, "Ok", data)
        except ConnectionError:
            return Report(False, "Couldn't get category data")
    
    def data_by_id(self, category: str, id: str) -> Report:
        try:
            data: list[dict] = self.__data_store.item_for_id(category, id)
            return Report(True, "Ok", data)
        except ConnectionError:
            return Report(False, "Couldn't get data by id")
        
    def write_categry(self, category: str) -> Report:
        rep: Report = self.data_by_category(category)
        return self.__write(rep, category)

    def write_by_id(self, category: str, id: str) -> Report:
        rep: Report = self.data_by_id(category, id)
        return self.__write(rep, category)
    
    def __write(self, rep: Report, category: str) -> Report:
        if not rep.ok:
            return Report(False, "There is no internet connection or a non-existent id/category has been entered")       
        self.__excel_worker.write(rep.data, category)  # pyright: ignore[reportArgumentType]
        return Report(True, "Ok")
