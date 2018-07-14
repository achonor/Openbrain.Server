#!usr/bin/env python3
#coding=utf-8

import pymysql
import functools
import os
from twisted.enterprise import adbapi

class GameSQL(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("MySQLdb", db = "openbrain", user = 'root', passwd = 'Lull0618', host = '127.0.0.1',
                                            use_unicode = True, charset = 'utf8')
    #同步连接
    def linkMySql(func):
        @functools.wraps(func)
        def wrapper(self, order, param):
            # 打开数据库连接
            db = pymysql.connect("localhost", "root", "Lull0618", "openbrain")
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            ret = None
            filePath = os.path.join("../sql/select", order + ".sql")
            with open(filePath, 'r') as file:
                try:
                    ret = func(self, file.read(), db, cursor, param)
                except Exception as e:
                    print(e)
                    # 发生错误时回滚
                    db.rollback()
                finally:
                    cursor.close()
                    # 关闭数据库连接
                    db.close()
            return ret
        return wrapper

    def readFile(func):
        @functools.wraps(func)
        def wrapper(self, cursor, order, param):
            filePath = os.path.join("../sql/select", order + ".sql")
            with open(filePath, 'r') as file:
                query = func(self, cursor, file.read(), param)
            return query
        return wrapper

    def QueryByInteraction(self, interaction, param = None, callback = None):
        query = self.dbpool.runInteraction(interaction, param)
        #错误回调
        query.addErrback(self.onError)
        #回调
        query.addCallback(self.printResult)
        query.addCallback(callback)
        return query

    #异步执行单条命令
    @readFile
    def QueryBySqlFile(self, cursor, order, param):
        return cursor.execute(order, param)

    #同步执行Select
    @linkMySql
    def SelectBySqlFile(self, order, db, cursor, param):
            cursor.execute(order, param)
            #获取数据
            data = cursor.fetchall()
            return data
    @linkMySql
    def InsertBySqlFile(self, order, db, cursor, param):
        cursor.execute(order, param)
        # 提交到数据库执行
        db.commit()

    @linkMySql
    def UpdateBySqlFile(self, order, db, cursor, param):
            cursor.execute(order, param)
            # 提交到数据库
            db.commit()

    #打印错误
    def onError(self, error):
        print("_GameSQL.onError error = ", error)
    #查询结果打印
    def printResult(self, result):
        print("GameSQL.printResult result = ", result)
        return result