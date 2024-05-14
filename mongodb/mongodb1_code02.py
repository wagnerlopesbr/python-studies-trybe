from pymongo import MongoClient


client = MongoClient()

db = client.catalogue  # catalogue = database name
students = db.books  # books = collection name

book = {
    "title": "Lord of the Rings",
}
document_id = db.books.insert_one(book).inserted_id
print(document_id)

client.close()
