'''
寻找水仙花数
题目要求：如果一个3位数等于其各位数字的立方和，
则称这个数为水仙花数。例如153 = 1^3+5^3+3^3，
因此153是一个水仙花数。编写一个程序，找出所有的水仙花数


def flower():
    for i in range(100, 1000):
        sum = 0
        temp = i
        while temp:
            sum = sum + (temp % 10) ** 3
            temp //= 10  # 注意这里要使用地板除哦~
        if sum == i:
            print(i)
flower()

可以用更简单的方式：
当成字符串 第【0】【1】【2】按索引就是百位 十位 个位:
下面参考代码
'''


def Find():
    for i in range(100, 1000):
        if int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3 == i:
            print(i)


Find()
