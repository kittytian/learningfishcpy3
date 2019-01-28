'''
2. 定义一个类 Nstr，当该类的实例对象间发生的加、减、乘、除运算时，将该对象的所有字符串的 ASCII 码之和进行计算：
#>>> a = Nstr('FishC')
#>>> b = Nstr('love')
#>>> a + b
899
#>>> a - b
23
#>>> a * b
201918
#>>> a / b
1.052511415525114
#>>> a // b
1

和41课第2题一样


class Nstr(int):
    def __new__(cls, arg=0):
        if isinstance(arg,str):# 如果arg是字符串
            total = 0 # 初始化变量total
            for each in arg:# 逐一拆分字符串
                total += ord(each)# 每一个字符计算ASCII值后逐次相加
            arg = total# 将结果total赋值给arg
        return int.__new__(cls, arg) # 返回父类int的__new__方法

a = Nstr('FishC')
b = Nstr('love')
print(a + b)
'''


class Nstr:
    def __init__(self, arg=''):
        if isinstance(arg, str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("参数错误！")

    def __add__(self, other):
        return self.total + other.total

    def __sub__(self, other):
        return self.total - other.total

    def __mul__(self, other):
        return self.total * other.total

    def __truediv__(self, other):
        return self.total / other.total

    def __floordiv__(self, other):
        return self.total // other.total
