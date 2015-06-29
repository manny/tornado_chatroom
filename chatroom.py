import logging
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.options import define, options, parse_command_line

define ("port", default=8888, help="run on the given port", type=int)
define ("debug", default=False, help="run in debug mode")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info("message served")
        self.write("too far away!")

application = tornado.web.Application([
    (r"/", MainHandler)], options.debug
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
