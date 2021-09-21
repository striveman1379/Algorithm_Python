# -*- coding:utf-8 -*-

'''
@author: eric
@file: tread_test.py
@time: 2021/8/10 10:49
'''


# 类方法

# class ClassTest:
#     _number = 0
#
#     @classmethod
#     def addNum(cls):
#         cls._number += 1
#
#     @classmethod
#     def getNum(cls):
#         return cls._number
#
#     def __new__(self):
#         ClassTest.addNum()
#         return super(ClassTest, self).__new__(self)
#
#
# class Student(ClassTest):
#     def __init__(self):
#         self.name = ""
#
# s1 = Student()
# s1.addNum()
#
# s2 = Student()
# s2.addNum()
#
# s3 = Student()
# s3.addNum()
#
# print(ClassTest.getNum())



#静态方法
# import time
#
# class TimeTest:
#     def __init__(self,hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     @staticmethod
#     def showtime():
#         return time.strftime("%H:%M:%S", time.localtime())
#
# print(TimeTest.showtime())
# t = TimeTest(10,10,18)
# nowTime = t.showtime()
# print(nowTime)

# class Singleton(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance == None:
#             print(super(Singleton, cls))
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance
#
# s1 = Singleton()
# s2 = Singleton()
#
# print(s1)
# print(s2)


# class Fruit:
#     def __init__(self):
#         pass
#     def color(self):
#         print('nothing')
#
# class Apple(Fruit):
#     def __init__(self):
#         pass
#     def color(self):
#         print("苹果是红色")
#
# class Orange(Fruit):
#     def __init__(self):
#         pass
#
#     def color(self):
#         print("橘子是橙色")
#
# class Fruits(object):
#     fruits = {'apple':Apple,'orange':Orange}
#
#     def __new__(cls, name):
#         if name in Fruits.fruits.keys():
#             return Fruits.fruits[name]()
#         return Fruit()
#
# apple = Fruits("apple")
# orange = Fruits("orange")
# apple.color()
# orange.color()
#
# peer = Fruits("peer")
# peer.color()

