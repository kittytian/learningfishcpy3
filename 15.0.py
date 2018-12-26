'''
编写一个进制转换程序，程序演示如下（提示，十进制转换二进制可以用bin()这个BIF）：
'''

flag = True
while flag:
    temp = input('请输入一个整数(输入Q结束程序);')
    if temp != 'Q':
        while not temp.isdigit():
            temp = input('输入有误！请输入一个整数(输入Q结束程序);')
        userinput = int(temp)
        print('十进制 -> 十六进制 ：%d' % userinput, '-> %#x' % userinput)
        print('十进制 -> 八进制 ：%d' % userinput, '-> %#o' % userinput)
        print('十进制 -> 二进制 ：%d' % userinput, '-> %s' % bin(userinput))
    else:
        flag = False






'''
一定要理清楚思路啊啊啊啊啊 怎么写成死循环了呢
拿到程序题 要考虑跳出循环啊 啊啊啊啊

参考：
q = True  %先定义一个flag 再进入循环 flag为假 跳出循环 可以加上判断 
while q:
    num = input('请输入一个整数(输入Q结束程序)：')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制 : %d -> 0x%x' % (num, num))
        print('十进制 -> 八进制 : %d -> 0o%o' % (num, num))
        print('十进制 -> 二进制 : %d -> ' % num, bin(num))
    else:
        q = False

'''