import random

secret = random.randint(1, 10) # 在python中的random.randint(a,b)用于生成一个指定范围内的整数。其中参数a是下限，参数b是下限 生成的随机数n: a <= n <= b。
times = 3
guess = 0
print("猜数字:")
while(guess != secret) and (times>0):
    temp = input()
    while not temp.isdigit():
        temp = input("int please:")
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print("good!")
    else:
        if guess > secret:
            print("bigger!")
        else:
            print("smaller!")
        if times>0:
            print("guess onece more!")
        else:
            print("you cannot guess anymore!")
print("游戏结束")
