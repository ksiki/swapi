from swapi.data.categories.category_writer import CategoryWriter
import swapi.utils.formatted as formatted


class FilmsWriter(CategoryWriter):
    __CATEGORY = "films"

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

        for film in data:
            film["characters"] = formatted.id_from_urls(film.get("characters"))  # pyright: ignore[reportArgumentType]
            film["planets"] = formatted.id_from_urls(film.get("planets"))  # pyright: ignore[reportArgumentType]
            film["starships"] = formatted.id_from_urls(film.get("starships"))  # pyright: ignore[reportArgumentType]
            film["vehicles"] = formatted.id_from_urls(film.get("vehicles"))  # pyright: ignore[reportArgumentType]
            film["species"] = formatted.id_from_urls(film.get("species"))  # pyright: ignore[reportArgumentType]

        return data
