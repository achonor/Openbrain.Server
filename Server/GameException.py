#!usr/bin/env python3
#coding=utf-8

#游戏异常类

class GameException(Exception):
    def __init__(self, _error_code, _message):
        self.message = _message
        self.error_code = _error_code

        print(self)

    def __str__(self):
        return "GameException: " + self.message + "Code: " + self.error_code