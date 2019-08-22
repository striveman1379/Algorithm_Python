# -*- coding:utf-8 -*-


#插入排序：默认列表第一个元素为有序区，无序区从第二个元素开始，依次取出每一个元素，放入到前面的与有序区元素依次作比较，插入到合适的位置

def insert_sort(list):
    n = len(list)
    for i in range(1,n):    #循环无序区的元素
        j=i                 #变量j为所抽取的要插入到有序区的元素的索引，代表临时手牌
        while j>0:          #手牌不能为list的第一个元素，故j必须大于0
            if list[j]<list[j-1]:       #如果手牌遇到的有序区元素比它大，便交换位置一直向前插
                list[j],list[j-1] = list[j-1],list[j]
                j -= 1      #因为手牌必须与依次向前有序区的元素作比较，直到遇到比其小的元素位置
            else:
                break

    return list


if __name__ == "__main__":
    list = [6, 3, 1, 7, 4, 8, 5, 2, 9]
    print(insert_sort(list))