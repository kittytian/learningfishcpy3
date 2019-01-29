'''
property事实上就是一个描述符类。下边就定义一个属于我们自己的MyProperty 来实现property的所有功能：（我们这里定义的MyProperty只是把 property 的功能进行照搬，大家可以加入自己的创意）：
'''
class MyProperty:
    def __init__(self,fget = None,fset = None,fdel=None):#之前property几个参数
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):#当他被调用 执行对应的获取方法 fget
        return self.fget(instance) #fget有参数 传入拥有者的实例对象instance

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self,instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = None
    def getX(self):
        return self._x #_x表示不希望外部访问 用指定的方法访问
    def setX(self,value):
        self._x = value
    def delX(self):
        del self._x
    x = MyProperty(getX, setX, delX)

c = C()
c.x = 'X-man'
print(c.x)
print(c._x)






