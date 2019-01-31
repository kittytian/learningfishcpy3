'''
48斐波那契数列例子用生成器实现
'''
def fibs():
    a = 0
    b = 1 #初始化
    while True:
        a, b = b, a+b
        yield a #生成器可以挂起  所以不是死循环

for each in fibs():
    if each > 100:
        break
    print(each)