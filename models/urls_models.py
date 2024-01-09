from pydantic import BaseModel, HttpUrl


class UrlShortener(BaseModel):
    original_url: str
    shortened_url: str
