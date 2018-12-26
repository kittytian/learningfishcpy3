#抄袭小甲鱼的代码 看输出
temp = input('请输入一个整数:')
number = int(temp)
while number:
    i = number - 1
    while i:
        print('#', end = '')#end不换行
        i = i - 1
    j = number
    while j:
        print('*', end = '')
        j = j - 1
    print()#print 默认换行
    number = number - 1
