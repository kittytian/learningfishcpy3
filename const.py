'''
50课后题要写的const
这个以后能用到

在 const 模块中我们到底做了什么，使得这个模块这么有“魔力”呢？大家跟着小甲鱼的提示，一步步来做你就懂了：

提示一：我们需要一个 Const 类
提示二：重写 Const 类的某一个魔法方法，指定当实例对象的属性被修改时的行为
提示三：检查该属性是否已存在
提示四：检查该属性的名字是否为大写
提示五：细心的鱼油可能发现了，怎么我们这个 const 模块导入之后就把它当对象来使用（const.NAME = "FishC"）了呢？
难道模块也可以是一个对象？没错啦，在 Python 中无处不对象，到处都是你的对象。
使用以下方法可以将你的模块与类 A 的对象挂钩:
'''
#sys.modules 是一个字典，它包含了从 Python 开始运行起，被导入的所有模块。键就是模块名，值就是模块对象。
'''
import sys
sys.modules[__name__] = A()


'''

class Const:
    def __setattr__(self, name, value):
        if name in self.__dict__: #self._dict_实例化对象的所有属性 它的作用是以字典的形式显示出当前对象的所有属性以及相对应的值：
            raise TypeError('常量无法改变！')
        if not name.isupper(): #判断大写
            raise TypeError('常量名必须由大写字母组成！')
        self.__dict__[name] = value



import sys
sys.modules[__name__] = Const()
