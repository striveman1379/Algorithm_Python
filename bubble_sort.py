# -*- coding:utf-8 -*-


list = [6,3,1,7,4,8,5,2,9]


#冒泡排序，相邻元素两两比较，大的值放后面，小的值放前面，大的再和其后面的作比较。每走一次，前面为序区，后面为有序区
def bubble_sort(list):
    n = len(list)
    for i in range(n-1):    #负责循环所走的次数
        for j in range(n-i-1):      #j为下标，因为从j开始取，j到列表的倒数第二位，j+1到最后一位，因为是递减的，所以要减i
            if list[j] > list[j+1]:         #如果前面的数大于后面的数，就交换位置
                list[j],list[j+1] = list[j+1],list[j]

    return list



if __name__ == '__main__':
    print(bubble_sort(list))
