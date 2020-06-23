#==============================================================================
# Title:  shepherd-user-service.py
# Author: Jeff Shepherd
# Date:   6/23/2020
# Modified By:
# Description: user service
#==============================================================================

import pymongo.mongo_client
import pprint
import datetime

# connect to local MongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client.web335

# create new user document
user = {
  "first_name": "Claude",
  "last_name": "Debussy",
  "email": "cdebussy@me.com",
  "employee_id": "0000008",
  "date_created": datetime.datetime.utcnow()
}

# insert new user document
user_id = db.users.insert_one(user).inserted_id

# output the auto-generated user_id
print(user_id)

# query users collection and print the returned doc
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))
