'''
1. 按照以下要求，定义一个类实现摄氏度到华氏度的转换（转换公式：华氏度 = 摄氏度*1.8+32）
要求：我们希望这个类尽量简练地实现功能，如下

#>>> print(C2F(32))
89.

class C2F:
      def __init__(self,c)
            self.c = c
      def caculate (self, c,f):

            self.f = self.c *1.8 +32
            return self.f

参考答案了 不熟 = = 继承float这个基类
'''
class C2F(float):
    def __new__(cls, args = 0.0):
        return float.__new__(cls, args *1.8 +32)

print(C2F(32))