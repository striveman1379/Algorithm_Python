# -*- coding:utf-8 -*-


#长方形完整格式

# for i in range(1,10):
#     for j in range(1,10):
#         print("%d*%d=%2d"%(i,j,i*j),end=" ")
#     print(' ')




#左下三角
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=" ")
    print(' ')

