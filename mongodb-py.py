import pymongo
import time
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
dbname = "kobra"
if dbname in dblist:
    print("The database %s exists." % (dbname))
mydb = myclient[dbname]

collist = mydb.list_collection_names()
collection = "customers"
if collection in collist:
    print("The collection %s exists." % (collection) )
mycol = mydb[collection]

x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

mydict = { "name": "John", "address": "Highway 37" }
mydict["modify_time"] = time.time()
x = mycol.insert_one(mydict)
print('one document %s inserted, total document is %d'  % (x.inserted_id,  mycol.count() ) )

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

for x in mylist:
    print(x)
    x["modify_time"] = time.time()


for x in mylist:
    print(x)
    y =  x["modify_time"]
    print( datetime.fromtimestamp(y) )
