'''
_ _new_ _（）才是在一个对象实例化的时候所调用的第一个方法。它跟其它魔法方法不同，它的第一个参数不是self而是这个类（cls），而其它参数会直接传递给_ _init_ _（）方法的。在 _ _init_ _（）之前被调用
_ _new_ _（）方法需要返回一个实例对象，通常是cls这个类实例化的对象，当然你也可以返回其它对象。
_ _new_ _（）方法平时很少去重写它，一般让Python用默认的方案执行就可以了。但是又一种情况需要重写这个魔法方法，就是当继承一个不可变的类型的时候，它的特性就显得尤为重要了

'''
class capStr(str):
    def __new__(cls,string):
        string = string.upper() #重写
        return str.__new__(cls, string) # 在 __new__替换string 再调用string的重写的new 返回一个对象

a = capStr('taq love gym')
print(a)