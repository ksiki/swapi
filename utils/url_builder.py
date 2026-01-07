from urllib.parse import urljoin
import re


class URLBuilder:
    def __init__(self, url: str):
        self.__base_url: str = url
        if not url.endswith("/"):
            self.__base_url += "/" 

    def build_category_url(self, category: str) -> str:
        if not self.__is_valid_url(category):
            category = self.__formatted_url(category)

        return urljoin(self.__base_url, category)

    def __formatted_url(self, url: str) -> str:
        """
        Deleting all "/" at the beginning and end of the line, because:

        urljoin("https://swapi.info/api/", "/people") = "https://swapi.info/people"  (disappears /api)
        """
        if url.startswith("/"):
            url = re.sub(r"^/+", "", url)
        if url.endswith("/"):
            url = re.sub(r"/+$", "", url)

        return url

    def __is_valid_url(self, url: str) -> bool:
        if url.startswith("/"):
            return False
        if url.endswith("/"):
            return False

        return True


u = URLBuilder("https://swapi.info/api")
print(u.build_category_url("/people/"))
