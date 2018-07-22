#!usr/bin/env python3
#coding=utf-8

#服务类

import GameData
import functools
import functions
from Server.GamePlayer import GamePlayer
from proto import cmd_pb2

TAG = "GameServer: "
class GameServer(object):

    def __init__(self):
        #玩家列表
        self.__playerDict = {}
        #connectID和userID的字典
        self.__connectIDToUserID = {}

    def readProto(func):
        @functools.wraps(func)
        def wrapper(self, player, linkProto, className, requestProto, callback):
            try:
                proto = className()
                proto.ParseFromString(requestProto.message_data)
                print (TAG, proto.__class__)
                print (TAG, proto)
                return func(self, player, linkProto, proto, callback)
            except Exception as e:
                print(TAG, "Eroor: ", e)
        return wrapper

    #处理请求协议
    def requestServer(self, linkProto, requestProto):

        className = None
        requestFunc = None
        requestPlayer = None
        messageName = requestProto.message_name
        if ("req_message_login_game" == messageName):
            className = cmd_pb2.req_message_login_game
            requestFunc= self.requestLogin
        elif ("req_message_start_match" == messageName):
            className = cmd_pb2.req_message_start_match
            requestFunc = self.requestMatch
            requestPlayer = self.getPlayerByLink(linkProto)
        if(None == requestFunc):
            print(TAG, "Error", "not found handle function")
            return
        def _sendData(rProto):
            #发送数据
            GameData.gameFactory.returnData(linkProto, requestProto.message_ID, rProto)
        #处理数据
        requestFunc(requestPlayer, linkProto, className, requestProto, _sendData)
    #登陆请求
    @readProto
    def requestLogin(self, player, linkProto, proto, callback):
        def _requestLogin(newPlayer):
            rProto = cmd_pb2.rep_message_login_game()
            #玩家信息
            newPlayer.SetPlayerInfoToProto(rProto.player_info)
            #保存一下
            self.addPlayer(newPlayer)
            callback(rProto)
        #创建Player
        GamePlayer.CreatePlayer(linkProto, proto.user_ID, proto.user_name, proto.user_icon, _requestLogin)

    #匹配请求
    @readProto
    def requestMatch(self, player, linkProto, proto, callback):
        GameData.gameMatch.addMatch(player)
        rProto = cmd_pb2.rep_message_start_match()
        callback(rProto)


    #推送玩家信息
    def sendPlayerInfo(self, player):
        rProto = cmd_pb2.rep_message_player_info()
        #设置玩家信息
        player.SetPlayerInfoToProto(rProto.player_info)
        #推送协议
        GameData.gameFactory.returnData(player.linkProto, 0, rProto)

    #推送匹配成功
    def sendMatchSuccess(self, player, otherPlayer):
        rProto = cmd_pb2.rep_message_match_success()
        otherPlayer.SetPlayerInfoToProto(rProto.player_info)
        #推送协议
        GameData.gameFactory.returnData(player.linkProto, 0, rProto)

    #获取玩家
    def getPlayer(self, userID):
        return self.__playerDict.get(userID)

    def getPlayerByLink(self, linkProto):
        userID = self.__connectIDToUserID[linkProto.connectID]
        if (None != userID):
            return self.__playerDict[userID]
        return None
    #添加玩家
    def addPlayer(self, cPlayer):
        self.__playerDict[cPlayer.userID] = cPlayer
        self.__connectIDToUserID[cPlayer.linkProto.connectID] = cPlayer.userID
    def removePlayer(self, connectID):
        userID  = self.__connectIDToUserID.get(connectID)
        if (None == userID):
            #还未登陆
            return
        self.__connectIDToUserID.pop(connectID)
        player = self.__playerDict.pop(userID)
        #从匹配队列中删除
        GameData.gameMatch.removeMatch(player)