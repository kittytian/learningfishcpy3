'''
break语句的作用是终止当前循环，跳出循环体。
continue语句的作用是终止本轮循环并开始下一轮循环（这里要注意的是：在开始下一轮循环之前，会先测试循环条件）。

5. 目测以下程序会打印什么？
1.	while True:
2.	    while True:
3.	        break
4.	        print(1)
5.	    print(2)
6.	    break
7.	print(3)
复制代码
会打印：
2
3

因为 break 只能跳出一层循环，记住咯！
'''

while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)