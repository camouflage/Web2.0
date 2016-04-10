# -*- coding: utf-8 -*-

import tornado.wsgi
import tornado.web
import os.path

import sae.const
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from IndexHandler import IndexHandler
from ContentHandler import ContentHandler
from AskHandler import AskHandler
from RespondHandler import RespondHandler
from SignupHandler import SignupHandler
from LoginHandler import LoginHandler
from LogoutHandler import LogoutHandler
#from VoteHandler import VoteHandler
from Classes import *


settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
    "cookie_secret": "EAzKXQAGa765YdkL5gEmheJJFuYh7EQnp2XdTP1o/Vo=",
}

app = tornado.wsgi.WSGIApplication([
    (r"/signup", SignupHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/ask", AskHandler),
    (r"/respond[0-9]+", RespondHandler),
    (r"/[0-9]+", ContentHandler),
    (r"/", IndexHandler),
], **settings)

application = sae.create_wsgi_app(app)