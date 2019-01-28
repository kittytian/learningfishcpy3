'''
修改上边【测试题】第 4 题，

class Counter:
        def __init__(self):
                self.counter = 0 # 这里会触发 __setattr__ 调用
        def __setattr__(self, name, value):
                self.counter += 1
“””既然需要 __setattr__ 调用后才能真正设置 self.counter 的值，所以这时候 self.counter 还没有定义，所以没法 += 1，错误的根源。”””
                super().__setattr__(name, value)
        def __delattr__(self, name):
                self.counter -= 1
                super().__delattr__(name)

使之可以正常运行：编写一个 Counter 类，用于实时检测对象有多少个属性。
程序实现如下：

#>>> c = Counter()
#>>> c.x = 1
#>>> c.counter
1
#>>> c.y = 1
#>>> c.z = 1
#>>> c.counter
3
#>>> del c.x
#>>> c.counter
2

'''

class Counter:
        def __init__(self):
                super().__setattr__('counter', 0)

        def __setattr__(self, name, value):
            super().__setattr__('counter', self.counter + 1)
            super().__setattr__(name, value)

        def __delattr__(self, name):
                super().__setattr__('counter', self.counter - 1)
                super().__delattr__(name)

c = Counter()
c.x = 1
c.y = 2
print(c.counter)
del c.y
print(c.counter)