# -*- coding:utf-8 -*-

'''
@author: eric
@file: queue_热土豆问题.py
@time: 2021/8/22 18:59
'''

"""
模拟程序采用队列来存放所有参加游戏的人名，按照传递土豆方向从队首排到队尾
游戏时，队首始终是持有土豆的人

模拟游戏开始，只需要将队首的人出队，随即再到队尾入队，算是土豆的一次传递
传递了num次后，将队首的人移除，不再入队，如此反复，直到队列中剩余1人
"""

from dataStructures_and_algorithms.chapter4_queueApply.queue_python import Queue

def hotPotato(nameList, num):
    #创建一个简单队列
    simQueue = Queue()
    for name in nameList:
        simQueue.enQueue(name)
    while simQueue.sizeQueue() > 1:
        for i in range(num):
            simQueue.enQueue(simQueue.deQueue())
            print(simQueue)

    return simQueue.deQueue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))


