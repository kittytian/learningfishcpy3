'''
0. 按照以下提示尝试定义一个 Person 类并生成类实例对象。
属性：姓名（默认姓名为“小甲鱼”）
方法：打印姓名
提示：方法中对属性的引用形式需加上 self，如 self.name
'''
class Person:
    #属性：姓名（默认姓名为“小甲鱼”）
    name = '小甲鱼'
    #方法：打印姓名
    def print_name(self):
        print(self.name)