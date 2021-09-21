# -*- coding:utf-8 -*-

'''
@author: eric
@file: 链表反转.py
@time: 2021/9/18 14:58
'''

'''
单链表反转
'''

#初始化一个链表节点，节点的属性有val和指针next
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #定义一个反转函数，参数为头节点
    def reverseList(self, head: ListNode) -> ListNode:
        #如果头结点为None或者头节点的下一个节点为None，在直接返回头节点
        if head == None or head.next == None:
            return head
        #最初，前节点为None，cur为当前节点
        pre, cur = None, head
        # 当单前节点不为None时
        while cur:
            tmp = cur.next  #1.先创建临时空间tmp保存当前节点的下一个节点
            cur.next = pre  #2.反转操作需将当前节点的下一个节点执行pre前节点
            pre = cur       #3.此时当前节点的值赋值给前节点pre
            cur = tmp       #4.此时之前保存的tmp节点的值再赋值给当前节点，继续遍历下一个节点的值
        return pre          #因为pre现在存储的是cur的值，所以返回pre

if __name__ == '__main__':
    #创建一个单链表：1,2,3,4,5
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    print(l1.val, l1.next.val, l1.next.next.val, l1.next.next.next.val, l1.next.next.next.next.val) # 1,2,3,4,5

    #初始化类并进行反转操作
    rev = Solution()
    l2 = rev.reverseList(l1)
    print(l2.val, l2.next.val, l2.next.next.val, l2.next.next.next.val, l2.next.next.next.next.val)  # 5,4,3,2,1

