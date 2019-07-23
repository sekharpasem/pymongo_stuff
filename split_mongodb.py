from pymongo import MongoClient

# instantiate Mongo Client
client = MongoClient('mongodb://localhost:27017')

# get pymongo test database
db = client['pymongo_test']

# gets the inventory collection from pymongo_test
collection = db.inventory


# prepare aggregate pipeline with $project
aggregate_pipline =[
      {
        "$match": {
          "sizes": "S"
        }
      },
      {
        "$project": {
          "item_id": {
                "$split": [
                  "$item",
                  "_"
                ]
          }
        }
      }
    ]

# aggregate query
cursor = collection.aggregate(aggregate_pipline)
for doc in cursor:
    print(doc)