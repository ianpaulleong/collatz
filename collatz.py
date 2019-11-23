# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:27:31 2019

@author: GAMEZ
"""

def collatz(theNum):
    curNum = theNum
    numList = list([curNum])
    while curNum > 1:
        if curNum%2 == 1:
            curNum = int(curNum*3 + 1)
        else:
            curNum = int(curNum/2)
        numList.append(curNum)
    return numList