#!usr/bin/env python3
#coding=utf-8

import pymysql
import functools
import os


class GameSQL(object):
    def linkMySql(func):
        @functools.wraps(func)
        def wrapper(self, order, param):
            # 打开数据库连接
            db = pymysql.connect("localhost", "root", "Lull0618", "openbrain")
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            ret = None
            try:
                ret = func(self, order, db, cursor, param)
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

    @linkMySql
    def selectSQL(self, order, db, cursor):
        ret = cursor.execute(order)
        # 提交到数据库执行
        db.commit()
        return ret

    @linkMySql
    def SelectBySqlFile(self, order, db, cursor):
        filePath = os.path.join("../sql/select", order + ".sql")
        with open(filePath, 'r') as file:
            #print(file.read())
            cursor.execute(file.read())
            # 提交到数据库执行
            db.commit()
            #获取数据
            data = cursor.fetchall()
            #print(data)
            return data
    @linkMySql
    def InsertBySqlFile(self, order, db, cursor, param):
        filePath = os.path.join("../sql/select", order + ".sql")
        with open(filePath, 'r') as file:
            cursor.execute(file.read(), param)
            # 提交到数据库执行
            db.commit()

    @linkMySql
    def UpdateBySqlFile(self, order, db, cursor, param):
        filePath = os.path.join("../sql/select", order + ".sql")
        with open(filePath, 'r') as file:
            cursor.execute(file.read(), param)
            # 提交到数据库执行
            db.commit()