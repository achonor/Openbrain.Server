#!usr/bin/env python
#coding=utf-8

#保存公共数据
import functions
from Server.GameServer import GameServer
from Server.GameSQL import GameSQL
from Server.GameProtocolFactory import GameProtocolFactory

#包头长度
global LENGTH_HEAD
LENGTH_HEAD = 4

#全局的连接工厂
global gameFactory
#全局服务类
global gameServer
#全局数据库
global gameSQL

def InitGameData():
    global gameFactory
    global gameServer
    global gameSQL

    gameFactory = GameProtocolFactory()
    gameServer = GameServer()
    gameSQL = GameSQL()
