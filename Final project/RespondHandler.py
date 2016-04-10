# -*- coding: utf-8 -*-

import tornado.wsgi
import tornado.web
import os.path

import sae.const
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Classes import *

class RespondHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("name"):
            self.redirect("/login")
            return
        url = self.request.uri

        ############   这里需要修改。
        url = url[1:]
        self.render("respond.html", user = self.get_secure_cookie("name"), number_of_article = url)

    def post(self):
        conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,
                             user=sae.const.MYSQL_USER,
                             passwd=sae.const.MYSQL_PASS,
                             db=sae.const.MYSQL_DB,
                             port=int(sae.const.MYSQL_PORT),
                             charset='utf8')
        cur = conn.cursor()
        conn.select_db('app_forum423423')    

        

        content = self.get_argument("content")
        writer = self.get_secure_cookie("name")
        num_vote = 0
        url = self.request.uri

        ############   这里需要修改。
        url = url[8:]
        floor_id = cur.execute("SELECT * FROM Article%s" % url)
        floor_id = int(floor_id) + 1
        upda = "Update ArticleTable SET answer=%d WHERE article_id=%d" % (floor_id, int(url))
        cur.execute(upda)
        value = [floor_id, num_vote, content, writer]
        
        
        #answer + 1
        sql = "insert into Article%s" % url
        cur.execute(sql + " values(%s,%s,%s,%s)", value)

        conn.commit()
        cur.close()
        conn.close()
        self.redirect("/"+url)