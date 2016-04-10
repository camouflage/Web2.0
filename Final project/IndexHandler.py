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


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        """
            deal with login
        """
        login = 0
        name = self.get_secure_cookie("name")
        #name = self.get_cookie("name")
        if name:
            login = 1
            
        """
            article
        """
        articleList = []

        # database
        conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,
                             user=sae.const.MYSQL_USER,
                             passwd=sae.const.MYSQL_PASS,
                             db=sae.const.MYSQL_DB,
                             port=int(sae.const.MYSQL_PORT),
                             charset='utf8')
        cur = conn.cursor()
        conn.select_db('app_forum423423')

        querysql = "SELECT * FROM ArticleTable ORDER BY article_id"
        cur.execute(querysql)
        result = cur.fetchall()
        
        conn.commit()
        cur.close()
        conn.close()

        for res in result:
            art = Article(res)
            articleList.append(art)

        self.render("index.html",
                    name=name,
                    login=login,
                    articleList=articleList)