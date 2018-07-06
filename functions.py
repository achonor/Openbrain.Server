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

#获取系统时间
def getSystemTime():
    #protobuf抽风，太大的数字序列化会报错，和客户端约定减少特定的值
    return time.time() - TIMEOFFSET

#int转化成char
def intToChar(num):
    ret = ''
    for i in range(3, -1, -1):
        tmpInt = ((255 << (8 * i))) & num
        ret = ret + chr(tmpInt)
    return ret
#char转化成int
def charToInt(str):
    ret = 0
    for i in range(0, 4, 1):
        ret = (ret << 8) | ord(str[i])
    return ret
#封装协议
def serialization(proto, playerID = 0, messageID = 0):
    mainProto = cmd_pb2.MainProto()
    mainProto.playerID  = playerID
    mainProto.messageID = messageID
    mainProto.messageName = proto.__class__.__name__
    mainProto.serverTime = getSystemTime()
    try:
        mainProto.messageData = proto.SerializeToString()
    except Exception as e:
        print(e)
        print(mainProto)
    #序列化包装后的协议
    tmpStr = mainProto.SerializeToString()
    tmpLen = len(tmpStr)
    tmpStr = intToChar(tmpLen) + tmpStr
    return tmpStr