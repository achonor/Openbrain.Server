#!usr/bin/env python
#coding=utf-8

#保存公共数据
import functions
from Server.GameServer import GameServer
from Server.GameSQL import GameSQL
from Server.GameMatch import GameMatch
from Server.GameProtocolFactory import GameProtocolFactory
from Render.PlayDataConfig import PlayDataConfig

#包头长度
global LENGTH_HEAD
LENGTH_HEAD = 4

#全局的连接工厂
global gameFactory
#全局服务类
global gameServer
#全局数据库
global gameSQL
#全局匹配控制类
global gameMatch
#配置文件
global playDataConfig

def InitGameData():
    global gameFactory
    global gameServer
    global gameSQL
    global gameMatch
    global playDataConfig

    gameFactory = GameProtocolFactory()
    gameServer = GameServer()
    gameSQL = GameSQL()
    gameMatch = GameMatch()

    #加载配置文件
    playDataConfig = PlayDataConfig()