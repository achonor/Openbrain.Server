#!usr/bin/env python3
#coding=utf-8

from abc import ABCMeta, abstractmethod

class DataReader:
    __metaclass__ = ABCMeta

    def getDataConfigPath(self):
        return "../DataConfig/" + self.getDataConfigName();

    @abstractmethod
    def getDataConfigName(self):pass

