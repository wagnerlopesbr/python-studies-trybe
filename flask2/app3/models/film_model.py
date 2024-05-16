from .db import db
from bson.objectid import ObjectId


class FilmModel:
    _collection = db["movies"]

    def __init__(self, data):
        self.data = data
    
    @classmethod
    def search_movies_by_title(cls, query={}):
        data = cls._collection.find(query)
        return [cls(movie) for movie in data]
    
    @classmethod
    def search_movie_by_id(cls, _id):
        data = cls._collection.find_one({"_id": ObjectId(_id)})
        return cls(data) if data else None
    
    def to_dict(self):
        movie = {
            "title": self.data["title"],
            "year": self.data["year"],
            "director": self.data["director"],
            "genre": self.data["genre"],
            "poster": self.data["poster"],
            "_id": str(self.data["_id"])
        }
        return movie
