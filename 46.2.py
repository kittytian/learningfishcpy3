'''
2. 再来一个有趣的案例：编写描述符 MyDes，使用文件来存储属性，
属性的值会直接存储到对应的pickle（腌菜，还记得吗？）的文件中。如果属性被删除了，文件也会同时被删除，属性的名字也会被注销。
举个栗子：

#>>> class Test:
        x = MyDes('x')
        y = MyDes('y')
        
#>>> test = Test()
#>>> test.x = 123
#>>> test.y = "I love FishC.com!"
#>>> test.x
123
#>>> test.y
'I love FishC.com!
产生对应的文件存储变量的值：
test.py x.pkl y.pkl
如果我们删除 x 属性：

#>>> del test.x
#>>>
对应的文件也不见了：
test.py y.pkl

#参考着写 给它弄懂就行 哪忘了补哪
'''
import os #为了删除pkl文件
import pickle #使用这个模块，就可以轻松地将列表、字典这类复杂类型存储为文件了。
class MyDes:

    saved = [] #设置一个类属性

    def __init__(self, name=None):
        self.var_name = name
        self.file_name = self.var_name + '.pkl'

    def __set__(self, instance, value):

        with open(self.file_name, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.var_name)

    def __get__(self, instance, owner):
        #访问的时候要判断该属性是否存在 删除的时候类属性要删除
        if self.var_name not in MyDes.saved:
            raise AttributeError('%s没有赋值' % self.var_name)

        with open(self.file_name, 'rb') as f:
            value = pickle.load(f)

        return value

    def __delete__(self, instance):
        os.remove(self.file_name)
        MyDes.saved.remove(self.var_name)

class Test:
    x = MyDes('x')
    y = MyDes('y')

test = Test()
test.x = 123
test.y = "I love FishC.com!"
test.x
test.y
#del test.x




