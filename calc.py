#1. 编写程序：calc.py 要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑

temp = input("输入1到100的数字: ")
guess = int(temp)
if 1 <= guess <= 100:
    print("hao piao liang")
else:
    print("hao chou")