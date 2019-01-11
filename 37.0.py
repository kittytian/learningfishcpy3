'''
0. 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
平日票价100元
周末票价为平日的120%
儿童半票
自己的思路是定义一个方法 在里面定义票价 但是没有充分使用类。类是高度抽象的，此处类应该可以涵盖成人和小孩。
参考小甲鱼的代码 重新写。
'''
class Ticket:
    def __init__(self, weekend=False, child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self,num):
        return self.exp * self.inc * self.discount * num

adult = Ticket()
child = Ticket(child=True)
print("2个成人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))

'''
class Ticket():#票的类
    def __init__(self, weekend = False, child = False):
        #定义魔法__init__函数（票, 周末= 假, 孩子=假）
        
        self.exp = 100 # 平日票价100
        if weekend:#判断周末是否为真
            self.inc = 1.2 # 周末票价为平日的120%
        else: # 周末为假
            self.inc = 1 # 平日票价的100%
        if child: # 判断孩子是否为真
            self.discount = 0.5 # 孩子半价
        else: # 不是孩子
            self.discount = 1 # 孩子平日票价100%

    def calcPrice(self, num): # 定义价钱函数
        return self.exp * self.inc * self.discount * num 
        # 返回 平日票价 * 周末票价 * 孩子票价 * 用户输入的数

adult = Ticket() # 票的类赋值给adult（成人）
child = Ticket(child = True) # 孩子的类

print('2个成人 + 1个小孩平日票价为：%.2f' % (adult.calcPrice(2) + child.calcPrice(1)))
# 打印2个成人 + 1个小孩平日票价为：%（程序计算结果,格式为保留小数点两位）
#2个成人 + 1个小孩平日票价为：250.00

#2个成人票价程序计算方式为：adult.calcPrice(2)

adult = Ticket() #()空代表默认参数 (self, weekend = False, child = False)
adult.calcPrice(adult, 2)
self.exp * self.inc * self.discount * num
100 * 1 * 1 * 2 等于 200

# 1个小孩平日票价程序计算方式：

child = Ticket(child = True)相当如(self, weekend = False, child = True)
child.calcPrice(child, 1)
self.exp * self.inc * self.discount * num
100 * 1 * 0.5 * 1 等于 50


# 结果 (adult.calcPrice(2) + child.calcPrice(1)) 200 + 50 等于 250
'''

