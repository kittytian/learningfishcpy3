'''
36例子 对象 = 属性 + 方法
代码定义了对象的特征（属性）和行为（方法），但还不是一个完整的对象，将定义的这些称为类（Class）。
需要使用类来创建一个真正的对象，这个对象就叫作这个类的一个实例（Instance）也叫实例对象（Instance Objects）
类名约定大写字母开头

创建一个对象，也叫类的实例化：
 #先运行程序
tt = Turtle() 创建一个实例对象

'''
class Turtle: # Python 中的类名约定以大写字母开头
    """关于类的一个简单例子"""
    # 属性（变量 静态特征）
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法（函数）
    def climb(self):
        print("我正在很努力的向前爬......")

    def run(self):
        print("我正在飞快的向前跑......")

    def bite(self):
        print("咬死你咬死你！！")

    def eat(self):
        print("有得吃，真满足^_^")

    def sleep(self):
        print("困了，睡了，晚安，Zzzz")
