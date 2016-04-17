import tornado.escape
import tornado.ioloop
import tornado.web

#os.path.join(os.path.dirname(__file__)
class RESTHandler(tornado.web.RequestHandler):
    def get(self):
        
        logging.error("howdy")
        self.write('{"return":"good"}')

static_path = "/Users/kirk/Documents/GoPiGo/GoKirkGo/web/"

application = tornado.web.Application([
    (r"/", RESTHandler),
    (r"/web/(.*)",tornado.web.StaticFileHandler, {"path": static_path})
])
 
if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()