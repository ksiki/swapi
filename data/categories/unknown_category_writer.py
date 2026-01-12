from swapi.data.categories.category_writer import CategoryWriter


class UnknownCategotryWriter(CategoryWriter):
    __CATEGORY = "unknown"

    def __init__(self, path: str):
        super().__init__(path)

    @property
    def category_name(self) -> str:
        return self.__CATEGORY

    def write(self, data: list[dict]):
        super()._write_to_excel(self.format_data(data), self.__CATEGORY)

    def format_data(self, data: list[dict]) -> list[dict]:
        return data