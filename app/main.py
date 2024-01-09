from http.client import HTTPException
from typing import List
from fastapi import FastAPI
from starlette import status
from models.urls_models import UrlShortener
from services.urls_services import create_shortened_url, store_url_shortener, retrieve_url_from_random_str, get_all_urls
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Homepage"}
@app.post("/urls/")
def create_url(url: str) -> UrlShortener:
    url_to_shorten = create_shortened_url(url=url)
    return store_url_shortener(url_to_shorten)




@app.get("/urls/")
def get_urls() -> List[UrlShortener]:
    return get_all_urls()
@app.get("/urls/{url_shortened}")
async def redirect_to_original(url_shortened: str):
    original_url = retrieve_url_from_random_str(url_shortened)
    if original_url:
        return RedirectResponse(url=original_url, status_code=status.HTTP_302_FOUND)
    else:
        raise HTTPException

