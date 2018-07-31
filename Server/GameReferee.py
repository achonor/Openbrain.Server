#!usr/bin/env python3
#coding=utf-8

#游戏裁判

import random
import functions
import GameData
from Server.GameException import GameException
from proto import cmd_pb2

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks, Deferred



#游戏局数
TOTAL_INNINGS = 3

#开始准备时间
READY_STAY_TIME = 5

#当前游戏玩法
PLAY_NUMBER = [0, 1, 2]

TAG = "GameReferee: "

class InningsData:
    def __init__(self, player1, player2):
        #本局游戏开始时间
        self.start_time = functions.getSystemTime() + READY_STAY_TIME
        #客户端展示随机玩法
        self.rand_play_id = random.sample(GameData.playDataConfig.getAllPlayID(), 3)
        #本局玩法
        self.play_id = random.choice([0, 2])#(self.rand_play_id)
        #玩法配置
        self.play_data = GameData.playDataConfig.getDataByID(self.play_id)
        #介绍结束时间
        self.intro_end_time = self.start_time + self.play_data.intro_time
        #本局游戏结束时间
        self.end_time = self.intro_end_time + self.play_data.time
        #分数
        self.grade = {}
        self.grade[player1] = 0
        self.grade[player2] = 0

    #更新分数
    def updateGrade(self, player, addValue):
        if (None == self.grade.get(player)):
            raise GameException(cmd_pb2.ERROR_CODE.OPPONENT_NOT_FOUND)
        self.grade[player] += addValue
        if (self.grade[player] < 0):
            self.grade[player] = 0
        return self.grade[player]

class GameReferee:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        #当前是第几局
        self.innings_idx = 0
        #局列表
        self.innings_list = []

        #稍后开始
        reactor.callLater(0.2, self.gameLoop)

    @inlineCallbacks
    def gameLoop(self):
        try:
            while(self.innings_idx < TOTAL_INNINGS):
                cur_innings = InningsData(self.players[0], self.players[1])
                self.innings_list.append(cur_innings)
                #等待游戏结束
                wait_end = Deferred()
                print("cur_innings.start_time = ", cur_innings.start_time)
                print("cur_innings.end_time = ", cur_innings.end_time, "functions.getSystemTime() = ", functions.getSystemTime())
                reactor.callLater(cur_innings.end_time - functions.getSystemTime(), wait_end.callback, 1)
                yield wait_end
                # 局数+1
                self.innings_idx += 1
                #推送本局游戏结束
                rProto = cmd_pb2.rep_message_innings_end()
                rProto.has_innings = (self.innings_idx < TOTAL_INNINGS)
                GameData.gameServer.sendInningsEnd(self.players[0], self.players[1], rProto)
            #游戏结束
            rProtos = []
            for idx in range(len(self.players)):
                player = self.players[idx]
                opponent = self.getOpponent(player)
                rProto = cmd_pb2.rep_message_game_end()
                #每局的玩法，分数
                for innings in self.innings_list:
                    rProto.play_list.append(innings.play_id)
                    rProto.left_grade.append(innings.grade[player])
                    rProto.right_grade.append(innings.grade[opponent])
                    #更新玩家属性
                    attr_offset = player.updateAttributeByGrade(innings.play_id, innings.grade[player])
                    for idx in range(len(attr_offset)):
                        if (idx < len(rProto.attribute_offset)):
                            rProto.attribute_offset[idx] += attr_offset[idx]
                        else:
                            rProto.attribute_offset.append(attr_offset[idx])
                rProtos.append(rProto)
            #对手信息
            for idx in range(len(self.players)):
                rProto = rProtos[idx]
                player = self.players[idx]
                opponent = self.getOpponent(player)
                #对手信息
                opponent.SetPlayerInfoToProto(rProto.player_info)
            GameData.gameServer.sendGameEnd(self.players[0], self.players[1], rProtos[0], rProtos[1])
        except Exception as e:
            print(TAG, "Error: ", e)
    #更新分数
    def updateGrade(self, player, index, addValue):
        innings = self.innings_list[index]
        if (None == innings):
            raise GameException(cmd_pb2.ERROR_CODE.INNINGS_GAME_HAS_END)
        return innings.updateGrade(player, addValue)

    #获取当前局
    def getCurInnings(self):
        return self.innings_list[self.innings_idx]

    #获取对手
    def getOpponent(self, player):
        if (player == self.players[0]):
            return self.players[1]
        return self.players[0]

