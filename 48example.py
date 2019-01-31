'''
一个容器如果是迭代器，那就必须实现__iter__（）魔法方法，这个方法实际上就是返回迭代器本身。
接下来重点是要实现的是__next__()魔法方法，因为它决定了迭代的规则
斐波那契数列 需要两个因子 所以在init初始化里面定义一个a一个b
'''
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1 #下一个值等于前两个和

    def __iter__(self):
        return self #返回本身 本身是个迭代器

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a #得到下一个斐波那契数列的值





fibs = Fibs()
for each in fibs:
    if each < 20: #加上判断条件 防止崩溃 一定要跳出循环
        print(each)
    else:
        break