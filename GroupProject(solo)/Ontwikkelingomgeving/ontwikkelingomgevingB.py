from pymongo import MongoClient
import mysql.connector
import MySQLdb.cursors
import random

client = MongoClient('localhost', 27017)

db = client.huwebshop
productsCollection = db.products

print(db)
print(productsCollection)
print("")

temptype = MySQLdb.cursors.DictCursor

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="11326",
    db="huwebshop"
)
mycursor = mydb.cursor(MySQLdb.cursors.DictCursor)

print(mydb)


# def migrate():
#     collection = productsCollection.find()
#
#     for i in collection:
#         _id = i.get("_id")
#         productName = i.get("name")
#         price = i["price"]["mrsp"]
#
#         sql = "INSERT INTO Products (_id, productName, price) VALUES (%s, %s, %s)"
#         val = (_id, productName, price)
#         mycursor.execute(sql, val)
#         mydb.commit()
#     print(mycursor.rowcount, "record inserted.")
#
# migrate()

def selectTable():
    mycursor.execute("SELECT * FROM Products")
    myresult = mycursor.fetchall()

    for x in myresult:
        return (x)


def priceAverage():
    lst = []
    for i in selectTable():
        lst.append(i["price"])
    average = sum(lst) / len(lst)
    print("Het gemiddelde is van alle prijzen is:", int(average))


priceAverage()


# def randomChooserAverageCalc():
#     lst = []
#     for i in selectTable():
#         lst.append(i)
#     random = random.choice(lst["price"])




