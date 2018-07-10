#!usr/bin/env python3
#coding=utf-

import sys
sys.path.append('..')

import time
import GameData
from proto import cmd_pb2
import functions
from Server.GameProtocolFactory import GameProtocolFactory
from twisted.application import internet, service

port = 8160


def main():
    #初始化公共数据
    GameData.InitGameData()

    from twisted.internet import reactor
    reactor.listenTCP(port, GameData.gameFactory)
    print("start!!!")
    reactor.run()
    print("end!!!")

if ("__main__" == __name__):
    main()
