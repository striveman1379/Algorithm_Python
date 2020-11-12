# -*- coding:utf-8 -*-

'''
@author: eric
@file: anagram.py
@time: 2020/11/12 16:27
'''

'''
判断两个词是否为变位词。
变位词指的是一个单词可以通过改变其他单词中字母的顺序来得到，也叫做兄弟单词，如army->mary

判断两个字符串是否为变位词
'''


'''
解法1：排序比较（时间复杂度 O(nlogn) ）

将两个字符串都按照字母顺序排好序，再逐个字符进行对比，如果都相同就是变位词，有任何不同就不是变位词
'''

'''
def anagram(s1,s2):
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False
        
print(anagram('apple','ppale'))



def anagram(s1,s2):
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    pos = 0
    matches = True

    while pos < len(list1) and matches:
        if list1[pos] == list2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches
    
print(anagram('apple','ppale'))
'''


'''
解法2：计数比较【时间复杂度O(n)】

为判断两个字符串是否为变位词，我们首先计算每一个字符在字符串中出现的次数。由于
共有 26 个可能的字符，我们可以利用有 26 个计数器的列表，每个计数器对应一个字符。每当我们 看到一个字符，
就在相对应的计数器上加一。最终，如果这两个计数器列表相同，则这两个字符串 是变位词。
'''

def anagram(s1,s2):
    list1 = [0]*26
    list2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        list1[pos] = list1[pos]+1
    print(list1)

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        list2[pos] = list2[pos]+1

    print(list2)

    num = 0
    matches = True
    while num < len(list1) and matches:
        if list1[num] == list2[num]:
            num+=1
        else:
            matches = False
    return matches

print(anagram('apple','ppale'))





