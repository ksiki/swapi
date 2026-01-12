from swapi.core.services import Services
from swapi.data.data_storage import DataStore
from swapi.data.excel_worker import ExcelWorker
from swapi.ui.cli import CLI

import swapi.config as config
import os

if __name__ == "__main__":
    path = input("Specify the path to the file (name) to save the data: ")
    excel_worker: ExcelWorker = ExcelWorker(path)
    os.system("cls" if os.name == "nt" else "clear")

    data_storage: DataStore = DataStore(config.API)
    service: Services = Services(excel_worker, data_storage) 
    ui: CLI = CLI(service)
    ui.menu()