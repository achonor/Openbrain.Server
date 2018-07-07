#!usr/bin/env python
#coding=utf-8

import GameData
import functions
from proto import cmd_pb2
from Server.GameProtocol import GameProtocol
from twisted.internet.protocol import  ServerFactory

class GameProtocolFactory(ServerFactory):
    protocol = GameProtocol
    def __init__(self):
        #为连接分配唯一ID
        self.connectIDIdx = 1
        #保存所有链接
        self.protoList = {}

    def buildProtocol(self, addr):
        tmpProto = ServerFactory.buildProtocol(self, addr)
        #分配ID
        tmpProto.connectID = self.connectIDIdx
        self.connectIDIdx += 1
        #保存连接
        self.protoList[tmpProto.connectID] = tmpProto
        return tmpProto

    def dataReceived(self, linkProto, data):
        #解析协议
        rootProto = cmd_pb2.root_proto()
        rootProto.ParseFromString(data)
        rootProto.connect_ID = linkProto.connectID
        #交给服务类处理
        GameData.gameFactory.requestServer(linkProto, rootProto)

    #返回数据给客户端
    def returnData(self, linkProto, messageID, proto):
        #序列化协议
        rspData = functions.serialization(proto, linkProto.connectID, messageID)
        #发送数据
        linkProto.sendData(rspData)

    def connectionLost(self, connectID):
        #移除
        self.removePlayer(connectID)

    def removePlayer(self, connectID):
        #移除连接
        self.protoList.pop(connectID)
        #移除玩家
        #GameData.My_Server.removePlayer(connectID)