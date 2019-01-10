'''
Python提供了一个with语句，利用这个语句抽象出文件操作中频繁使用的try/except/finally相关的细节。
对文件操作使用with语句，将大大减少代码量，而且你再也不用担心出现文件打开了忘记关闭的问题了
（with会自动帮你关闭文件）with 语句会自动处理文件的打开和关闭，如果中途出现异常，会执行清理代码，然后确保文件自动关闭。
 你可以换一种形式写出下边的伪代码吗？
with A() as a:
    with B() as b:
        suite
答：with 语句处理多个项目的时候，可以用逗号隔开写成一条语句

with A() as a, B() as b:
    suite
'''
try:
    #f = open('data.txt', 'w')
    with open('data.txt', 'w') as f: #改成with 可以自动调用f.close
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错啦：' + str(reason))
#finally:
   # f.close() #关闭不存在的文件对象 33课后题可以处理