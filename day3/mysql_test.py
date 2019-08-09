#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

####封装数据库########################
class DB(object):
    def __init__(self):
        #连接数据库
        self.conn = pymysql.connect(
            host="115.28.108.130",
            user="test",
            password="123456",
            charset = 'utf8',
            port = 3306,
            db='api_test'
        )
        self.cursor = self.conn.cursor()         ###吧游标绑定给self（实例对象）

    def execute(self,sql):            ######给一个sql执行，并返回查询结果
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # def close(self):
    #     self.conn.colse()
