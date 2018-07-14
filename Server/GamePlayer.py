#!usr/bin/env python3
#coding=utf-8


import GameData
from proto import cmd_pb2

'''玩家的信息'''

class GamePlayer(object):
    def __init__(self, linkProto, userID, userName, userIcon):
        #玩家的链接
        self.__linkProto = linkProto
        #ID
        self.userID = userID
        #用户昵称
        self.userName = userName
        # icon url
        self.userIcon = userIcon
        #体力
        self.energy = 0
        #钻石数量
        self.gems = 0
        #等级
        self.level = 0
        #熟练度
        self.proficiency = 0
    #玩家注册初始化
    def InitPlayer(self):
        self.energy = 15
        self.gems = 0
        self.level = 1
        self.proficiency = 1

        pass
    @staticmethod
    def CreatePlayer(linkProto, userID, userName, userIcon, callback):
        #查询数据库是否有用户
        def _CreatePlayer(cursor, param):
            # 查数据库，是否是第一次登陆
            GameData.gameSQL.QueryBySqlFile(cursor, "select_user", [userID])
            player = None
            ret = cursor.fetchall()
            if (None != ret and 0 < len(ret)):
                GameData.gameSQL.QueryBySqlFile(cursor, "update_user_name_icon_by_id", [userName, userIcon, userID])
                player = GamePlayer(linkProto, userID, userName, userIcon)
            else:
                player = GamePlayer(linkProto, userID, userName, userIcon)
                player.InitPlayer()
                # 写入user表
                GameData.gameSQL.QueryBySqlFile(cursor, "insert_user", [player.userID, player.userName, player.userIcon,
                                                                player.energy, player.gems,  player.level, player.proficiency])

            # 从数据库获取玩家数据
            GameData.gameSQL.QueryBySqlFile(cursor, "select_user", [userID])
            ret = cursor.fetchall()
            player.UpdatePlayerDataByDBResult(ret)
            # 同步一次玩家数据
            player.SendPlayerInfo()
            return player
        GameData.gameSQL.QueryByInteraction(_CreatePlayer, None, callback)



    def SendPlayerInfo(self):
        rProto = cmd_pb2.rep_message_player_info()
        #设置玩家信息
        self.SetPlayerInfoToProto(rProto.player_info)
        #推送协议
        GameData.gameFactory.returnData(self.linkProto, 0, rProto)

    def SetPlayerInfoToProto(self, proto):
        proto.user_name = self.userName
        proto.user_icon = self.userIcon
        proto.energy = self.energy
        proto.gems = self.gems
        proto.level = self.level
        proto.proficiency = self.proficiency

    #提交玩家数据到数据库
    def UpdateToDB(self):
        #写入user表
        GameData.gameSQL.UpdateBySqlFile("update_user_all_by_id",
                                         [self.userName, self.userIcon, self.energy,
                                          self.gems, self.level, self.proficiency, self.userID])

    #同步数据库数据
    def UpdatePlayerDataByDBResult(self, ret):
        self.userName = ret[0][1]
        self.userIcon = ret[0][2]
        self.energy = ret[0][3]
        self.gems = ret[0][4]
        self.level = ret[0][5]
        self.proficiency = ret[0][6]

    def __del__(self):
        self.level = 2
        self.UpdateToDB();

    @property
    def linkProto(self):
        return self.__linkProto
    @linkProto.setter
    def linkProto(self, value):
        self.__linkProto = value