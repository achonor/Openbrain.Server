#!usr/bin/env python3
#coding=utf-8


import GameData
from proto import cmd_pb2


'''玩家的信息'''

class GamePlayer(object):
    def __init__(self, linkProto, userID, userName):
        #玩家的链接
        self.__linkProto = linkProto
        #ID
        self.userID = userID
        #用户昵称
        self.userName = userName
        #用户icon url
        self.userIcon = ""
    #玩家注册初始化
    def InitPlayer(self):
        #写入user表
        GameData.gameSQl.InsertBySqlFile("insert_user", [self.userID, self.userName])
        pass
    @staticmethod
    def CreatePlayer(linkProto, userID, userName):
        player = None
        #查询数据库是否有用户
        ret = GameData.gameSQl.SelectBySqlFile("select_user", [userID])
        if (0 < len(ret)):
            GameData.gameSQl.UpdateBySqlFile("update_user_name_by_id", [userName, userID])
            player = GamePlayer(linkProto, userID, userName)
        else:
            player = GamePlayer(linkProto, userID, userName)
            player.InitPlayer()
        #同步一次玩家数据
        if (None != player):
            player.SendPlayerInfo()
        return player

    def SendPlayerInfo(self):
        rProto = cmd_pb2.rep_message_player_info()
        #设置玩家信息
        self.SetPlayerInfoToProto(rProto.player_info)
        #推送协议
        GameData.gameFactory.returnData(self.linkProto, 0, rProto)

    def SetPlayerInfoToProto(self, proto):
        proto.user_ID = self.userID
        proto.user_name = self.userName
        proto.user_icon = self.userIcon

    @property
    def linkProto(self):
        return self.__linkProto
    @linkProto.setter
    def linkProto(self, value):
        self.__linkProto = value