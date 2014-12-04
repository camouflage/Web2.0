# -*- coding: utf-8 -*-
"""
13331231 孙圣 pretest2 main.py
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
            (r"^/login$", LoginHandler),
            (r"^/[a-z]+/[a-z]+/[0-9]+$", BlogHandler),
            (r"^/logout$", LogoutHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="71oETzKXQGGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class LoginHandler(tornado.web.RequestHandler):
    """
        LoginHandler
    """
    def get(self):
        self.render(
            "index.html",
            errormsg = ""
        )

    def post(self):
        # get argument
        user = self.get_argument("user")
        pwd = self.get_argument("pwd")

        # read from users.txt
        userfile = open("users.txt", "r")
        users = dict()
        for line in userfile:
            users[line.split(",")[0]] = line.split(",")[1]
        userfile.close()

        # validate and set cookie
        valid = 0
        if user in users and users[user] == pwd:
            valid =  1
        if valid == 1:
            self.set_secure_cookie("user", user)
            #self.set_secure_cookie("pwd", pwd)
        else:
            # TO DO: 404
            return

        # read from blog.txt to determine the url
        blogfile = open("blog.txt", "r")
        line = blogfile.readline()
        author = line.split(":")[1]
        blogfile.close()
        self.redirect("/" + user + "/" + author + "/1")     

class BlogHandler(tornado.web.RequestHandler):
    """
        BlogHandler
    """
    def get(self):
        # read from blog.txt and display
        blogfile = open("blog.txt", "r")
        line = blogfile.readline().strip()
        bloginfo = line.split(":")
        title = bloginfo[0]
        author = bloginfo[1]
        article = bloginfo[2]

        login = 1
        user = ""
        if not self.get_secure_cookie("user"):
            login = 0
        else:
            user = self.get_secure_cookie("user")

        url = "/" + user + "/" + author + "/1"
        self.render(
            "blog.html",
            title = title,
            author = author,
            article = article,
            login = login,
            user = user,
            url = url
        )

    def post(self):
        comment = self.get_argument("comment")
        self.get()

class LogoutHandler(tornado.web.RequestHandler):
    """
        LogoutHandler
    """
    def post(self):
        self.clear_cookie("user")
        self.render(
            "logout.html"
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
