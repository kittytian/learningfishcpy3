'''
0. 编写一个符合以下要求的函数：
    a) 计算打印所有参数的和乘以基数（base=3）的结果
    b) 如果参数中最后一个参数为5，则设定基数为(base =5)，基数不参与求和计算。
'''

def myfunc(*params,base = 3):
    result = 0
    for each in params:
        result += each
    result *= base
    return result

print(myfunc(1,2,3,4,5,base= 5))


