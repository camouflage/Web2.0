# -*- coding: utf-8 -*-
"""
13331231 孙圣 hw3 movie.py
"""

import random

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# class song
class Song(object):
    """
        class Song, store the song info
    """
    def __init__(self, name, size):
        self.name = name
        # in bytes
        self.size = size

# application configuration
class Application(tornado.web.Application):
    """
        class Application:
            set handler & path
    """
    def __init__(self):
        handlers = [
            (r"/", MovieHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
            )
        tornado.web.Application.__init__(self, handlers, **settings)

class MovieHandler(tornado.web.RequestHandler):
    """
        MovieHandler:
            get movie name and render the specific html
    """
    def get(self):
        film = self.get_argument("film")
        film_path = os.path.join(os.path.dirname(__file__), "static/moviefiles/" + film)
        # file_list = os.listdir(film_path)

        # read from info.txt
        infofile = open(os.path.join(film_path, "info.txt"), 'r')
        title = infofile.readline()
        year = infofile.readline()
        rating = infofile.readline()
        reviewnum = infofile.readline()
        # rating
        if int(rating) < 60:
            bigpicurl = "2/rottenbig.png"
        else:
            bigpicurl = "3/freshbig.png"

        self.render("movie.html",
                    moviename=film,
                    title=title,
                    year=year,
                    rating=rating,
                    reviewnum=reviewnum,
                    bigpicurl=bigpicurl
        )

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
