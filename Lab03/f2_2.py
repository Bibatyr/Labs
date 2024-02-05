def get_high_score_movies(movie_list):
    return[movie for movie in movie_list if movie["imdb"] > 5.5]