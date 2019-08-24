# -*- coding:utf-8 -*-


list = [6,3,1,7,4,8,5,2,9]

def quick_sort(list):
    #如果list为空或只有一个值
    if len(list) < 2:
        return list

    #设置一个基准值，譬如list第一个元素，list中的其它元素与其比较大小
    else:
        pivot = list[0]
        left = quick_sort([i for i in list[1:] if i <= pivot])
        right = quick_sort([i for i in list[1:] if i > pivot])

        return left + [pivot] +right




if __name__ == '__main__':
    print(quick_sort(list))