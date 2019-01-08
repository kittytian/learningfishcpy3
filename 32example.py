#异常--关于文件的例子
file_name = input('请输入需要打开的文件名:')
f = open(file_name)
print('文件的内容是：')
for each_line in f:
    print(each_line)
f.close()
'''
请输入需要打开的文件名:README
Traceback (most recent call last):
  File "/Users/kittytian/PycharmProjects/xiaojiayu/32example.py", line 3, in <module>
    f = open(file_name)
FileNotFoundError: [Errno 2] No such file or directory: 'README' 这就是异常的一个例子 找不到文件

'''