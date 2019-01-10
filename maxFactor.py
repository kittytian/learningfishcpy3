'''
34课例子  else和while搭配使用 和for也是这样
求这个小程序主要是要求用户输入的数的最大约数，
如果是素数的话就顺便提醒一下”这是一个素数“。
注意要使用地板除法（count = num // 2）哦，否则结果会出错。
使用暴力的方法一个一个尝试（num % count == 0），如果符合条件则打印最大的约数，
并break，同时不会执行else语句块的内容了。如果一直没遇到合适的条件，则会执行else语句块内容。
'''

def showMaxFactor(num):
    count = num // 2
    while count > 1:#count最大因数
        if num % count == 0:
            print('%d最大的约数是%d' % (num, count))
            break
        count -= 1#每次因数－1
    else:
        print('%d是素数！' % num)

num = int(input('请输入一个数：'))
showMaxFactor(num)
