from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import logging
  
#Website
#http://www.drdobbs.com/open-source/building-restful-apis-with-tornado/240160382?pgno=1

#http://localhost:8898/?get_json={"34":35,"35":36}
#https://www.safaribooksonline.com/library/view/introduction-to-tornado/9781449312787/ch01s02.html

from tornado.log import enable_pretty_logging
enable_pretty_logging() 

class RESTHandler(tornado.web.RequestHandler):
    def get(self):
        json_request = self.get_argument('get_json')
        logging.info("RESTHandler Request")
        logging.info(json_request)
        self.write('{"return":"good"}')
application = tornado.web.Application([
    (r"/", RESTHandler)
])
 
if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()