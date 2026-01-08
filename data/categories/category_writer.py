from abc import ABC, abstractmethod
import pandas as pd

class CategoryWriter(ABC):
    ENGINE = "openpyxl"

    def __init__(self, path: str):
        self.__path: str = path

    @property
    @abstractmethod
    def category_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def write(self, data: list[dict]):
        raise NotImplementedError

    @abstractmethod
    def __format_data(self, data: list[dict]) -> list[dict]:
        raise NotImplementedError

    def _write_to_excel(self, data: list[dict], category: str):
        df: pd.DataFrame = pd.DataFrame(data)
        with pd.ExcelWriter(self.__path, engine=self.ENGINE) as writer:
            df.to_excel(writer, sheet_name=category, index=False)

    def _data_is_not_empty(self, data: list[dict]) -> bool:
        count_peopls: int = len(data)
        if count_peopls <= 0:
            return False
        
        return True