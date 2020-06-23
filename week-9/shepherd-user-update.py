#==============================================================================
# Title:  shepherd-user-service.py
# Author: Jeff Shepherd
# Date:   6/23/2020
# Modified By:
# Description: user update
#==============================================================================

import pymongo.mongo_client
import pprint
import datetime

# connect to local MongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client.web335

# update email address
db.users.update_one( {"employee_id": "0000008"},
  {
    "$set": {
      "email": "cdebussy@bellevue.edu"
    }
  }
)

# output fields using find one
pprint.pprint(db.users.find_one(
  {"employee_id": "0000008"}
))
