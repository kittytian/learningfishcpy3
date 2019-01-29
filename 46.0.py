'''
0. 按要求编写描述符 MyDes：当类的属性被访问、修改或设置的时候，分别做出提醒。
程序实现如下：

#>>> class Test:
        x = MyDes(10, 'x')

#>>> test = Test()
#>>> y = test.x
正在获取变量： x
#>>> y
10
#>>> test.x = 8
正在修改变量： x
#>>> del test.x
正在删除变量： x
噢~这个变量没法删除~
#>>> test.x
正在获取变量： x
8
答：其实大家如果自己认真思考了代码，会发现我们这里描述符起到的作用是间接地保存指定变量的数据。

'''
class MyDes:
    def __init__(self, varval=None, varname=None):
        self.var = varval
        self.name = varname
    def __get__(self, instance, owner):
        print('正在获取变量:', self.name)
        return self.var
    def __set__(self, instance, value):
        print('正在修改变量：', self.name)
        self.var = value
    def __delete__(self, instance):
        print('正在删除变量：', self.name)
        print('噢~这个变量没法删除~')

class Test:
    x = MyDes(10, 'x')

test = Test()
y = test.x
print(y)
test.x = 8
del test.x
test.x
print(test.x)

