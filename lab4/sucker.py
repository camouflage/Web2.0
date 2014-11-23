# -*- coding: utf-8 -*-
"""
13331231 孙圣 lab4 sucker.py
"""

import os.path

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
            (r"/", SuckerHandler),
            (r"/info", InfoHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
            )
        tornado.web.Application.__init__(self, handlers, **settings)

class SuckerHandler(tornado.web.RequestHandler):
    """
        SuckerHandler:
            get query parameter and render the html
    """
    def get(self):
        self.render(
            "buyagrade.html"
        )

class InfoHandler(tornado.web.RequestHandler):
    """
        InfoHandler:
            render the html
    """
    def get(self):
        name = self.get_argument("name")
        section = self.get_argument("section")
        ccnum = self.get_argument("ccnum")
        cc = self.get_argument("cc")

        # check: fill in all the info
        if ( name == "" or section == "(Select a section)" or ccnum == "" or cc == "none" ):
            self.render("error.html",
                        errormessage="You didn't fill out the form completely.")
            return

        # check: valid ccnum
        valid = True
        valid = ccnum.isdigit() and len(ccnum) == 16
        if cc == "visa":
            valid = ccnum[0] == '4'
        if cc == "mastercard":
            valid = ccnum[0] == '5'

        #
        if not valid:
            self.render("error.html",
                        errormessage="You didn't provide a valid card number.")
            return

        # write to file
        infofile = open("suckers.txt", "a")
        infofile.write(";".join([name, section, ccnum, cc]) + '\n')
        infofile.close()

        # read from file
        infofile = open("suckers.txt", "r")
        info = infofile.read()
        infofile.close()

        self.render(
            "sucker.html",
            name=name,
            section=section,
            ccnum=ccnum,
            cc=cc,
            info=info
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
