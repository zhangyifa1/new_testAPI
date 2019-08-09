#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

####数据库基础封装########################

#连接数据库
db_config = {
    'host': '115.28.108.130',
    'db': 'longtengserver',
    'user': 'test',
    'password': '123456',
    'charset': 'utf8',
    'autocommit':True
}

class DB(object):
    def __init__(self):
        print("建立数据库链接")
        self.conn = pymysql.connect(**db_config)
        self.cursor = self.conn.cursor()    ########建立游标

    def execute(self,sql):
        print("执行sql:{sql}".format(sql = sql))             ###format
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print ("查询结果：{result}".format(result = result))     ###format
        return result

    # def close(self):           不会自动关闭数据库，需要手动调用
    #     self.conn.close()
    def __del__(self):           ###自动关闭数据库，无需手动调用
        self.conn.close()

#####模块私有代码############
if __name__=='__main__':        ########一般用来调试当前代码，此处用于调试mysql数据的调试
    db = DB()
    r = db.execute('select * from cardInfo where cardNumber ="123456"')
    print(r)
    db.close()

class longtengserver(DB):
    ##该项目数据库常用业务#########
    def del_card(self,card_number):
        print("删除加油卡:{card_number}")
        sql = 'delete from cardinfo where cardNumber = "{card_number}.format(card_number=card_number)"'    ####format
        self.execute(sql)

    def check_card(self,card_number):
        print ("检查数据库加油卡：{card_number}".format(card_number=card_number))           ######format
        sql ='select * from cardinfo where cardNumber = "123456" '     ######新式语法，不会出错
        self.execute(sql)
        result = self.execute(sql)
        #print (result)
        if result != ():
            return True
        else:
            return False
