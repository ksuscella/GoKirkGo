import logging

#http://localhost:8888/version
#http://localhost:8888/getgamebyid/500

from datetime import date
import random
import time
import tornado.escape
import tornado.ioloop
import tornado.web

import Robot

tracker = 0 
 
class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '3.5.1',
                     'last_build':  date.today().isoformat() ,
                     'loop': Robot.getCount}
        self.write(response)
 
class GetGameByIdHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = { 'id': int(id),
                     'name': 'Crazy Game',
                     'release_date': date.today().isoformat() }
        self.write(response)
 
application = tornado.web.Application([
    (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
    (r"/version", VersionHandler)
])
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    Robot.robot()
    
    