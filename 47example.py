'''
举个例子：编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数。

如果说你希望定制的容器是不可变的话（元组 字符串），你只需要定义__len__()和__getitem__()方法。

__len__(self)    　　　　　　            定义当被 len() 调用时的行为（返回容器中元素的个数）
__getitem__(self, key)                 定义获取容器中指定元素的行为，相当于 self[key]

参数是可变数量的 （*args），因为我们不知道用户要传入多少个数据，
我们把用户输入的数据初始化为一个列表，self.values 就是一个列表，
我们通过列表推导式的形式把数据存放到 self.values 这个列表中。
另外，还需要记录列表中每个元素被访问的次数，我们立刻会想到字典，
我们把每个元素在列表中的下标作为字典的键，然后值就是累计的访问次数。
我们定义 self.count 这个字典，初始化可以使用 fromkeys ，
并把所有下标对应的Key所对应的值初始化为0。
我们这是一个不可变的容器，所以需要定义  __len__() 和 __getitem__() 方法， 
 __len__() 就直接是返回 len(self.values) 的值，
 __getitem__() 中的 key 就是对应的下标，我们这里是获取key对应的值，
 所以需要返回self.values[key]，
 另外，对应着访问了它一次，所以对应的 self.count[key] 加1。




'''
class CountList:

    def __init__(self, *args):
        self.values = [x for x in args] #[有关A的表达式 for A in B]
        self.count = {}.fromkeys(range(len(self.values)), 0) #fromkeys（）方法用于创建并返回一个新的字典，它有两个参数：第一个参数是字典的键；第二个参数是可选的，是传入键对应的值。如果不能提供，那么默认是None。

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key): #key相应下标
        self.count[key] += 1 #获取一次 加1
        return self.values[key]

c1 = CountList(1,3,5,7,9)
c2 = CountList(2,4,6,8,10)
print(c1[1])
print(c1[1]+c2[1])
print(c1.count)



