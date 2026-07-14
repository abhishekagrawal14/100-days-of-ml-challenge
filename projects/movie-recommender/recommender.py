import os
import pickle 
import gdown

from config import MOVIE_LIST_PATH, SIMILARITY_PATH, SIMILARITY_GDRIVE_URL
from utils import fetch_posters

if not os.path.exists(SIMILARITY_PATH):
     gdown.download(SIMILARITY_GDRIVE_URL, SIMILARITY_PATH, quiet=False)

movies = pickle.load(open(MOVIE_LIST_PATH , 'rb'))
similarity = pickle.load(open(SIMILARITY_PATH , 'rb'))

def recommend(movie):
    print("FUNCTION CALLED WITH:", movie) 
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)) , reverse=True ,key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_posters(movie_id))

    return recommended_movies, recommended_posters
