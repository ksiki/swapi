from swapi.data.categories.category_writer import CategoryWriter
import swapi.utils.formatted as formatted


class PeoplesWriter(CategoryWriter):
    __CATEGORY = "people"

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

        for people in data:
            people["homeworld"] = formatted.id_from_url(people.get("homeworld"))  # pyright: ignore[reportArgumentType]
            people["films"] = formatted.id_from_urls(people.get("films"))  # pyright: ignore[reportArgumentType]
            people["species"] = formatted.id_from_urls(people.get("species"))  # pyright: ignore[reportArgumentType]
            people["vehicles"] = formatted.id_from_urls(people.get("vehicles"))  # pyright: ignore[reportArgumentType]
            people["starships"] = formatted.id_from_urls(people.get("starships"))  # pyright: ignore[reportArgumentType]

        return data
