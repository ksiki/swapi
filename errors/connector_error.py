class ConnectorError(RuntimeError):
    @staticmethod
    def raise_error(url: str):
        raise ConnectorError(f"Request failed for {url}")