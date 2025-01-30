import os
import sys
import json
import pandas as pd
import numpy as np
import pymongo
from dotenv import load_dotenv
import certifi
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Load environment variables
load_dotenv()

# Get MongoDB URL from .env file
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

# MongoDB SSL certification setup using certifi
ca = certifi.where()


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    # Convert CSV to JSON format for MongoDB insertion
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    # Insert records into MongoDB
    def insert_data_mongodb(self, records, database, collection):
        try:
            # Connect to MongoDB using pymongo
            self.database = database
            self.collection = collection
            self.records = records

            # MongoDB client with SSL verification disabled
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL, tls=True, tlsCAFile=ca
            )
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            # Insert the records into the collection
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


# Main function to execute
if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"  # Define your CSV file path
    DATABASE = "phishing_detection_db"  # MongoDB database name
    Collection = "NetworkData"  # MongoDB collection name

    # Initialize the NetworkDataExtract class and perform operations
    networkobj = NetworkDataExtract()

    # Convert CSV data to JSON
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)

    # Insert the records into MongoDB
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(f"Inserted {no_of_records} records into MongoDB.")
