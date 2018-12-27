'''
1. 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。
举例：get_digits(12345) ==> [1, 2, 3, 4, 5]

看了下答案解题思路：利用除以10取余数的方式，每次调用get_digits(n//10)，并将余数存放到列表中即可。要注意的是结束条件设置正确。
自己写:


def get_digits(n):
    list1 = []
    if n:
        list1.append(n % 10)
        get_digits(n // 10)
    print(list1)

get_digits(12345)

输出[]
[1]
[2]
[3]
[4]
[5]

'''

result = []


def get_digits(n):
    if n > 0:
        result.insert(0, n % 10)
        get_digits(n // 10)


get_digits(12345)
print(result)
