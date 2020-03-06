from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.huwebshop
productsCollection = db.products

print(db)
print(productsCollection)
print("")

first = productsCollection.find_one({}, {"_id": 0, "name": 1, "price.mrsp": 1})
for i, j in first.items():
    if j == type({}):
        for k, l in j.items():
            print(i, ":", l)
    else:
        print(i, ":", j)
print("")

findLetter = productsCollection.find({"brand": {"$regex": "^R"}})
for i in findLetter:
    print(i["brand"])
    break

prices = productsCollection.find({"price.mrsp": 1})
for i in prices:
    print(i)
