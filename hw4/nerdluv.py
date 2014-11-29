# -*- coding: utf-8 -*-
"""
13331231 孙圣 hw4 nerdLuv.py
"""
import os.path
import re

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# application configuration
class Application(tornado.web.Application):
    """
        class Application:
            set handler & path
    """
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/result", ResultHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True
            )
        tornado.web.Application.__init__(self, handlers, **settings)

class Single(object):
    """
        class Single storing info
    """
    def __init__(self, name, gender, age, personality, os, seeking, lage, hage):
        self.name = name
        self.gender = gender
        self.age = age
        self.personality = personality
        self.os = os
        self.seeking = seeking
        self.lage = lage
        self.hage = hage

class IndexHandler(tornado.web.RequestHandler):
    """
        IndexHandler
    """
    def get(self):
        self.render(
            "index.html"
        )

class ResultHandler(tornado.web.RequestHandler):
    """
        ResultHandler
    """
    def post(self):
        # get info from query parameter
        name = self.get_argument("name")
        gender = self.get_argument("gender")
        age = self.get_argument("age")
        personality = self.get_argument("personality")
        os = self.get_argument("os")
        seeking = self.get_arguments("seeking")
        lage = self.get_argument("lage")
        hage = self.get_argument("hage")

        # save to file
        signuplist = [name, gender, age, personality, os, "".join(seeking), lage, hage]
        singles = open("singles.txt", "a")
        singles.write("\n" + ",".join(signuplist))
        singles.close()

        # read all singles from file
        singles = open("singles.txt", "r")
        for line in singles:
            line.strip()
            singlesinfolist = line.split(",")
            

        singles.close()
        #self.render("results.html")


def main():
    """
        Start it up
    """
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
