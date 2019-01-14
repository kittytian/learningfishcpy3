'''
 定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特性的数据结构。
至少需要有以下方法：
方法名	含义
isEmpty()	判断当前栈是否为空（返回 True 或 False）
push()	往栈的顶部压入一个数据项
pop()	从栈顶弹出一个数据项（并在栈中删除）
top()	显示当前栈顶的一个数据项
bottom()	显示当前栈底的一个数据项

参考小甲鱼 写 把stack当成一个列表【】

1.在类实例化时，如果没有输入参数，则默认为空列表
2.把栈想象成货物一层压一层，先放上的是[0], 再其后是1，2，3...，最上面是是-1
'''
class Stack:
    def __init__(self, start=[]): #start=[] 允许初始栈有元素，例如stack1 = Stack([1,2,3])
        self.stack = []
        for x in start:
            self.push(x)#这个地方使用了迭代器，start是个列表，用for x in start 每次循环会把start中的一个元素读出来赋值给x，直到元素全部读取完毕才终止循环，然后调用push方法入栈

    def isEmpty(self):
        return not self.stack


    def push(self, obj):
        self.stack.append(obj)

    def pop(self, obj):
        self.stack.pop(obj)

    def top(self):#要判断栈为空
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[-1] #1.在类实例化时，如果没有输入参数，则默认为空列表
     #2.把栈想象成货物一层压一层，先放上的是[0], 再其后是1，2，3...，最上面是是-1

    def bottom(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[0]

s = Stack([1,2,3,4,5])
print(s)
print(s.isEmpty())
print(s.push(9))




