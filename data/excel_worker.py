from swapi.data.categories.category_writer import CategoryWriter
from swapi.data.categories.films_writer import FilmsWriter
from swapi.data.categories.people_writer import PeopleWriter
from swapi.data.categories.planets_writer import PlanetsWriter
from swapi.data.categories.species_writer import SpeciesWriter
from swapi.data.categories.starships_writer import StarshipsWriter
from swapi.data.categories.unknown_category_writer import UnknownCategotryWriter
from swapi.data.categories.vehicles_writer import VehiclesWriter
from swapi.errors.unknown_category_error import UnknownCategoryError


class ExcelWorker:
    def __init__(self, path_to_file: str):
        self.__path_to_file: str = path_to_file
        self.__writters: list[CategoryWriter] = list()
        self.__unknown_category_writer = UnknownCategotryWriter(self.__path_to_file)

        self.__init_writters()

    def write(self, data: list[dict], category: str):
        try:
            writter: CategoryWriter = self.__find_writer(category)
            writter.write(data)
        except UnknownCategoryError:
            self.__unknown_category_writer.write(data)

    def __find_writer(self, category: str) -> CategoryWriter:
        for writter in self.__writters:
            if writter.category_name == category:
                return writter  
        raise UnknownCategoryError(f"Writer for category {category} not found")

    def __init_writters(self):
        self.__writters.append(FilmsWriter(self.__path_to_file))
        self.__writters.append(PeopleWriter(self.__path_to_file))
        self.__writters.append(PlanetsWriter(self.__path_to_file))
        self.__writters.append(SpeciesWriter(self.__path_to_file))
        self.__writters.append(StarshipsWriter(self.__path_to_file))
        self.__writters.append(VehiclesWriter(self.__path_to_file))
