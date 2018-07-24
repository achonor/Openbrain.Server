#!usr/bin/env python3
#coding=utf-8

from Render.DataReader import DataReader
import functions
from proto.xls2proto import play_data_pb2

@functions.singleton
class PlayDataConfig(DataReader):
    def __init__(self, *args, **kw):
        self.__srcData = None
        self.__dataDict = {}

    def loadConfig(self):
        #加载数据
        with open(self.getDataConfigPath(), 'rb') as file:
            file_data = file.read()
            #反序列化
            self.__srcData = play_data_pb2.play_data_ARRAY()
            self.__srcData.ParseFromString(file_data)
            print("play_data: ")
            print(self.__srcData)
            for data in self.__srcData.items:
                self.__dataDict[data.id] = data

    def getDataByID(self, id):
        return self.__dataDict.get(id, None)

    def getAllData(self):
        return self.__dataDict

    def getDataConfigName(self):
        return "play_data.bin"