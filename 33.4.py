'''
把文件关闭放在 finally 语句块中执行还是会出现问题，像下边这个代码，
当前文件夹中并不存在"My_File.txt"这个文件，那么程序执行起来会发生什么事情呢？你有办法解决这个问题吗？
try:
    f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    f.close()
这个修正方法也没想到 参考答案：

答：由于finally语句块里试图去关闭一个并没有成功打开的文件，因此会弹出错误内容如下：
Traceback (most recent call last):
  File "/Users/kittytian/PycharmProjects/xiaojiayu/33.4.py", line 24, in <module>
    f.close()
NameError: name 'f' is not defined

使用locals(),locals()是当前局部变量符号表
如果f成功打开，则f就会在locals()内；直接判断f是否在locals()内即可

'''


try:
    f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
    print(f.read())
except OSError as reason:
    print('出错啦：' + str(reason))
finally:
    if 'f' in locals():# 如果文件对象变量存在当前局部变量符号表的话，说明打开成功
        f.close()