from pymongo import MongoClient

# instantiate Mongo Client
client = MongoClient('mongodb://localhost:27017')

# get pymongo test database
db = client['pymongo_test']

# gets the inventory collection from pymongo_test
collection = db.inventory


# prepare aggregate pipeline with unwind
aggregate_pipline = [{"$unwind":"$sizes"}]

# aggregate query
cursor = collection.aggregate(aggregate_pipline)
for doc in cursor:
    print(doc)


"""
Unwind with some optional params, like path, includeArrayIndex, preserveNullAndEmptyArrays

Unwind with path param:
Here with param or without param will result into same results

"""
db.inventory.aggregate( [ { "$unwind": "$sizes" } ] )
db.inventory.aggregate( [ { "$unwind": { "path": "$sizes" } } ] )

'''
The result from above operation as follows

{ "_id" : 1, "item" : "ABC", "sizes" : "S" }
{ "_id" : 1, "item" : "ABC", "sizes" : "M" }
{ "_id" : 1, "item" : "ABC", "sizes" : "L" }
{ "_id" : 3, "item" : "IJK", "sizes" : "M" }

'''


'''

Unwind with includeArrayIndex param:

The operation unwinds the sizes array and includes the array index of the array index in the new arrayIndex field. 
If the sizes field does not resolve to an array but is not missing, null, or an empty array, the arrayIndex field is null.

'''
db.inventory.aggregate( [ { "$unwind": { "path": "$sizes", "includeArrayIndex": "arrayIndex" } } ] )

'''
The result from the above operation as follows

{ "_id" : 1, "item" : "ABC", "sizes" : "S", "arrayIndex" : NumberLong(0) }
{ "_id" : 1, "item" : "ABC", "sizes" : "M", "arrayIndex" : NumberLong(1) }
{ "_id" : 1, "item" : "ABC", "sizes" : "L", "arrayIndex" : NumberLong(2) }
{ "_id" : 3, "item" : "IJK", "sizes" : "M", "arrayIndex" : null }

'''

'''
Unwind with preserveNullAndEmptyArrays:

In addition to unwinding the documents where the sizes is an array of elements or a non-null, non-array field, the operation outputs, without modification, those documents where the sizes field is missing, null or an empty array

'''
db.inventory.aggregate( [
   { "$unwind": { "path": "$sizes", "preserveNullAndEmptyArrays": True } }
] )

'''
The result from the above operation as follows

{ "_id" : 1, "item" : "ABC", "sizes" : "S" }
{ "_id" : 1, "item" : "ABC", "sizes" : "M" }
{ "_id" : 1, "item" : "ABC", "sizes" : "L" }
{ "_id" : 2, "item" : "EFG" }
{ "_id" : 3, "item" : "IJK", "sizes" : "M" }
{ "_id" : 4, "item" : "LMN" }
{ "_id" : 5, "item" : "XYZ", "sizes" : null }

'''