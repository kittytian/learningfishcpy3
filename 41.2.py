'''
定义一个类继承于 int 类型，并实现一个特殊功能：
当传入的参数是字符串的时候，返回该字符串中所有字符的 ASCII 码的和
（使用 ord() 获得一个字符的 ASCII 码值）。
实现如下：

#>>> print(Nint(123))
123
#>>> print(Nint(1.5))
1
#>>> print(Nint('A'))
65
#>>> print(Nint('FishC'))
461

看答案= = 主要用到了 isinstance方法

'''
class Nint(int):
    def __new__(cls, arg=0):
        if isinstance(arg,str):# 如果arg是字符串
            total = 0 # 初始化变量total
            for each in arg:# 逐一拆分字符串
                total += ord(each)# 每一个字符计算ASCII值后逐次相加
            arg = total# 将结果total赋值给arg
        return int.__new__(cls, arg) # 返回父类int的__new__方法

print(Nint('FishC'))
