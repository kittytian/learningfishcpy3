'''
实例化对象时是可以传入参数的，这些参数会自动传入_ _init_ _（）方法中，可以通过重写这个方法来自定义对象的初始化操作
'''
class Ball:
    def __init__(self, name):
        self.name = name
    def kick(self):
        print("我叫%s，该死的，谁踢我..." % self.name)

b = Ball('土豆') #重写init方法后 可以传入name这个参数 #因为重写了__init__(self)方法，实例化对象时需要一个参数
'''
如果c = Ball()##这里没有传入参数就会报错，可以在定义类是给name设置默认参数
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: __init__() missing 1 required positional argument: 'name'
就会报错 必须传name参数
'''