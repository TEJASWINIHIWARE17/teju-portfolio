from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = MongoClient(MONGODB_URL)

database = client[DATABASE_NAME]

contacts_collection = database["contacts"]


def check_database_connection():
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully")
        return True

    except Exception as error:
        print("MongoDB connection failed:", error)
        return False