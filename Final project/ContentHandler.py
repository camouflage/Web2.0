# -*- coding: utf-8 -*-

import tornado.wsgi
import tornado.web
import os.path


import sae.const
import MySQLdb
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Classes import *

class ContentHandler(tornado.web.RequestHandler):
    def get(self):
        """
            deal with login
        """
        login = 0
        name = self.get_secure_cookie("name")
        if name:
            login = 1
            
        # get url
        url = self.request.uri
        url = url[1:]
        num = int(url)
        
        """
            #of view
        """
        # database
        conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,
                             user=sae.const.MYSQL_USER,
                             passwd=sae.const.MYSQL_PASS,
                             db=sae.const.MYSQL_DB,
                             port=int(sae.const.MYSQL_PORT),
                             charset='utf8')
        cur = conn.cursor()
        conn.select_db('app_forum423423')

        querysql = "SELECT * FROM ArticleTable WHERE article_id=%d" %num
        count = cur.execute(querysql)
        if count == 0:
            self.redirect("/")
            return
        
        scan = cur.fetchone()

        querysql = "UPDATE ArticleTable SET scan=%d WHERE article_id=%d" %(scan[2]+1, num)
        cur.execute(querysql)

        """
            display
        """

        floorList = []
        querysql = "SELECT * FROM Article%d ORDER BY floor_id" %num
        cur.execute(querysql)
        result = cur.fetchall()

        for res in result:
            floor = Floor(res) 
            floorList.append(floor)

        conn.commit()
        cur.close()
        conn.close()
        
        self.render("content.html",
                    floorList=floorList,
                    title=scan[3],
                    ans_num=scan[1],
                    view_num=scan[2],
                    name=name,
                    login=login,
                    number_of_article = num,
                   )
        
    def post(self):
        url = self.request.uri
        url = url[1:]
        art_id = int(url)
        
        fid = self.get_argument("fid")
        fid = int(fid)
        # database
        conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,
                             user=sae.const.MYSQL_USER,
                             passwd=sae.const.MYSQL_PASS,
                             db=sae.const.MYSQL_DB,
                             port=int(sae.const.MYSQL_PORT),
                             charset='utf8')
        cur = conn.cursor()
        conn.select_db('app_forum423423')

        querysql = "SELECT * FROM Article%d WHERE floor_id=%d" %(art_id, fid)
        cur.execute(querysql)
        
        result = cur.fetchone()
        vote = result[1]
            
        querysql = "Update Article%d SET num_vote=%d WHERE floor_id=%d" %(art_id, vote + 1, fid)
        cur.execute(querysql)
        
        conn.commit()
        cur.close()
        conn.close()
        self.get()
        #self.finish('-1')