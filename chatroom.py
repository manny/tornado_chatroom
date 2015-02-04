import logging
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.options

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info("message served")
        self.write("too far away!")

application = tornado.web.Application([
    (r"/", MainHandler)
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
