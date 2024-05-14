from pymongo import MongoClient


client = MongoClient()

db = client.catalogue  # catalogue = database name

documents = [
    {
        "title": "Lord of the Rings",
    },
    {
        "title": "The Great Gatsby",
    },
    {
        "title": "The Hobbit",
    },
    {
        "title": "Harry Potter",
    },
]

db.books.insert_many(documents)  # add "books" collection to the database with "documents" data

client.close()
