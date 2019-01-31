'''
48example 迭代器设置参数 避免一直迭代
'''
class Fibs:
    def __init__(self, n=10):
        self.a = 0
        self.b = 1 #下一个值等于前两个和
        self.n = n

    def __iter__(self):
        return self #返回本身 本身是个迭代器

    def __next__(self): #在next那加条件控制
        self.a, self.b = self.b, self.a + self.b
        if self.a >self.n:
            raise StopIteration
        return self.a #得到下一个斐波那契数列的值





fibs = Fibs()
for each in fibs:
        print(each)
#更改n：
fibs = Fibs(100)
for each in fibs:
        print(each)
