import requests
from typing import List, Dict

from app.config import TMDB_API_KEY

TMDB_BASE_URL = "https://api.themoviedb.org/3"


def search_movie(query: str, limit: int = 5) -> List[Dict]:
    url = f"{TMDB_BASE_URL}/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "ru-RU",
        "include_adult": False,
        "page": 1,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data.get("results", [])[:limit]

def movies_by_rating(min_rating: float, limit: int = 5):
    url = f"{TMDB_BASE_URL}/discover/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "language": "ru-RU",
        "sort_by": "vote_average.desc",
        "vote_average.gte": min_rating,
        "vote_count.gte": 100,  # чтобы отсечь мусор
        "page": 1,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data.get("results", [])[:limit]
