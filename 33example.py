#33 try except例子 处理文件不存在异常

'''
Traceback (most recent call last):
  File "/Users/kittytian/PycharmProjects/xiaojiayu/33example.py", line 2, in <module>
    f = open('我为什么是一个文件.txt')#文件不存在 filenotfounderror
FileNotFoundError: [Errno 2] No such file or directory: '我为什么是一个文件.txt'
'''
try:
    #int('abc') 后面except异常没有 出错 就报错了
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')  # 文件不存在 filenotfounderror
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦\n错误的原因是：' + str(reason))
except TypeError as reason:
    print('类型出错啦\n错误的原因是：' + str(reason))


#as reason reason是个变量名 错误的原因

#到sum出错 就抛出异常 后面文件出错就不走了
'''
可以这样做 碰到异常 就打印 出错啦（不推荐）
try:
    int('abc') 
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')  # 文件不存在 filenotfounderror
    print(f.read())
    f.close()
except:
    print('出错啦')

'''