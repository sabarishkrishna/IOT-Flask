from pymongo.mongo_client import MongoClient
import certifi
from src import get_config


class DbConn:
    @staticmethod
    def get_connection(database=None):
        # Create a new client and connect to the server
        client = MongoClient(get_config("mongodb_connection_string"), tlsCAFile=certifi.where())

        if database is None:
            return client[get_config("mongodb_database")]
        else:
            return client[database]