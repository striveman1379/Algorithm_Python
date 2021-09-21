# -*- coding:utf-8 -*-

'''
@author: eric
@file: queue_python.py
@time: 2021/8/22 18:17
'''
"""
采用List来容纳Queue的数据项
将List首端作为队列末尾
将List末尾作为队列首段
enQueue()复杂度是O(n)
deQueue()复杂度是O(1)
"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enQueue(self,item):
        self.items.insert(0,item)

    def deQueue(self):
        return self.items.pop()

    def sizeQueue(self):
        return len(self.items)


