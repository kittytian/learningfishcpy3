'''
现在要求定义一个类，叫水池，水池里要有乌龟和鱼。
在Python里其实很简单，直接把需要的类放进去实例化放进一个新类就可以了，这就叫组合（没有继承关系的横向关系）：
继承：纵向关系
'''
class Turtle:
    def __init__(self, x):
        self.num = x #传入几个x就是多少个乌龟生成

class Fish:
    def __init__(self, x):
        self.num = x

class Pool:
    def __init__(self, x, y):#x个乌龟 y个鱼
        self.turtle = Turtle(x)#实例化乌龟出来 传入 self.turtle这个变量就行
        self.fish = Fish(y)

    def print_num(self):
        #注意一下：self.turtle是乌龟的实例变量 我们要得到的是整形 self.turtle.num
        print('水池里总共有乌龟%d只，小鱼%d条' %(self.turtle.num , self.fish.num))

pool = Pool(1,10)
pool.print_num()
