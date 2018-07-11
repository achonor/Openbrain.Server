#!usr/bin/env python3
#coding=utf-8

#服务类

import GameData
import functools
import functions
from Server.GamePlayer import GamePlayer
from proto import cmd_pb2

class GameServer(object):
    def __init__(self):
        #玩家列表
        self.__playerDict = {}

    def readProto(func):
        @functools.wraps(func)
        def wrapper(self, linkProto, className, requestProto):
            proto = className()
            proto.ParseFromString(requestProto.message_data)
            print ('MessageName: ', proto.__class__)
            print (proto)
            return func(self, linkProto, proto)
        return wrapper

    #处理请求协议
    def requestServer(self, linkProto, requestProto):

        className = None
        requestFunc = None
        messageName = requestProto.message_name
        if ('req_message_login_game' == messageName):
            className = cmd_pb2.req_message_login_game
            requestFunc= self.requestLogin
        if(None == 1):
            return

        #处理数据
        rProto = requestFunc(linkProto, className, requestProto)
        #发送数据
        GameData.gameFactory.returnData(linkProto, requestProto.message_ID, rProto)

    #登陆请求
    @readProto
    def requestLogin(self, linkProto, proto):
        rProto = cmd_pb2.rep_message_login_game()
        #创建Player
        player = GamePlayer.CreatePlayer(linkProto, proto.user_ID, proto.user_name, proto.user_icon)
        #玩家信息
        player.SetPlayerInfoToProto(rProto.player_info)
        #保存一下
        self.addPlayer(player)
        return rProto

    #获取玩家
    def getPlayer(self, userID):
        return self.__playerDict.get(userID)
    #添加玩家
    def addPlayer(self, cPlayer):
        self.__playerDict[cPlayer.userID] = cPlayer