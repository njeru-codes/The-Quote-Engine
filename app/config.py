from pydantic import BaseSettings
from pymongo import MongoClient


class Settings(BaseSettings):
    mongo_uri:str
    class Config:
        env_file = ".env"

settings = Settings()

def db_connection():
    try:
        connection =MongoClient( settings.mongo_uri)
        return connection
    except Exception as error:
        print(error)
    # finally:
    #     connection.close()
