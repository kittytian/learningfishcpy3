print('-------')
temp = input("猜数字：")  #input是python内置函数 返回用户输入
guess = int(temp)#int内置函数（BIF) 字符串返回整形
if guess == 8:
    print("you guess right")
    print("no reward!")
else:
    print("guess wrong !the right answer is 8")
print("exit~")