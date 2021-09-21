# -*- coding:utf-8 -*-

'''
@author: eric
@file: stack_dec_to_bin.py
@time: 2021/8/13 17:57
'''

from dataStructures_and_algorithms.chapter3_stackApply.stack_01 import MyStack


#将十进制转换为2进制
def dec_to_bin(decNum):
    s = MyStack()

    while decNum > 0:
        s.pushItem(decNum % 2)      #将余数插入栈
        decNum = decNum // 2        #不断地除2，直到小于0

    binNum = ''
    while not s.isEmpty():
        binNum = binNum + str(s.popItem())      #不断拼接从栈中抛出的字符串
    return binNum

print(dec_to_bin(233))


#十进制转换为任意进制
def dec_to_any(decNum, base):
    s = MyStack()

    while decNum > 0:
        s.pushItem(decNum % base)      #将余数插入栈
        decNum = decNum // base        #不断地除2，直到小于0

    binNum = ''
    while not s.isEmpty():
        binNum = binNum + str(s.popItem())      #不断拼接从栈中抛出的字符串
    return binNum

print(dec_to_any(233,16))

