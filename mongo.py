Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@JamesSinnott1994 
Code-Institute-Solutions
/
MongoDB
2
11
6
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
MongoDB/03-ManipulateDataProgrammaticallyWithPython/01-run_mongo_commands_from_a_python_file/mongo.py /
@TravelTimN
TravelTimN Flask Rebuild 2020
Latest commit d4256c1 on 3 Aug 2020
 History
 1 contributor
81 lines (66 sloc)  1.83 KB
  
import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()

""" Insert a single document """
# new_doc = {
#     "first": "douglas",
#     "last": "adams",
#     "dob": "11/03/1952",
#     "gender": "m",
#     "hair_color": "grey",
#     "occupation": "writer",
#     "nationality": "british"
# }
# coll.insert(new_doc)

""" Insert multipe documents """
# new_docs = [{
#     "first": "terry",
#     "last": "pratchett",
#     "dob": "28/04/1948",
#     "gender": "m",
#     "hair_color": "not much",
#     "occupation": "writer",
#     "nationality": "british"
# }, {
#     "first": "george",
#     "last": "rr martin",
#     "dob": "20/09/1948",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "nationality": "american"
# }]
# coll.insert_many(new_docs)

""" Find documents with 'first' name set to 'douglas' """
# documents = coll.find({"first": "douglas"})

""" Delete documents with 'first' name set to 'douglas' """
# coll.remove({"first": "douglas"})
# documents = coll.find()

""" Update a single document (first one only) """
# coll.update_one(
#     {"nationality": "american"},
#     {"$set": {"hair_color": "maroon"}}
# )
# documents = coll.find({"nationality": "american"})

""" Update all documents """
# coll.update_many(
#     {"nationality": "american"},
#     {"$set": {"hair_color": "maroon"}}
# )
# documents = coll.find({"nationality": "american"})

for doc in documents:
    print(doc)