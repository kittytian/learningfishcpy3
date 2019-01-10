'''
1. 按照以下提示尝试定义一个矩形类并生成类实例对象。
属性：长和宽
方法：设置长和宽 -> setRect(self)，获得长和宽 -> getRect(self)，获得面积 -> getArea(self)
提示：方法中对属性的引用形式需加上 self，如 self.width

程序截图：

'''
class Rectangle:
    length = 0
    width = 0

    def setRect(self):
        print('请输入矩形的长和宽:')
        self.length = float(input('长：'))
        self.width = float(input('宽：'))

    def getRect(self):
        print('这个矩形的长是 %.2f，宽是 %.2f' % (self.length, self.width))

    def getArea(self):
        area = self.length * self.width
        print(area)

'''
class Rectangle:
    length = 5
    width = 4 #(⊙﹏⊙)b程序里初始值是这个
    
    def setRect(self):
        print("请输入矩形的长和宽...")
        self.length = float(input('长：'))
        self.width = float(input('宽：'))
 
    def getRect(self):
        print('这个矩形的长是：%.2f，宽是：%.2f' % (self.length, self.width))
        
    def getArea(self):
        return self.length * self.width #用return 就行

'''