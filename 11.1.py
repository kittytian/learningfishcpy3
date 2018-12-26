'''
列表推导式（List comprehensions）也叫列表解析，灵感取自函数式编程语言 Haskell。Ta 是一个非常有用和灵活的工具，可以用来动态的创建列表，语法如：

[有关A的表达式 for A in B]

例如
1.	>>> list1 = [x**2 for x in range(10)]
2.	>>> list1
3.	[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
复制代码
相当于
1.	list1 = []
2.	for x in range(10):
3.	    list1.append(x**2)
复制代码

问题：请先在 IDLE 中获得下边列表的结果，并按照上方例子把列表推导式还原出来。
1.	>>> list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
复制代码

'''
list1 = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 2 != 0:
                list1.append((x, y))
print(list1)

'''
1.	>>> list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
复制代码
1.	list1 = []
2.	for x in ragne(10):
3.	    for y in range(10):
4.	        if x%2 == 0:
5.	            if y%2 != 0:
6.	                list1.append((x, y))
复制代码

'''