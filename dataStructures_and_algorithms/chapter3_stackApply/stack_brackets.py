# -*- coding:utf-8 -*-

'''
@author: eric
@file: stack_brackets.py
@time: 2021/8/9 9:47
'''

from dataStructures_and_algorithms.chapter3_stackApply.stack_01 import MyStack

"""
碰到各种左括号仍然入栈
碰到各种右括号的时候需要判断栈顶的左括号是否跟右括号属于同一种类
"""


def stack_match_brackets(bracketString):
        s = MyStack()
        balanced = True     #平衡tag
        index = 0       #待匹配字符串索引

        #当待匹配字符串大于0且默认平衡时开始匹配
        while index < len(bracketString) and balanced:
            symbol = bracketString[index]           #symbol为当前匹配的符号
            if symbol in "({[":                     #如果symbol为左括号其中之一，就压入栈
                s.pushItem(symbol)

            else:      # 如果当前值不是左括号中的元素
                if s.isEmpty():   #当前值不是左括号中的元素且栈是空的，没有与symbol进行匹配的元素，则为不对称
                    balanced = False
                else:   #当前值不是左括号中的元素且栈不空，取出栈顶元素与匹配
                    left = s.popItem()
                    if not matches(left,symbol):        #如果左右匹配为false，则为不对称
                        balanced = False
            index = index+1     #当前值是左括号中的元素或者匹配成功的情况下，index+1

        #如果栈是空的，且对称性为true，则代表所以括号都匹配完成或者字符串为空
        if s.isEmpty() and balanced:
            return True
        else:
            return False


#匹配左右两个括号，且下面括号的位置要对称
def matches(left, right):
    lefts = "({["
    rights = ")}]"
    return lefts.index(left) == rights.index(right)


bracketString = "{[([])]}}"
# bracketString = ""
print(stack_match_brackets(bracketString))