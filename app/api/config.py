from pymongo import MongoClient
import os

def db_connection():
    try:
        connection =MongoClient( os.environ.get('mongo_uri'))
        return connection
    except Exception as error:
        print(error)
    # finally:
    #     connection.close()
