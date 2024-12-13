#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.logs
collection = db.nginx
total_logs = collection.count_documents({})
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}
status_get_count = collection.count_documents({"method": "GET", "path": "/status"})
print("OK")
