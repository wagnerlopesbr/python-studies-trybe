from models.film_model import FilmModel


class FilmController:
    def search_movies_by_title(self, title=None):
        query = {"title": title} if title else None
        movies = FilmModel.search_movies_by_title(query)
        return [movie.to_dict() for movie in movies]
    
    def search_movie_by_id(self, _id):
        movie = FilmModel.search_movie_by_id(_id)
        return movie.to_dict() if movie else None
