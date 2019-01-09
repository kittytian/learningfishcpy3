'''
2. 尝试一个新的函数 int_input()，当用户输入整数的时候正常返回，否则提示出错并要求重新输入。%
程序实现如图：

请教1:
    int_input("请输入一个整数：")  这一句括号里的即是一个形参又是一个输入？为什么？

这一句的括号里不是形参，是实参，传递给了int_input函数
它并不是一个输入，能够作为输入是因为int_input函数中调用了input函数，才有了输入的功能

请教2:
    def int_input(prompt=''):  这里的我用（prompt）和（prompt=''）的结果是一样的，他们有区别吗？如果是（prompt=''）的话是什么意思？
第一种(prompt)并没有指定形参的默认值，这样在调用int_input函数时必须带参数，将该参数赋值给了prompt
第二种（prompt=''）指定了形参的默认值为空''，这种情况下在调用int_input函数时可以不写参数，比如
a = int_input()，

设置默认参数可以避免调用函数时没有给指定参数传值而引发的错误。
你可以尝试把def int_input(prompt='')和def int_input(prompt)两种情况下调用:
x=int_input()
如果没有设置默认参数，程序会报错。



def int_input(prompt=''):
这个就是定义一个函数，名字是int_input，调用这个函数的时候要传入一个参数，这个参数有个名字是prompt，而且规定了默认值为“空”

int(input(prompt))
里面的prompt就是刚才函数定义时传入的变量，然后对这个变量转换成int类型，如果是数字就直接跳出循环了，如果不是数字，会报一个ValueError，然后打印“出错，您输入的不是整数！”

'''
def int_input(prompt = ''):
    while True:
        try:
            int(input(prompt))
            break
        except ValueError:
            print('出错！您输入的不是整数')

int_input('请输入一个整数：')




