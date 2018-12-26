'''
Python 的作者在很长一段时间不肯加入三元操作符就是怕跟C语言一样搞出国际乱码大赛，
蛋疼的复杂度让初学者望而生畏，
不过，如果你一旦搞清楚了三元操作符的使用技巧，或许一些比较复杂的问题反而迎刃而解。
请将以下代码修改为三元操作符实现：
1.	x, y, z = 6, 5, 4
2.	if x < y:
3.	    small = x
4.	    if z < small:
5.	        small = z
6.	elif y < z:
7.	    small = y
8.	else:
9.	    small = z

'''
'''
自己写的：
x, y, z = 6, 5, 4
small = x if x < y else y
print(small)
small = y if y < z else z
print(small)
small = z if z < x else x
print(small)
答案：
'''
x, y, z = 6, 5, 4
small = x if (x < y and x < z) else (y if y < z else z)
