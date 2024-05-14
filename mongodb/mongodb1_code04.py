from pymongo import MongoClient


client = MongoClient()

db = client.catalogue  # catalogue = database name

print(db.books.find_one())  # find_one() method returns the first document in the collection

for book in db.books.find({"title": {"$regex": "t"}}):  # search for documents with title containing "t"
    print(book["title"])  # print the title of the book

client.close()
