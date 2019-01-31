'''
0. 要求实现一个功能与 reversed() 相同（内置函数 reversed(seq) 是返回一个迭代器，是序列 seq 的逆序显示）的生成器。例如：
#>>> for i in myRev("FishC"):
    print(i, end='')

ChsiF
'''
def myRev(data):
    index = len(data) - 1
    while not index < 0:
        yield (data[index])
        index -= 1

for i in myRev("FishC"):
        print(i, end='')

'''
   >>> range(0, -10, -1) # 负数
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]


def myRev(data):
    # 这里用 range 生成 data 的倒序索引
    # 注意，range 的结束位置是不包含的
    for index in range(len(data)-1, -1, -1):
        yield data[index]

'''