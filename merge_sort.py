# -*- coding:utf-8 -*-

#归并排序：使用递归，把大问题分割成一个个的小问题，先处理小问题，排序正确后，同样用递归把想要的结果整合起来

def merge_sort(list):

    n = len(list)
    #列表长度小于，不需要排序，直接返回该列表
    if n < 2:
        return list

    #将所需处理的列表一分为2，并使用递归持续拆分，直都每个列表中只有一个元素为止
    mid = n // 2

    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(list[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(list[mid:])

    #定义左右两个游标，对左右列表中的数据进行比较并放入result列表中
    left_pointer, right_pointer = 0, 0

    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1                   #游标需自+1，取尽每一个元素
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1                  #游标需自+1，取尽每一个元素

    #有可能左或者右列表先取完，另一个还剩有元素，故需要将剩余的元素添加到result列表中
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result

if __name__ == "__main__":
    list = [6, 3, 1, 7, 4, 8, 5, 2, 9]
    sorted_list = merge_sort(list)
    print(sorted_list)
