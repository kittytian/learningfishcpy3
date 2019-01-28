'''
 Python 的修饰符就是一种优雅的封装，但要注意的是只可以在模块或类定义内对函数进行修饰，不允许修饰一个类。

一个修饰符就是一个函数，它将被修饰的函数做为参数，并返回修饰后的同名函数或其它可调用的东西
'''
import time


def timeslong(func):
    def call():
        start = time.clock()
        print("It's time starting ! ")
        func()
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)

    return call


@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y
#f = timeslong(f) 修饰符相当于这个

print(f())

