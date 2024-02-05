def calculate_average_score(movie_list):
    if not movie_list:
        return 0.0
    
    total_score = sum(movie["imdb"] for movie in movie_list)
    average_score = total_score / len(movie_list)
    return average_score