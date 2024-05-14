from pymongo import MongoClient


with MongoClient() as client:  # use "with" statement to automatically close the connection
    db = client.catalogue  # catalogue = database name
    for book in db.books.find({"title": {"$regex": "t"}}):
        print(book["title"])
