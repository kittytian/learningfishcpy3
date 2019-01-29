'''
__get__(self, instance, owner)

–用于访问属性，它返回属性的值

（二）•__set__(self, instance, value)

–将在属性分配操作中调用，不返回任何内容

（三）•__delete__(self, instance)

–控制删除操作，不返回任何内容

这三个方法和我们上节课提到的 __getattr__, __setattr__, delattr__是很相像的，但是这三个我们称之为属于描述符属性的方法。__get__用于访问属性的时候直接调用，__set__用于将属性分配，也就是赋值的时候被调用，__delete__用于删除属性的时候被调用。

先来一个最直观的例子：

'''


class MyDescriptor: #描述符类
    def __get__(self, instance, owner):
        print('getting', self, instance, owner)

    def __set__(self, instance, value):
        print('setting', self, instance, value)

    def __delete__(self, instance):
        print('deleting', self, instance)


class Test:
    x = MyDescriptor() #Test类属性x 类似之前property
    #MyDescriptor实现了__get__()、__set__()和__delete__()方法，并且将它的类实例指派给Test类的属性x，所以MyDescriptor就是所谓描述符类。

test = Test() #实例化Test类，然后尝试着对x属性进行各种操作
test.x #getting <__main__.MyDescriptor object at 0x1040fc9b0> <__main__.Test object at 0x1040fcac8> <class '__main__.Test'>
#当访问x属性的时候，Python会自动调用描述符的__get__()方法，几个参数的内容分别是：self是描述符类自身的实例；instance是这个描述符的拥有者所在的类的实例，在这里也就是Test类的实例；owner是这个描述符的拥有者所在的类本身。
print(test) #<__main__.Test object at 0x10458af98>
print(Test)#<class '__main__.Test'>
test.x = 'X-MAN'  #赋值调用set  最后一个参数value是等号右边的值 #setting <__main__.MyDescriptor object at 0x10458af60> <__main__.Test object at 0x10458af98> X-MAN
del test.x #deleting <__main__.MyDescriptor object at 0x10458af60> <__main__.Test object at 0x10458af98>