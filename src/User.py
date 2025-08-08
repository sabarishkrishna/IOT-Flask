from src.DbConn import DbConn
import random
import json

class User:
    def __init__(self, id):
       print("user wiith {}".format(id))
       db = DbConn.get_connection()
       print(list(db.admins.find()))
    

    @staticmethod
    def register(username, password, confirm_password):
        db = DbConn.get_connection()
        admins = db.admins
        if password != confirm_password:
            raise Exception("[*] Please enter correct password!")
        
        try:
            id = admins.insert_one({
                "username": username,
                "password": password,
                "activate_token":random.randint(1000, 9999)

            })

            return id
        except:
            return "Some error occurred"
        
    @staticmethod
    def login(username, password):
        db = DbConn.get_connection()
        data = db.admins.find_one({"username" : username})
        if data['password'] == password:
            print("[*] User logged in....")
        else:
            raise Exception("[*] Please enter correct password")
        