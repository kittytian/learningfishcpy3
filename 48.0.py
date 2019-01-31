'''
0. 用 while 语句实现与以下 for 语句相同的功能：
for each in range(5):
    print(each)

python range() 函数可创建一个整数列表，一般用在 for 循环中。
'''
list1 = range(5)
it = iter(list1)
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)


'''
alist = range(5)
it = iter(alist)
 
while True:
    try:
        print(next(it))
    except StopIteration:
        break


'''
