# -*- coding:utf-8 -*-

'''
@author: eric
@file: 单向链表实现快速排序.py
@time: 2021/9/9 10:40
'''

'''
快速排序的基本思想：
从序列当中选择一个基准数
在这里我们选择序列当中第一个数作为基准数
将序列当中的所有数依次遍历，比基准数大的位于其右侧，比基准数小的位于其左侧
重复步骤1.2，直到所有子集当中只有一个元素为止。
'''

# class Node():
#     def __init__(self, item = None):
#         self.item = item        # 数据域
#         self.next = None        # 指针域
#
# # 链表类，生成链表以及定义相关方法
# class LinkList():
#     def __init__(self):
#         self.head = None
#
#     #生成链表，这里使用list来生成
#     def create(self,item):
#         self.head = Node(item[0])


