def id_from_url(url: str) -> str:
    if url is None or len(url) <= 0:
        return ""
    
    split: list[str] = url.split("/")  
    return split[len(split) - 1]


def id_from_urls(urls: list) -> list:
    id: list[str] = []

    for url in urls:
        id.append(id_from_url(url))

    return id