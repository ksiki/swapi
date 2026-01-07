from swapi.data.connection.connector import Connector, ConnectorError
from swapi.utils.url_builder import URLBuilder


class DataStore:
    def __init__(self, api: str):
        self.__api: str = api
        self.__connector: Connector = Connector(api)
        self.__url_builder: URLBuilder = URLBuilder(api)

    def existing_categories(self) -> dict:
        self.update_connector(self.__api)

        if not self.__connector.is_successfully:
            raise ConnectorError.raise_error(self.__api)

        return self.__connector.data[0]

    def category(self, category: str) -> list[dict]:
        url: str = self.__url_builder.build_category_url(category)
        self.update_connector(url)

        if not self.__connector.is_successfully:
            raise ConnectorError.raise_error(url)
        
        return self.__connector.data
    
    def item_for_id(self, category: str, id: str) -> list[dict]:
        url: str = self.__url_builder.build_id_url(category, id)
        self.update_connector(url)

        if not self.__connector.is_successfully:
            raise ConnectorError.raise_error(url)

        return self.__connector.data

    def update_connector(self, url: str):
        if self.__connector.url == url:
            return

        self.__connector.change_url(url)
        if not self.__connector.is_successfully:
            self.__connector.reconnect()
