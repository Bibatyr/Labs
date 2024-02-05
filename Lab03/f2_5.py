def calculate_average_score_by_category(movie_list, category):
    category_movies = [movie["imdb"] for movie in movie_list if movie ["category"] == category]

    if not category_movies:
        return 0.0
    
    average_score = sum(category_movies) / len(category_movies)
    return average_score

