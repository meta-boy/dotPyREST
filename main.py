import tornado.ioloop
import tornado.web
import pymongo
from routes.DbRoute import *


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/user/create', UserCreate),
        (r'/user/delete', UserDelete),
        (r'/user/update', UserUpdate),
        (r'/user/fetch', UserFetch),

    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(config["port"])
    tornado.ioloop.IOLoop.current().start()
