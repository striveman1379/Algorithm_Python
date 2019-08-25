# -*- coding:utf-8 -*-

list = [6,3,1,7,4,8,5,2,9]

n=len(list)

#选择排序算法：选择排序的思路是固定位置，选择排序，即：先从序列中，找到最小的元素，放到第一个位置，然后找到第二小的元素，放到第二个位置，以此类推，直到排好所有的值

def select_sort(list):

    for i in range(n-1):        #i表示趟数，也表示无序区第一个数
        min_loc = i                 #每次i变化时，将最小下标值改为i，将本次循环第一个位置的值
        for j in range(i+1,n):          #当前i位置元素与其之后的所有值进行比对
            if list[min_loc] > list[j]:     #如果最小值比最其后面的某个元素大，就交换它们的位置，保证最小值在前面
                list[min_loc],list[j] = list[j],list[min_loc]
    return list


if __name__=="__main__":
    print(select_sort(list))