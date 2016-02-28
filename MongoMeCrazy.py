#MongoDB Me Crazy - Practice Python File

from pymongo import MongoClient

client = MongoClient()
db = client.kirk

result = db.test.insert_one(
    { "34":34}
)

print result.inserted_id
