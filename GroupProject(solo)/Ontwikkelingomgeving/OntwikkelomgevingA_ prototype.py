from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.huwebshop
productsCollection = db.products

print(db)
print(productsCollection)
print("")

first = productsCollection.find()
for i in first:
    print("Naam:", i["name"])
    print("Prijs:", i["price"]["mrsp"])
    print("")
    break

# dit kan ook:
# first = productsCollection.find_one({}, {"_id": 0, "name": 1, "price.mrsp": 1})
# for i, j in first.items():
#     if isinstance(j, dict):
#         for k in j:
#             print(i + ":", j[k])
#     else:
#         print(i + ":", j)
# print("")


find = productsCollection.find()
for i in find:
    if i["brand"][0] == "R":
        print("Merknaam:", i["brand"])
        print("")
        break

# dit kan ook!
# find = productsCollection.find({"brand": {"$regex": "^R"}})
# for i in find:
#     print(i["brand"])
#     break

prices = productsCollection.find()
lst = []
for i in prices:
    lst.append(i["price"]["mrsp"])
average = sum(lst) / len(lst)
print("Het gemiddelde is van alle prijzen is:", int(average))

# kan ook
# prices = productsCollection.find({}, {"_id": 0, "price.mrsp": 1})
