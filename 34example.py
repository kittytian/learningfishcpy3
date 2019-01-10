'''
else语句还能跟刚刚学的异常处理进行搭配，实现跟与循环语句搭配差不多：
只要try语句块里没有出现任何异常，那么就会执行else语句块里的内容了。
'''
try:
    #int('abc')#会报错 传进去的值是错的 报valueerror else不会执行
    int('123') #执行else
    print(int('123'))
except ValueError as reason:
    print('出错啦：' + str(reason))
else:
    print('没有任何异常')