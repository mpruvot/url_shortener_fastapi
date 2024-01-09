import json
import string
import random

from models.urls_models import UrlShortener
from typing import List


def get_random_str(length: int = 5):
    """Returns a random string of 5 characters long"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def create_shortened_url(url: str):
    """Returns a shortened URL based on the original URL"""
    new_url = UrlShortener(original_url=url, shortened_url=get_random_str())
    return new_url


def store_url_shortener(url: UrlShortener) -> UrlShortener:
    """Stores the shortened URL in the database"""
    url_shortener_to_json = url.model_dump()
    try:
        with open("/Users/marius/Desktop/url_shortener_fastapi/urls.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(url_shortener_to_json)

    with open("/Users/marius/Desktop/url_shortener_fastapi/urls.json", "w") as file:
        json.dump(data, file, indent=4)

    return url


def get_all_urls() -> List[UrlShortener]:
    """Returns all shortened URLs in the json file"""
    with open("/Users/marius/Desktop/url_shortener_fastapi/urls.json", "r") as file:
        data = json.load(file)
        return [UrlShortener(**url_dict) for url_dict in data]


def retrieve_url_from_random_str(random_key: str) -> str:
    """Return the full URL from the Db"""
    data = get_all_urls()
    found_match = None
    for url in data:
        if url.shortened_url == random_key:
            found_match = url.original_url
    return found_match


test = retrieve_url_from_random_str("dmUKl")
print(test)