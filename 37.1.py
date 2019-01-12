'''
1. 游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
（初学者不一定可以完整实现，但请务必先自己动手，你会从中学习到很多知识的^_^）

假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
游戏生成1只乌龟和10条鱼
它们的移动方向均随机
乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
当移动到场景边缘，自动向反方向移动
乌龟初始化体力为100（上限）
乌龟每移动一次，体力消耗1
当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
鱼暂不计算体力
当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束

【闭包那有道扩展 和这个差不多 记得看看 我是模仿那个扩展写了一部分。。不能完全实现 记得看懂小甲鱼的参考】

自己写的：
import random

x = [0, 10]
y = [0, 10]

class Turtle:
    def __init__(self):
        self.power = 100
        #初始化坐标
        self.x = random.randint(x[0], x[1])
        self.y = random.randint(y[0], y[1])
    def move(self, direction, step):
        # direction参数设置方向，1为向右（向上），-1为向左（向下），0为不移动
        # step参数设置移动的距离
        new_x = self.x + direction[0] * step
        new_y = self.y + direction[1] * step
        # 检查移动后是否超出x轴边界
        if new_x < x[0]:
            self.x = x[0] - (new_x - x[0])
        elif new_x > x[1]:
            self.x = x[1] - (new_x - x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出y轴边界
        if new_y < y[0]:
            self.y= y[0] - (new_y - y[0])
        elif new_y > y[1]:
            self.y = y[1] - (new_y - y[1])
        else:
            self.y= new_y

        self.power -= 1
        return self.x, self.y



    def eat(self):
        if 乌龟和鱼坐标重叠:
            self.power += 20


class Fish:
    def __init__(self):
        self.x = random.randint(x[0], x[1])
        self.y = random.randint(y[0], y[1])
    def move(self,direction, step =1):
        # direction参数设置方向，1为向右（向上），-1为向左（向下），0为不移动
        # step参数设置移动的距离
        new_x = self.x + direction[0] * step
        new_y = self.y + direction[1] * step
        # 检查移动后是否超出x轴边界
        if new_x < x[0]:
            self.x = x[0] - (new_x - x[0])
        elif new_x > x[1]:
            self.x = x[1] - (new_x - x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出y轴边界
        if new_y < y[0]:
            self.y = y[0] - (new_y - y[0])
        elif new_y > y[1]:
            self.y = y[1] - (new_y - y[1])
        else:
            self.y = new_y
        return self.x, self.y
t = Turtle()
for i in range(10):
    f = Fish()

小甲鱼的：用了random.choice函数 就可以像我的思路那样定义direction和step了
'''
import random as r

legal_x = [0,10]
legal_y = [0,10]

#乌龟类
class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, 2, -1, -2])#（只有四种可能）
        new_y = self.y + r.choice([1, 2, -1, -2])

        # 检查移动后是否超出x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y


        # 体力消耗
        self.power -= 1


        # 返回移动后的新位置
        return (self.x, self.y)


    def eat(self):
        self.power += 20
        #判断龟的体力是否大于100 大于100再初始化
        if self.power > 100:
            self.power = 100

#鱼类
class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 返回移动后的新位置
        return (self.x, self.y)


# 全局位置
turtle = Turtle()
fish = [] #鱼变量为空列表 因为要生成10条鱼

for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):  # 判断没有一只鱼
        print('鱼儿都吃完了，游戏结束！')
        break  # 退出死循环
    if not turtle.power:  # 判断龟的没有体力
        print('乌龟体力耗尽，游泳游挂了！^_^')
        break  # 退出死循环

    pos = turtle.move()
    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    #for each_fish in fish[:]:
  #下面的for...in...结构就是迭代器。fish[:]  就是 列表fish的拷贝，不需要特别操作，只要写出这个形式，就已经是新的对象
    for each_fish in fish[:]:  # 鱼列表里元素 分别拷贝给每表鱼变量
        if each_fish.move() == pos:  # 判断每条鱼移动和pos变量是否相等
            # 鱼儿被吃掉了
            turtle.eat()  # 龟的吃的方法
            fish.remove(each_fish)  # 鱼列表删除（每个鱼变量）
            print('有一条鱼儿被吃掉了...')











