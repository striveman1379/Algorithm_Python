# -*- coding:utf-8 -*-

'''
@author: eric
@file: stack_01.py
@time: 2021/8/6 9:59
'''

#此栈用list来实现，右边为栈顶
class MyStack:
    def __init__(self):
        self.items = []

    #判断是否为空栈
    def isEmpty(self):
        return self.items == []

    #添加元素
    def pushItem(self,item):
        self.items.append(item)

    #删除栈顶元素
    def popItem(self):
        return self.items.pop()

    #查看栈顶元素
    def peekItem(self):
        return self.items[-1]

    #查看栈的大小
    def sizeItems(self):
        return len(self.items)



