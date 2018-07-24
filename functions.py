#!usr/bin/env python
#coding=utf-8
import time
import copy
import random
import functools
from proto import cmd_pb2

TIMEOFFSET = 0

#输出函数运行时间
def runtime(func):
    @functools.wraps(func)
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print("uesd time:", end - start)
    return wrapper

#单例修饰词
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def getInstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getInstance


#获取系统时间
def getSystemTime():
    #protobuf抽风，太大的数字序列化会报错，和客户端约定减少特定的值
    return time.time() - TIMEOFFSET

#int转化成char
def intToBytes(num):
    array = []
    for i in range(3, -1, -1):
        tmpInt = ((255 << (8 * i))) & num
        array.append(tmpInt)
    return bytes(array)
#char转化成int
def bytesToInt(str):
    ret = 0
    for i in range(0, 4, 1):
        ret = (ret << 8) | str[i]
    return ret
#封装协议
def serialization(proto, connectID = 0, messageID = 0):
    rootProto = cmd_pb2.root_proto()
    rootProto.connect_ID  = connectID
    rootProto.message_ID = messageID
    rootProto.message_name = proto.__class__.__name__
    rootProto.server_time = getSystemTime()
    try:
        rootProto.message_data = proto.SerializeToString()
    except Exception as e:
        print(e)
        print(rootProto)
    #序列化包装后的协议
    tmpStr = rootProto.SerializeToString()
    tmpLen = len(tmpStr)
    tmpStr = intToBytes(tmpLen) + tmpStr
    return tmpStr

def listToRepeated(src_list, des_repeate):
    for var in src_list:
        des_repeate.append(var)