'''
一般面向对象的编程语言都会区分公有和私有的数据类型，像c++和Java它们使用public和private关键字，用于声明数据是公有的还是私有的，但在Python中并没有用类似的关键字来修饰。
难道Python所有东西都是透明的？也不全是，默认上对象的属性和方法都是公开的，可以直接通过点操作符（.）进行访问：

class Person:
    name = '小甲鱼'

p = Person()
p.name
'小甲鱼'

为了实现类似私有变量的特征，Python内部采用了一种叫name mangling（名字改编）的技术，
在Python中定义私有变量只需要在变量名或函数名前加上“_ _”两个下划线，那么这个函数或变量就会成为私有的了：
class Person:
    __name = '小甲鱼'

p = Person()
p.__name
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'Person' object has no attribute '__name'
访问 就要这么写：

'''

class Person:
    __name = '小甲鱼'
    def getName(self):
        return self.__name

p = Person()
#p.getName()
p._Person__name

