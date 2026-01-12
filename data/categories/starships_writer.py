from swapi.data.categories.category_writer import CategoryWriter
import swapi.utils.extractor as extractor


class StarshipsWriter(CategoryWriter):
    __CATEGORY = "starships"

    def __init__(self, path: str):
        super().__init__(path)

    @property
    def category_name(self) -> str:
        return self.__CATEGORY

    def write(self, data: list[dict]):
        data = self.format_data(data)
        super()._write_to_excel(data, self.__CATEGORY)

    def format_data(self, data: list[dict]) -> list[dict]:
        if not self._data_is_not_empty(data):
            return data

        for starship in data:
            starship["pilots"] = extractor.id_from_urls(starship.get("pilots"))  # pyright: ignore[reportArgumentType]
            starship["films"] = extractor.id_from_urls(starship.get("films"))  # pyright: ignore[reportArgumentType]

        return data