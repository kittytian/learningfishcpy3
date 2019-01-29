'''
0. 根据课堂上的例子，定制一个列表，同样要求记录列表中每个元素被访问的次数。
这一次我们希望定制的列表功能更加全面一些，比如支持 append()、pop()、extend() 原生列表所拥有的方法。你应该如何修改呢？

要求1：实现获取、设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）
要求2：增加 counter(index) 方法，返回 index 参数所指定的元素记录的访问次数
要求3：实现 append()、pop()、remove()、insert()、clear() 和 reverse() 方法（重写这些方法的时候注意考虑计数器的对应改变）

今天只有一道动动手的题目，但在写代码的时候要时刻考虑到你的列表增加了计数器功能，所以请务必要考虑周全再提交答案。

附课堂上的例子：
class CountList:
        def __init__(self, *args):
                self.values = [x for x in args]
                self.count = {}.fromkeys(range(len(self.values)), 0)

        def __len__(self):
                return len(self.values)

        def __getitem__(self, key):
                self.count[key] += 1
                return self.values[key]


为了实现这些功能 不能用字典存放元素的计数了
对于列表来说 删除一个元素 其他元素下标会发生变化
改用一个列表存放元素的计数

继承父类list 用父类方法初始化
小甲鱼参考：

'''
class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0) #初始化为0

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1 #每次访问,count对应索引位置的值会加1,也就实现了计数
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key,value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()


c1 = CountList(1,3,5,7,9)
print(c1[3])
print(c1.counter(3))


