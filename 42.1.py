'''
1. 移位操作符是应用于二进制操作数的，现在需要你定义一个新的类 Nstr，也支持移位操作符的运算：
#>>> a = Nstr('I love FishC.com!')
#>>> a << 3
'ove FishC.com!I l'
#>>> a >> 3
'om!I love FishC.c'

字符串切片！！
class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]

'''
class Nstr(str):
    def __lshift__(self, other):
        while other > 0:
            self = self[1:] + self[0]
            other -= 1
        return self

    def __rshift__(self, other):
        while other > 0:
            self = self[-1] + self[:-1]
            other -= 1
        return self

a = Nstr('I love FishC.com!')
print(a << 5)
