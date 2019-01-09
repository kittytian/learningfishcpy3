#33 try except的一个知识点： 处理文件不存在异常 用except捕获多个异常
try:
    sum = 1 + '1'
    f = open('我为什么是一个文件.txt')  # 文件不存在 filenotfounderror
    print(f.read())
    f.close()
except (OSError, TypeError): #将多个异常变成一个元祖
    print('出错啦')

