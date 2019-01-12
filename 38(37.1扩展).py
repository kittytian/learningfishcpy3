'''
38课堂例子 ——继承
扩展37课后作业：对鱼类进行细分，有金鱼（Goldfish）、三文鱼（Salmon）、鲤鱼（Carp），还有鲨鱼（Shark）。
'''
import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10) #范围就是0到10包括
        self.y = r.randint(0, 10)

    def move(self):
        #演示继承 边界先不考虑 假设所有的鱼都是一路向西游 每次x减一格
        self.x -= 1
        print('我的位置是：', self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #调用未绑定的父类方法 :
        #这里需要注意的是这个self并不是父类Fish的实例对象，而是子类Shark的实例对象，所以这里说的未绑定是指并不需要绑定父类的实例对象，使用子类的实例对象代替即可。
        #Fish.__init__(self) #调用未绑定的父类方法 :

        #使用super函数:super函数的“超级”之处在于你不需要明确给出任何基类的名字，它会自动帮你找到所有基类以及对应的方法。由于你不用给出基类的名字，这就意味着如果需要改变类继承关系，只要改变class语句里的父类即可，而不必要在大量代码中去修改所有被继承的方法。
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃☆´∀｀☆')
            self.hungry = False
        else:
            print('太撑了 吃不下了')

fish = Fish()
fish.move()
goldfish = Goldfish()
goldfish.move()
goldfish.move()
goldfish.move()
shark = Shark()
shark.eat()
shark.eat()
shark.move() #会报错：AttributeError: 'Shark' object has no attribute 'x' __int__(self)重写了 所以会覆盖父类的方法
'''
在Shark类中，重写了魔法方法_ _init_ _,但新的_ _int_ _方法里边没有初始化鲨鱼的x坐标和y坐标，因此调用move方法就会出错。那么解决这个问题的方案就很明显了，应该在鲨鱼类中重写_ _int_ _方法的时候先调用基类Fish的_ _init_ _方法。
下面介绍两种可以实现的技术：
（1）调用未绑定的父类方法
（2）使用super函数

'''




