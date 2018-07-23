#!usr/bin/env python3
#coding=utf-8

#开始游戏匹配

import math
import functions
import GameData

#容差值，相差多少的玩家可以匹配到一起
ToleranceValue = 100


TAG = "GameMatch: "
class MatchData:
    def __init__(self, _player):
        self.player = _player
        #开始匹配的时间
        self.startTime = functions.getSystemTime()

    def __cmp__(self, other):
        return self.player.startTime < other.startTime

    def getValue(self):
        return self.player.ranking

    #匹配权值范围
    def getMatchRange(self):
        curTime = functions.getSystemTime()
        offset = ToleranceValue + (curTime - self.startTime)
        return [self.player.ranking - offset, self.player.ranking + offset]

class GameMatch:
    def __init__(self):
        #匹配队列(非队列)
        self.matchQueue = {}
        #定时匹配
        from twisted.internet import task
        loopMatch = task.LoopingCall(self.match)
        loopMatch.start(0.5)

    def addMatch(self, player):
        matchData = MatchData(player)
        self.matchQueue[player] = matchData

    def removeMatch(self, player):
        self.matchQueue.pop(player, None)

    def match(self):
        try:
            #匹配成功的玩家dict
            successList = {}
            for key1, match1 in self.matchQueue.items():
                if (None != successList.get(match1)):
                    #已经匹配过的数据
                    continue
                range = match1.getMatchRange()
                #寻找排名最接近的玩家
                nearData = None
                for key2, match2 in self.matchQueue.items():
                    if (match1 == match2 or None != successList.get(match2)):
                        continue
                    if ((range[0] <= match2.getValue() and match2.getValue() <= range[1]) and (None == nearData or math.fabs(match1.getValue() - match2.getValue()) < math.fabs(match1.getValue() - nearData.getValue()))):
                        nearData = match2
                if (None != nearData):
                    #匹配成功
                    successList[match1] = nearData
                    successList[nearData] = match1
            #处理匹配成功数据
            for key, values in successList.items():
                #从队列移除
                if ("D532B5446BA9E5AC90AB5138D1BD19BC" != key.player.userID):
                    self.removeMatch(key.player)
                #推送匹配成功
                GameData.gameServer.sendMatchSuccess(key.player, values.player)
        except Exception as e:
            print(TAG, "Error: ", e)