import requests


class Connector:
    def __init__(self, url: str):
        self.__url = url
        self.__connect()

    @property
    def url(self) -> str:
        return self.__url

    @property
    def is_successfully(self) -> bool:
        try:
            self.__responce.raise_for_status()
            return True
        except requests.exceptions.RequestException:
            return False

    @property
    def data(self) -> dict:
        return self.__responce.json()

    def reconnect(self):
        self.__connect()

    def __connect(self):
        self.__responce = requests.get(self.__url)