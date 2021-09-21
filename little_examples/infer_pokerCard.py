# -*- coding:utf-8 -*-

'''
@author: eric
@file: infer_pokerCard.py
@time: 2021/8/12 17:27
'''

"""
*1.
从牌顶拿出一张牌，放到桌子上
*2.
从牌顶拿出一张牌，放在牌的底部
*3.
重复第一步，第二步操作，知道所有的牌都放到了桌子上
*
*问：已知桌子上牌的顺序是1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
*牌原来的顺序是什么
*
*分析：如果这个操作倒着来
*1.
从牌底部拿一张牌放到牌顶
*2.
从桌子上拿一张牌放到牌顶
"""


from collections import deque

def findCardLocation(location):
    resqueue = deque()
    print("resqueque---",resqueue)
    n = len(location)
    for i in range(n-1,-1,-1):
        if resqueue:
            print(resqueue)
            resqueue.appendleft(resqueue.pop())
        resqueue.appendleft(location[i])
        # print(resqueue)
    return resqueue

if __name__ == '__main__':
    # location = [1,2,3,4]
    # location = [4,2,3,1]
    location = [4,2,3,1]                    #牌桌，从上到下
    # location = [1,3,2,4]
    # location = [4,2,5,1,3]
    # location = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    list1 = findCardLocation(location)
    print(list1)                            #原始，从上到下
    print(type(list1))
