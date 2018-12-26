'''#请写一个程序打印出 0~100 所有的奇数
'''
i = 0
while i <= 100:
    if i % 2 != 0:
        print(i)
    i = i + 1
'''
小甲鱼参考：
1.	i = 0
2.	while i <= 100:
3.	    if i % 2 != 0:
4.	        print(i, end=' ')
5.	        i += 1
6.	    else:
7.	        i += 1

'''