'''
尝试自己举例说明如何使用类的静态方法，并指出使用类的静态方法有何有点和需要注意的地方？（一定要自己先动手再看答案哦^_^）
答：静态方法是类的特殊方法，静态方法只需要在普通方法的前边加上 @staticmethod 修饰符即可。
'''
class C:
    @staticmethod ## 该修饰符表示 static() 是静态方法
    def static(arg1, arg2, arg3):
        print(arg1, arg2, arg3, arg1+arg2+arg3)
    def nostatic(self):
        print("I'm the f**king normal method!")

'''
静态方法最大的优点是：不会绑定到实例对象上，换而言之就是节省开销。

>>> c1 = C()
>>> c2 = C()
# 静态方法只在内存中生成一个，节省开销
>>> c1.static is C.static
True
>>> c1.nostatic is C.nostatic
False
>>> c1.static
<function C.static at 0x03001420>
>>> c2.static
<function C.static at 0x03001420>
>>> C.static
<function C.static at 0x03001420>
# 普通方法每个实例对象都拥有独立的一个，开销较大
>>> c1.nostatic
<bound method C.nostatic of <__main__.C object at 0x03010590>>
>>> c2.nostatic
<bound method C.nostatic of <__main__.C object at 0x032809D0>>
>>> C.nostatic
<function C.nostatic at 0x0328D2B8>
使用的时候需要注意的地方：静态方法并不需要 self 参数，因此即使是使用对象去访问，self 参数也不会传进去。

>>> c1.static(1, 2, 3)
1 2 3 6
>>> C.static(1, 2, 3)
1 2 3 6


'''
