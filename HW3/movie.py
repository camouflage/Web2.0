# -*- coding: utf-8 -*-
"""
13331231 孙圣 hw3 movie.py
"""

import collections

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# class review
class Review(object):
    def __init__(self, info, like, name, where):
        self.info = info
        self.like = like
        self.name = name
        self.where = where

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
            shortcuticon = "rotten.gif"
        else:
            bigpicurl = "3/freshbig.png"
            shortcuticon = "fresh.gif"
        infofile.close()

        # read from generaloverview.txt
        generalfile = open(os.path.join(film_path, "generaloverview.txt"), 'r')
            # ensure order
        generaloverview = collections.OrderedDict()
        for line in generalfile:
            golist = line.split(':')
            generaloverview[golist[0]] = golist[1]
        generalfile.close()

        # read from review
        reviewfilelist = os.listdir(film_path)
        reviewlist = []
        for myfile in reviewfilelist:
            if myfile[:6] == "review":
                reviewfile = open(os.path.join(film_path, myfile), 'r')
                info = reviewfile.readline()
                if reviewfile.readline().strip() == "FRESH":
                    like = "fresh.gif"
                else:
                    like = "rotten.gif"
                name = reviewfile.readline()
                where = reviewfile.readline()
                review = Review(info, like, name, where)
                reviewlist.append(review)
                reviewfile.close()

        # decide left or right
        leftlist = reviewlist[:len(reviewlist) / 2]
        rightlist = reviewlist[len(reviewlist) / 2:]   

        # render
        self.render(
                    "movie.html",
                    moviename=film,
                    title=title,
                    year=year,
                    rating=rating,
                    reviewnum=reviewnum,
                    bigpicurl=bigpicurl,
                    generaloverview=generaloverview,
                    leftlist=leftlist,
                    rightlist=rightlist,
                    pagereviewnum=len(reviewlist),
                    shortcuticon=shortcuticon
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
