import os.path
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


def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler)
            ],
        cookie_secret="Figure this out later",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsfr_cookies=True,
        debug = options.debug,
    )

    tornado.options.parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
