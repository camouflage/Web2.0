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
    def __init__(self, infolist):
        self.name = infolist[0]
        # deal with the pic name
        nameunderscore = self.name.lower()
        nameunderscore = nameunderscore.replace(" ", "_")
        nameunderscore += ".jpg"
        pic_path = os.path.join(os.path.dirname(__file__), "static/images")
        pic_list = os.listdir(pic_path)
        if nameunderscore in pic_list:
            self.nameunderscore = nameunderscore
        else:
            self.nameunderscore = "default_user.jpg"

        self.gender = infolist[1]
        self.age = int(infolist[2])
        self.personality = infolist[3]
        self.os = infolist[4]
        """
        # deal with seeking
        self.seekingmale = False
        self.seekingfemale = False
        if "M" in infolist[5]:
            self.seekingmale = True
        if "F" in infolist[5]:
            self.seekingfemale = True
        """
        self.seeking = infolist[5]
        self.lage = int(infolist[6])
        self.hage = int(infolist[7])

    def setrating(self, rating):
        """
            setrating
        """
        self.rating = rating

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

        newsingleinfolist = [name, gender, age, personality, os, "".join(seeking), lage, hage]
        newsingle = Single(newsingleinfolist)

        # read all other singles from file
        singles = open("singles.txt", "r")
        singleslist = []
        for line in singles:
            line.strip()
            singlesinfolist = line.split(",")
            single = Single(singlesinfolist)
            singleslist.append(single)
        singles.close()

        # save the new single to file
        singles = open("singles.txt", "a")
        singles.write("\n" + ",".join(newsingleinfolist))
        singles.close()

        suitablesingles = []
        for single in singleslist:
            append = True
            if not (newsingle.gender in single.seeking and single.gender in newsingle.seeking):
                append = False
            # deal with rating
            rating = 0
            if newsingle.age >= single.lage and newsingle.age <= single.hage and single.age >= newsingle.lage and single.age <= newsingle.hage:
                rating += 1
            if single.os == newsingle.os:
                rating += 2
            for i in range(4):
                if newsingle.personality[i] == single.personality[i]:
                    rating += 1
            if rating < 3:
                append = False

            if append:
                single.setrating(rating)
                suitablesingles.append(single)

        self.render(
            "results.html",
            name=name,
            suitablesingles=suitablesingles
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
