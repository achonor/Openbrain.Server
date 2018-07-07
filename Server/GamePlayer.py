#!usr/bin/env python
#coding=utf-8


'''玩家的信息'''

class GamePlayer(object):
    def __init__(self, linkProto):
        #玩家的链接
        self.__linkProto = linkProto

    @property
    def linkProto(self):
        return self.__linkProto
    @linkProto.setter
    def linkProto(self, value):
        self.__linkProto = value