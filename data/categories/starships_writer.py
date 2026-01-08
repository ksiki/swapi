from swapi.data.categories.category_writer import CategoryWriter
import swapi.utils.formatted as formatted


class StarshipsWriter(CategoryWriter):
    __CATEGORY = "starships"

    def __init__(self, path: str):
        super().__init__(path)

    @property
    def category_name(self) -> str:
        return self.__CATEGORY

    def write(self, data: list[dict]):
        data = self.__format_data(data)
        super()._write_to_excel(data, self.__CATEGORY)

    def __format_data(self, data: list[dict]) -> list[dict]:
        if not self._data_is_not_empty(data):
            return data

        for starship in data:
            starship["pilots"] = formatted.id_from_urls(starship.get("pilots"))  # pyright: ignore[reportArgumentType]
            starship["films"] = formatted.id_from_urls(starship.get("films"))  # pyright: ignore[reportArgumentType]

        return data