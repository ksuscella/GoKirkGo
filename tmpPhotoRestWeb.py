from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import logging
import cv2
import json
import base64
from pymongo import MongoClient     #Load Results into MongoDB
import numpy as np
import urllib
import StringIO

#Website
#http://www.drdobbs.com/open-source/building-restful-apis-with-tornado/240160382?pgno=1

#http://localhost:8898/?get_json={"34":35,"35":36}
#https://www.safaribooksonline.com/library/view/introduction-to-tornado/9781449312787/ch01s02.html

#from tornado.log import enable_pretty_logging
#enable_pretty_logging() 

client = MongoClient()
db = client.kirk

class ImageHandler(tornado.web.RequestHandler):
    def post(self):
        logging.error("posting")
        # get post data
        file_body = self.request.files['capture.jpg'][0]['body']
        
        fh = open("/Users/kirk/Documents/GoPiGo/GoKirkGo/onWeb.png", "wb")
        fh.write(file_body)
        fh.close()
        
        

class RESTHandler(tornado.web.RequestHandler):
    def get(self):
        #json_request = self.get_argument('get_json')
        #image_request = self.get_argument('get_image')
        logging.error("howdy")
        #image_request =urllib.unquote(image_request).decode('utf8')
        #convert = base64.b64decode(image_request)

        #t = open("/Users/kirk/Documents/GoPiGo/GoKirkGo/capture2.jpg", "w+")
        #t.write(convert)
        #t.close()
        
        #self.write('{"return":"good"}')
application = tornado.web.Application([
    (r"/", RESTHandler),
    (r"/image", ImageHandler)
    
])
 
if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()