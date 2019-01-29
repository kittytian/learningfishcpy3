'''
按要求编写描述符 Record：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件：record.txt
程序实现如下：

#>>> class Test:
        x = Record(10, 'x')
        y = Record(8.8, 'y')

#>>> test = Test()
#>>> test.x
10
#>>> test.y
8.8
#>>> test.x = 123
#>>> test.x = 1.23
#>>> test.y = "I love FishC.com!"
#>>>
产生文件：record.txt

答：这道题考察的点比较多，例如字符串的转换、文件的操作、time 模块的用法、描述符……大家哪里不会补哪里~
注意用ctime（） 我之前用的是perf_counter
自己的问题 注意一下 set后面应该是str（value）

'''
import time as t

class Record:
    def __init__(self, var_val=None, name=None):
        self.val = var_val
        self.var_name = name
        self.file_name = 'record3.txt'

    def __get__(self, instance, owner): #以写入模式打开，如果文件存在，则在末尾追加写入
        with open(self.file_name, 'a',) as f:
            f.write('%s变量位于北京时间%s被读取,%s=%s\n' % (self.var_name, str(t.ctime()), self.var_name, str(self.val)))
        return self.val

    def __set__(self, instance, value):
        with open(self.file_name, 'a',) as f:
            f.write('%s变量位于北京时间%s被修改,%s=%s\n' % (self.var_name, str(t.ctime()), self.var_name, str(value)))
            self.val = value

class Test:
    x = Record(10, 'x')
    y = Record(8.8, 'y')

test = Test()
test.x
test.y
test.x = 123
test.y = "I love FishC.com!"
