# tworzenia połączenia z serwerem filmowym, pobieranie najpopularniejszych filmów

import requests
API_TOKEN = "Appi key"


def get_headers():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    return headers


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_type):
    categories = ["popular", "now_playing", "upcoming", "top_rated"]
    if list_type not in categories:
        list_type = 'popular'
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()
# pobieranie obrazka


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
    print(data)
    return data["results"][:how_many]


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    return response.json()


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = get_headers()
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()
