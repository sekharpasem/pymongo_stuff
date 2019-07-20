from pymongo import MongoClient

# instantiate Mongo Client
client = MongoClient('mongodb://localhost:27017')

# get pymongo test database
db = client['pymongo_test']

# gets the inventory collection from pymongo_test
collection = db.inventory

# insert single record
document = { "item1": "ABC1", "sizes": ["S", "M", "L"]}
result = collection.insert_one(document)
print("Inserted record with _id : {}".format(result.inserted_id))


# inserts multiple records
inserts_list = [
    {"item2": "ABC2", "sizes": ["S", "L"]},
    {"item3": "ABC3", "sizes": ["S", "M", "L"]},
    {"item4": "ABC4", "sizes": ["S", "M", "L"]},
    {"item5": "ABC5", "sizes": ["S", "M"]},
]
result = collection.insert_many(inserts_list)
print("Inserted records with _id : {}".format(str(result.inserted_ids)))