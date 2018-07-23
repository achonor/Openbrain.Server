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

#单局游戏时间
ONE_INNINGS_TIME = 20

#当前游戏玩法
PLAY_NUMBER = [0, 1, 2]

TAG = "GameReferee: "

class InningsData:
    def __init__(self, player1, player2):
        #本局游戏开始时间
        self.start_time = functions.getSystemTime() + READY_STAY_TIME
        #客户端展示随机玩法
        self.rand_play = random.sample(PLAY_NUMBER, 3)
        #本局玩法
        self.play = random.choice(self.rand_play)
        #本局游戏结束时间
        self.end_time = self.start_time + ONE_INNINGS_TIME
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
        while(self.innings_idx < TOTAL_INNINGS):
            #局数
            self.innings_idx += 1
            self.innings_list.append(InningsData(self.players[0], self.players[1]))
            #等待游戏结束
            wait_end = Deferred()
            reactor.callLater(READY_STAY_TIME + ONE_INNINGS_TIME, wait_end.callback, 1)
            yield wait_end
            #推送本局游戏结束

        #游戏结束
    #更新分数
    def updateGrade(self, player, index, addValue):
        innings = self.innings_list[index]
        if (None == innings):
            raise GameException(cmd_pb2.ERROR_CODE.INNINGS_GAME_HAS_END)
        return innings.updateGrade(player, addValue)

    #获取当前局
    def getCurInnings(self):
        return self.innings_list[self.innings_idx - 1]

    #获取对手
    def getOpponent(self, player):
        if (player == self.players[0]):
            return self.players[1]
        return self.players[0]