'''
property（fget = None，fset = None，fdel = None，doc = None）
第一个参数是获取属性的方法名（例子中是getSize），
第二个参数是设置属性的方法名（例子中是setSize），
第三个参数是删除属性的方法名（例子中是delSize）。

'''

class C:
    def __init__(self,size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize,setSize,delSize)
'''
c1 = C()
c1.getSize()
10
c1.x
10
c1.x = 18
c1.x
18
del c1.x
c1.size
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'C' object has no attribute 'size'

'''
