'''
编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值


def power(x, y):
    return x ** y

print(power(2,3))
看了答案发现 人家的意思是不用**幂函数
'''


def power(x, y):
    result = 1

    for i in range(y):
        result *= x

    return result


print(power(2, 3))


