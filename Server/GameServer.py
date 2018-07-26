#!usr/bin/env python3
#coding=utf-8

#服务类

import GameData
import functools
import functions
from Server.GamePlayer import GamePlayer
from Server.GameReferee import GameReferee
from Server.GameException import GameException
from proto import cmd_pb2

TAG = "GameServer: "
class GameServer(object):

    def __init__(self):
        #玩家列表
        self.__playerDict = {}
        #connectID和userID的字典
        self.__connectIDToUserID = {}
        #裁判dict
        self.__refereeDict = {}

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
        requestPlayer = self.getPlayerByLink(linkProto)
        messageName = requestProto.message_name
        if ("req_message_login_game" == messageName):
            className = cmd_pb2.req_message_login_game
            requestFunc= self.requestLogin
        elif ("req_message_start_match" == messageName):
            className = cmd_pb2.req_message_start_match
            requestFunc = self.requestMatch
        elif ("req_message_start_ready" == messageName):
            className = cmd_pb2.req_message_start_ready
            requestFunc = self.requestReady
        elif ("req_message_start_game" == messageName):
            className = cmd_pb2.req_message_start_game
            requestFunc = self.requestStartGame
        elif ("req_message_updata_grade" == messageName):
            className = cmd_pb2.req_message_updata_grade
            requestFunc = self.requestUpdateGrade
        if(None == requestFunc):
            print(TAG, "Error: ", "not found handle function")
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
        try:
            rProto = cmd_pb2.rep_message_start_match()
            if (None != self.__refereeDict.get(player)):
                # 已经在游戏中了
                raise GameException(cmd_pb2.ERROR_CODE.HAS_REFEREE)
            else:
                GameData.gameMatch.addMatch(player)
        except GameException as e:
            rProto.isOK = e.error_code

        callback(rProto)

    #游戏准备请求
    @readProto
    def requestReady(self, player, linkProto, proto, callback):
        try:
            rProto = cmd_pb2.rep_message_start_ready()
            # 获取裁判
            referee = self.__refereeDict.get(player)
            #获取当前局
            innings = referee.getCurInnings()
            if (None == innings):
                raise GameException(cmd_pb2.ERROR_CODE.GAME_NOT_START)
            #获取对手
            opponent = referee.getOpponent(player)
            #设置返回信息
            rProto.innings = referee.innings_idx
            rProto.start_time = innings.start_time
            opponent.SetPlayerInfoToProto(rProto.player_info)
            functions.listToRepeated(innings.rand_play_id, rProto.rand_play_id)
            rProto.play_id = innings.play_id
        except GameException as e:
            rProto.isOK = e.error_code

        callback(rProto)

    #请求开始游戏
    @readProto
    def requestStartGame(self, player, linkProto, proto, callback):
        try:
            rProto = cmd_pb2.rep_message_start_game()
            # 获取裁判
            referee = self.__refereeDict.get(player)
            #获取对手
            opponent = referee.getOpponent(player)
            #获取当前局
            innings = referee.getCurInnings()
            #设置返回信息
            rProto.end_time = innings.end_time
            rProto.play_id = innings.play_id
            rProto.intro_end_time = innings.intro_end_time
            opponent.SetPlayerInfoToProto(rProto.player_info)
        except GameException as e:
            rProto.isOK = e.error_code

        callback(rProto)

    #请求更新分数
    @readProto
    def requestUpdateGrade(self, player, linkProto, proto, callback):
        try:
            rProto = cmd_pb2.rep_message_updata_grade()
            #获取裁判
            referee = self.__refereeDict.get(player)
            rProto.grade = referee.updateGrade(player, proto.innings, proto.add_value)
            #获取对手
            opponent = referee.getOpponent(player)
            #给玩家对手推送分数
            tmpProto = cmd_pb2.rep_message_updata_opponent_grade()
            tmpProto.grade = rProto.grade
            GameData.gameFactory.returnData(opponent.linkProto, 0, tmpProto)
        except GameException as e:
            rProto.isOK = e.error_code

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
        try:
            rProto = cmd_pb2.rep_message_match_success()
            otherPlayer.SetPlayerInfoToProto(rProto.player_info)
            #推送协议
            GameData.gameFactory.returnData(player.linkProto, 0, rProto)
            #添加裁判
            if (None == self.__refereeDict.get(player) and None == self.__refereeDict.get(otherPlayer)):
                referee = GameReferee(player, otherPlayer)
                self.__refereeDict[player] = referee
                self.__refereeDict[otherPlayer] = referee
            elif(self.__refereeDict.get(player) != self.__refereeDict.get(otherPlayer)):
                print(TAG, "Error: player different referee")
        except Exception as e:
            print(TAG, e)
    #推送局结束
    def sendInningsEnd(self, player1, player2, rProto):
        # 推送协议
        GameData.gameFactory.returnData(player1.linkProto, 0, rProto)
        GameData.gameFactory.returnData(player2.linkProto, 0, rProto)
    #推送游戏结束
    def sendGameEnd(self, player1, player2, rProto1, rProto2):
        #删除裁判
        self.__refereeDict.pop(player1, None)
        self.__refereeDict.pop(player2, None)
        # 推送协议
        GameData.gameFactory.returnData(player1.linkProto, 0, rProto1)
        GameData.gameFactory.returnData(player2.linkProto, 0, rProto2)

    #获取玩家
    def getPlayer(self, userID):
        return self.__playerDict.get(userID)

    def getPlayerByLink(self, linkProto):
        userID = self.__connectIDToUserID.get(linkProto.connectID)
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