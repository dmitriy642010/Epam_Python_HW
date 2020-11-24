import urllib.request
from urllib.error import HTTPError, URLError


def count_dots_on_i(url: str) -> int:
    try:
        site = urllib.request.urlopen(url)
        data = site.read().decode()
        return sum(1 for symb in data if symb == "i")
    except (HTTPError, URLError):
        raise ValueError("Unreachable {url}")
