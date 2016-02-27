from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import logging
 
#Examples: 
#http://localhost:8888/getgamebyid/500
#http://localhost:8888/version
 
#Website
#http://www.drdobbs.com/open-source/building-restful-apis-with-tornado/240160382?pgno=1

#http://localhost:8888/?greeting={"34":35,"35":36}
#https://www.safaribooksonline.com/library/view/introduction-to-tornado/9781449312787/ch01s02.html

from tornado.log import enable_pretty_logging
enable_pretty_logging()
 
class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '3.5.1',
                     'last_build':  date.today().isoformat() }
        data = self.request.body
        print(data)
        self.write(response)
 
class GetGameByIdHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = { 'id': int(id),
                     'name': 'Crazy Game',
                     'release_date': date.today().isoformat() }
        self.write(response)
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        response = {"hello":"world"}
        greeting = self.get_argument('greeting', 'Hello')
        logging.info("Hello world")
        print(greeting)
        self.write(greeting)
application = tornado.web.Application([
    (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
    (r"/version", VersionHandler),
    (r"/", TestHandler)
    #(r"/test/(?P<param1>[^\/]+)/?", TestHandler)
])
 
if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()