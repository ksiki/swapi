import requests


class Connector:
    def __init__(self, url: str):
        self.__url: str = url
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
    def data(self) -> list[dict]:
        data = self.__responce.json()
        if isinstance(data, dict):
            data = [data]

        return data

    def reconnect(self):
        self.__connect()

    def __connect(self):
        self.__responce = requests.get(self.url)