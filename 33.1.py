'''
还记得我们第一个小游戏吗？
只要用户输入非整型数据，程序立刻就会蹦出不和谐的异常信息然后崩溃。

'''
import random

secret = random.randint(1, 10)
print('------------------我爱鱼C工作室------------------')
try:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)
    while guess != secret:
        temp = input("哎呀，猜错了，请重新输入吧：")
        guess = int(temp)
        if guess == secret:
            print("我草，你是小甲鱼心里的蛔虫吗？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
    print("游戏结束，不玩啦^_^")
except ValueError as reason:
    print('输入类型出错啦\n错误的原因是：' + str(reason))

'''
参考代码：
这里对可能导致异常的 guess = int(temp) 进行监测、
自己没写 guess = secret

import random

secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
try:
    guess = int(temp)
except ValueError:
    print('输入错误！')
    #guess = secret 
     不妨猜一下小甲鱼现在心里想的是哪个数字：a
Traceback (most recent call last):
  File "/Users/kittytian/PycharmProjects/xiaojiayu/33.1.py", line 42, in <module>
    while guess != secret:
NameError: name 'guess' is not defined
输入错误！

while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束，不玩啦^_^")

'''
