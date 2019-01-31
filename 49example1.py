'''

列表推导式
'''
a = [i for i in range(100) if not (i % 2) and i % 3] #求得就是100以内，能被2整除但不能被3整除的所有整数
print(a) #[2, 4, 8, 10, 14, 16, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52, 56, 58, 62, 64, 68, 70, 74, 76, 80, 82, 86, 88, 92, 94, 98]

#字典推导式 有:是字典
b = {i: i % 2 == 0 for i in range(10)} #判断是否为偶数
print(b) #{0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}

#集合推导式 没有：是集合
c = {i for i in [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 3, 2, 1]}
print(c) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

#字符串没有推导式 只要有双引号 就是字符串
d = "i for i in 'i love gym'"
print(d)#输出 i for i in 'i love gym'

#生成器推导式！！！！！用普通小括号括起来的
e = (i for i in range(10))
print(e) #输出 <generator object <genexpr> at 0x1040aedb0>
print(next(e))
print(next(e))
print(next(e))
for each in e:
    print(each)

#生成器推导式如果作为函数的参数，可以直接写推导式，而不用加小括号：
print(sum(i for i in range(100) if i % 2)) #不能被2整除的和