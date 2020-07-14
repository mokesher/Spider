#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql
import traceback

class Sql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root",
                                    database="spider", charset="utf8")
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def insert(self, *args):
        try:
            result = self.cursor.execute("SELECT content from ac_moke WHERE content=%s;", [args[2]])
            if not result:
                self.cursor.execute("insert into ac_moke(title,page,content,url,date)"
                                    " values(%s,%s,%s,%s,%s)", [*args])
                self.db.commit()
        except:
            print(traceback.format_exc())

    def close(self):
        self.cursor.close()
        self.db.close()