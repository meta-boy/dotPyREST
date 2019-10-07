import pymongo


class DatabaseHandler:
    def __init__(self, client:  pymongo.MongoClient, username = None, password = None):
        self.username = username
        self.password = password
        self.data = None
        self.client = client
        self.cursor = self.client["dotpy"]["users"]




    def create(self, data):
        try:
            for k, v in data.items():
                self.cursor.insert_one({"user": k, "value": v})
                self.fetch(k)
        except Exception as e:
            self.data = {"error": {"value": e.__class__.__name__}}
            print(e)
            pass
        pass
    

    def delete(self, user):
        try:
            self.cursor.delete_one({"user": user})
            self.data = {"deleted": True}
        except Exception as e:
            self.data = {"error": {"value": e.__class__.__name__}}

    def update(self, data):
        try:
            for k, v in data.items():
                self.fetch(k)
                newData = {"$set": {"value": v}}
                self.cursor.update_one({"value": self.data["value"]}, newData)
                self.fetch(k)
        except Exception as e:
            print(e)
            self.data = {"error": {"value": e.__class__.__name__}}
            
        pass

    def fetch(self, user):
        for x in self.cursor.find():
            if user == x["user"]:
                self.data = x
                break
        