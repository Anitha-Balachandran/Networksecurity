from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://writetoanithalidiya:<password>@cluster0.5ztpm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

from pymongo.mongo_client import MongoClient
import certifi  # Import certifi for SSL certificates


# Create a new client and connect to the server with certifi certificate
client = MongoClient(uri, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error: {e}")
