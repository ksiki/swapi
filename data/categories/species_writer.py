from swapi.data.categories.category_writer import CategoryWriter
import swapi.utils.extractor as extractor


class SpeciesWriter(CategoryWriter):
    __CATEGORY = "species"

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

        for specie in data:
            specie["homeworld"] = extractor.id_from_url(specie.get("homeworld"))  # pyright: ignore[reportArgumentType]
            specie["people"] = extractor.id_from_urls(specie.get("people"))  # pyright: ignore[reportArgumentType]
            specie["films"] = extractor.id_from_urls(specie.get("films"))  # pyright: ignore[reportArgumentType]

        return data