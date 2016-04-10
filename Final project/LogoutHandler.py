# -*- coding: utf-8 -*-

import tornado.wsgi
import tornado.web
import os.path

import sae.const
import sae.kvdb
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Classes import *

class LogoutHandler(tornado.web.RequestHandler):
    """
        LogoutHandler
    """
    def get(self):
        # deal with logout
        self.clear_cookie("name")
        self.redirect("/")