from __future__ import absolute_import

import os
from config import Env
import tornado.web
import tornado.httpserver
import tornado.ioloop

from tornado.options import define, options
define("port", default=3000, type=int)
define("env", default='dev', type=str)

_ROOT_PATH = os.path.dirname(__file__)
ROOT_JOIN  = lambda sub_dir: os.path.join(_ROOT_PATH, sub_dir)

from controller import *
from model import DB

class Application(tornado.web.Application):
    def __init__(self, router, NotFound = None, **settings):
        default = dict(
            template_path         = ROOT_JOIN('view'),
            static_path           = ROOT_JOIN('static'),
            cookie_secret         = Env.COOKIE_SEC,
            default_handler_class = NotFound
        )
        super().__init__(handlers=router, **{**default, **settings})
        # service start mongod 
        # self.model = DB(Env)

def main():
    router = [
        (r'/', HomeHandler),
    ]
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(router, My404, debug=(options.env == 'dev')))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()
