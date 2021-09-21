# -*- coding:utf-8 -*-

'''
@author: eric
@file: 单例__new__方法.py
@time: 2021/8/9 18:28
'''

# 基于__new__方法实现（推荐使用，方便）
# 当我们实现单例时，为了保证线程安全需要在内部加入锁
# 我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），
# 实例化对象；然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式

import threading

class Singleton:
    _instance_lock = threading.Lock()

    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        with Singleton._instance_lock:
            if not hasattr(Singleton,"_instance"):
                Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)

def task(args):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()



'''
输出：
<__main__.Singleton object at 0x0000025491F925F8> <__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
<__main__.Singleton object at 0x0000025491F925F8>
'''