'''
class C:
    def __init__(self, size=10):
        self.size = size

    def getXSize(self):
        return self.size

    def setXSize(self, value):
        self.size = value

    def delXSize(self):
        del self.size

        x = property(getXSize, setXSize, delXSize)
        修改为“使用属性修饰符创建描述符”的方式实现。
'''
class C:
    def __init__(self, size=10):
        self.size = size
    @property
    def x(self):
        return self.size
    @x.setter
    def x(self, value):
        self.size = value
    @x.deleter
    def x(self):
        del self.size
