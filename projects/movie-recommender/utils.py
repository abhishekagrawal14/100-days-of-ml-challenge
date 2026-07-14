import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import TMDB_API_KEY, TMDB_BASE_URL, TMDB_IMAGE_BASE_URL

session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

def fetch_posters(movie_id):
    try:
        response = session.get(
            f"{TMDB_BASE_URL}/{movie_id}?api_key={TMDB_API_KEY}&language=en-US",
            timeout=10
        )
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return TMDB_IMAGE_BASE_URL + poster_path
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for {movie_id}: {e}")
    return "https://via.placeholder.com/500x750?text=No+Image"
    
