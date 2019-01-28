'''
1. 编写 Demo 类，使得下边代码可以正常执行：
#>>> demo = Demo()
#>>> demo.x
'FishC'
#>>> demo.x = "X-man"
#>>> demo.x
'X-man'
自己写的时候写成__getattribute__方法了
__ getattr__(self, name)	定义当用户试图获取一个不存在的属性时的行为
__ getattribute__(self, name)	定义当该类的属性被访问时的行为

'''
class Demo:
    def __getattr__(self, name):
        self.name = 'Fishc'
        return self.name

demo = Demo()
print(demo.x)
demo.x = 'love'
print(demo.x)
