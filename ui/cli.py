from swapi.core.report import Report
from swapi.core.services import Services
from tabulate import tabulate as tb

import msvcrt
import os


class CLI:
    def __init__(self, service: Services):
        self.__service = service
    
    def menu(self):
        while (True):
            self.__clear_console()
            categories: Report = self.__service.categories
            if not categories.ok:
                print(categories.sys_message)
                break

            category = self.__select_category(categories.data)  # pyright: ignore[reportArgumentType]
            self.__clear_console()
            data: Report = self.__service.data_by_category(category)
            if not data.ok:
                print(data.sys_message)
                break

            print(f"Total entries: {len(data.data)}")
            print("Save data? (y - yes, n - no)")
            if self.__confirmation_dialog():
                self.__service.write_categry(category)

    def __select_category(self, categories: list[str]) -> str:
        print("Existing categories (Press the index):")
        count_categories = len(categories)
        for i in range(count_categories):
            print(f"{i + 1}. {categories[i].capitalize()}")

        while (True):
            try:
                input = int(self.__getch_key())
                index = input - 1
                if index >= 0 and index < count_categories:
                    return categories[index]
            except ValueError:
                pass      

    def __confirmation_dialog(self) -> bool:
        while (True):
            key = self.__getch_key()
            match key:
                case "y":
                    return True
                case "n":
                    return False

    def __to_table(self, data: dict):
        if len(data) == 0:
            return ""
    
        return tb(data, headers="keys", tablefmt="pipe")

    def __getch_key(self) -> str:
        return msvcrt.getch().decode()    
    
    def __clear_console(self):
        os.system("cls" if os.name == "nt" else "clear")