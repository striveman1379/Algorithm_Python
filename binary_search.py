# -*- coding:utf-8 -*-



list=[1, 2, 3, 4, 5, 6, 7, 8, 9]

element = 8


#二分查找，必须是正向有序的序列，
def binary_search(list,element):

    low = 0
    high = len(list) - 1
    while low<=high:

        #二分嘛，一分为2地查找
        mid = (high + low) // 2
        #如果找到该元素就返回
        if list[mid]==element:
            return mid
        #如果所要查找的元素在比当前位置元素大，就往右边区域去找，反之则往左边区域
        elif list[mid]<element:
            low=mid+1
        else:
            high=mid-1

    return False            #没找到，返回false

print(binary_search(list,element))



"""
#二分查找，递归版本------有问题

def binary_search2(list,element):

    if len(list)==0:
        return False
    else:
        mid = len(list)//2

        if list[mid]==element:
            return mid
        else:
            if element<list[mid]:
                return binary_search2(list[:mid], element)
            else:
                return binary_search2(list[mid + 1:], element)


print(binary_search2(list,9))

"""