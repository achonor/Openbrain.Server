#!usr/bin/env python3
#coding=utf-8

import atexit
import GameData
import functions
from proto import cmd_pb2

'''玩家的信息'''

class GamePlayer(object):
    def __init__(self, linkProto, userID, userName, userIcon):
        #是否是AI
        self.isAI = False
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
        #速度
        self.speed = 0
        #判断力
        self.judgment = 0
        #计算力
        self.calculate = 0
        #精确度
        self.accuracy = 0
        #观察力
        self.observation = 0
        #记忆力
        self.memory = 0
        #排名
        self.ranking = 0
        #分数
        self.grade = 0

    def __getitem__(self, key):
        if (0 == key):
            return self.speed
        elif (1 == key):
            return self.judgment
        elif (2 == key):
            return self.calculate
        elif (3 == key):
            return self.accuracy
        elif (4 == key):
            return self.observation
        elif (5 == key):
            return self.memory
    def __setitem__(self, key, value):
        if (0 == key):
            self.speed = value
        elif (1 == key):
            self.judgment = value
        elif (2 == key):
            self.calculate = value
        elif (3 == key):
            self.accuracy = value
        elif (4 == key):
            self.observation = value
        elif (5 == key):
            self.memory = value

    @staticmethod
    def createAI():
        rand_player_data = GameData.gameSQL.SelectBySqlFile("rand_user", None)
        ai_player = GamePlayer(None, rand_player_data[0][1], rand_player_data[0][2], rand_player_data[0][3])
        ai_player.isAI = True
        ai_player.UpdatePlayerDataByDBResult(rand_player_data)
        return ai_player

    #玩家注册初始化
    def InitPlayer(self):
        self.energy = 15
        self.gems = 0
        self.level = 1
        self.proficiency = 1
        self.speed = 10
        self.judgment = 10
        self.calculate = 10
        self.accuracy = 10
        self.observation = 10
        self.memory = 10
        self.ranking = 2147483647
        self.grade = 10

    @staticmethod
    def CreatePlayer(linkProto, userID, userName, userIcon, callback):
        #查询数据库是否有用户
        def _CreatePlayer(cursor, param):
            # 查数据库，是否是第一次登陆
            GameData.gameSQL.QueryBySqlFile(cursor, "select_user", [userID])
            player = None
            ret = cursor.fetchall()
            print(ret)
            if (None != ret and 0 < len(ret)):
                GameData.gameSQL.QueryBySqlFile(cursor, "update_user_name_icon_by_id", [userName, userIcon, userID])
                player = GamePlayer(linkProto, userID, userName, userIcon)
            else:
                player = GamePlayer(linkProto, userID, userName, userIcon)
                player.InitPlayer()
                # 写入user表
                GameData.gameSQL.QueryBySqlFile(cursor, "insert_user", [player.userID, player.userName, player.userIcon,
                                                                        player.energy, player.gems,  player.level, player.proficiency,
                                                                        player.speed, player.judgment, player.calculate, player.accuracy,
                                                                        player.observation, player.memory, player.ranking, player.grade])

            # 从数据库获取玩家数据
            GameData.gameSQL.QueryBySqlFile(cursor, "select_user", [userID])
            ret = cursor.fetchall()
            player.UpdatePlayerDataByDBResult(ret)
            # 同步一次玩家数据
            #GameData.gameServer.sendPlayerInfo(player)
            return player
        GameData.gameSQL.QueryByInteraction(_CreatePlayer, None, callback)


    def SetPlayerInfoToProto(self, proto):
        proto.user_name = self.userName
        proto.user_icon = self.userIcon
        proto.energy = self.energy
        proto.gems = self.gems
        proto.level = self.level
        proto.proficiency = self.proficiency
        proto.speed = self.speed
        proto.judgment = self.judgment
        proto.calculate = self.calculate
        proto.accuracy = self.accuracy
        proto.observation = self.observation
        proto.memory = self.memory
        proto.ranking = self.ranking
        proto.grade = self.grade

    #提交玩家数据到数据库
    @atexit.register
    def UpdateToDB(self):
        if (self.isAI):
            return
        #写入user表
        GameData.gameSQL.UpdateBySqlFile("update_user_all_by_id",
                                         [self.userName, self.userIcon, self.energy, self.gems, self.level, self.proficiency,
                                          self.speed, self.judgment, self.calculate, self.accuracy, self.observation, self.memory, self.ranking, self.grade, self.userID])

    #同步数据库数据
    def UpdatePlayerDataByDBResult(self, ret):
        if (self.isAI):
            return
        self.userName = ret[0][2]
        self.userIcon = ret[0][3]
        self.energy = ret[0][4]
        self.gems = ret[0][5]
        self.level = ret[0][6]
        self.proficiency = ret[0][7]
        self.speed = ret[0][8]
        self.judgment = ret[0][9]
        self.calculate = ret[0][10]
        self.accuracy = ret[0][11]
        self.observation = ret[0][12]
        self.memory = ret[0][13]
        self.ranking = ret[0][14]
        self.grade = ret[0][15]

    #通过游戏分数计算属性变化, 返回属性变化
    def updateAttributeByGrade(self, play_id, grade):
        ret_list = []
        #获取玩法数据
        play_data = GameData.playDataConfig.getDataByID(play_id)
        for idx in range(len(play_data.expect_grade_scale)):
            expect_grade = (play_data.expect_grade_scale[idx] * self[idx])
            new_attr = (grade - expect_grade) * play_data.attribute[idx] * 0.0001
            new_attr = functions.numberClamp(self[idx] + new_attr, 0, 100)
            ret_list.append(new_attr - self[idx])
            self[idx] = new_attr;
        return ret_list

    def __del__(self):
        self.UpdateToDB()
    @property
    def linkProto(self):
        return self.__linkProto
    @linkProto.setter
    def linkProto(self, value):
        self.__linkProto = value