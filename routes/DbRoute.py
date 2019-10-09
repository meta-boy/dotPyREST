import pymongo
import tornado.web
from modules.databaseHandler import DatabaseHandler
from config import config
from tornado import gen
import json
client = pymongo.MongoClient(f"mongodb://localhost:{config['DBPORT']}/")


class UserCreate(tornado.web.RequestHandler):

    @gen.coroutine
    def post(self):     
        user = self.get_argument("user", default=None)
        output = self.get_argument("output", default=None)
        
        data = {
            user : {
                "output": output
            }
        }

        d = DatabaseHandler(client)
        try:
            if data:
                d.create(data)
                dataToSend = {
                    "user": d.data["user"],
                    "value": d.data["value"]
                }
                self.write(dataToSend)
            else:
                self.send_error(400)
        except Exception as e:
            print(e)

            self.send_error(500)


class UserFetch(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        user = self.get_argument("user", default=None)
        d = DatabaseHandler(client)
        print("OK")
        try:
            if user:
                d.fetch(user)
                dataToSend = {
                    "user": d.data["user"],
                    "value": d.data["value"]
                }

                self.write(dataToSend)
            else:
                self.send_error(400)
        except Exception as e:
            print(e)

            self.send_error(404)


class UserDelete(tornado.web.RequestHandler):

    @gen.coroutine
    def delete(self):
        user = self.get_argument("user", default=None)
        d = DatabaseHandler(client)
        print(user)
        try:
            if user:
                d.delete(user)
                dataToSend = {
                    "deleted": d.data["deleted"]
                }
                self.write(dataToSend)
            else:
                self.send_error(400)
        except Exception as e:
            print(e)

            self.send_error(404)


class UserUpdate(tornado.web.RequestHandler):
    @gen.coroutine
    def post(self):
        data = self.get_argument("data", default=None)
        data = json.loads(str(data))
        d = DatabaseHandler(client)
        try:
            if data:
                d.update(data)
                dataToSend = {
                    "user": d.data["user"],
                    "value": d.data["value"]
                }
                self.write(dataToSend)
            else:
                self.send_error(400)
        except Exception as e:
            print(e)
            self.send_error(500)


class UserFetchAll(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        d = DatabaseHandler(client)
        try:
            data = d.fetchall()
            self.write(data)
        except Exception as e:
            print(e)
            self.send_error(404)


class ShowAll(tornado.web.RequestHandler):  
    
    @gen.coroutine
    def get(self):
        d = DatabaseHandler(client)
        try:
            data = d.fetchall()
            self.render("../templates/users.html", data = data)
        except Exception as e:
            print(e)
            self.write_error(404)


class EnterUserName(tornado.web.RequestHandler):
    
    @gen.coroutine
    def get(self):
        data = self.get_argument("data", default= None)
        self.render("../templates/fill.html", data = data)