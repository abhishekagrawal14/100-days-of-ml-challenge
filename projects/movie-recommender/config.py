import os 
from dotenv import load_dotenv 

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Base directory — jaha config.py khud hai, uske hisaab se path banayenge
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# local paths of files 
MOVIE_LIST_PATH = os.path.join(BASE_DIR, "models", "movies.pkl")
SIMILARITY_PATH = os.path.join(BASE_DIR, "models", "similarity.pkl")

# google drive link of similarity_path as its large 

SIMILARITY_GDRIVE_URL = "https://drive.google.com/uc?id=17V0O1wAl2yDsQQZ6nL7oI99yYaFNiFiZ"

# TMDB API base URLs
TMDB_BASE_URL = "https://api.themoviedb.org/3/movie"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

