'''
这几个魔法方法在使用上需要注意的是，有一个死循环的陷阱，初学者很容易中招，通过一个实例来讲解。
写一个矩形类，默认有宽和高两个属性；
如果为一个叫square的属性赋值，那么说明这是一个正方形，值就是正方形的边长，此时宽和高都应该等于边长

赋值会触发 setattr 这个魔法方法 所以重写这个

getattr 也可能会遇到死循环


'''
class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height #触发setattr 然后走setattr的else self name = value 又回来这 死循环
        #实例化对象，调用__init__()方法，在这里self.width和self.heigth分别初始化赋值。一发生赋值操作，就会自动触发__setattr__（）魔法方法，width和height两个属性被赋值，于是执行else的下边的语句，就变成了self.width = value,那么就相当于又触发了__setattr__(),那么这样就依赖基类的方法来实现赋值
    def __setattr__(self, name, value): #name是赋值等号左边的 value是右边的
        if name == 'square':
            self.width = value
            self.height = value
        else: #如果不是 就按默认赋值 方法一 调用基类操作
            #self.name = value
            #super().__setattr__(name, value) 方法二是给特殊属性__dict__赋值。对象有一个特殊属性，叫做__dict__,它的作用是以字典的形式显示出当前对象的所有属性以及相对应的值
            self.__dict__[name] = value
    def getArea(self):
        return self.width * self.height


r1 = Rectangle(4,5)
print(r1.getArea())
r1.square = 10
print(r1.getArea())
print(r1.__dict__)