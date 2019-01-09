'''
try finally 例子

try:
	检测范围
except Exception[as reason]:
	出现异常（Exception）后的处理代码
finally:
	无论如何都会被执行的代码

'''
try:
    f = open('我为什么是一个文件.txt', 'w')  # 文件不存在 filenotfounderror
    print(f.write('我存在了！'))
    sum = 1 + '1'
   # f.close()
except (OSError, TypeError): #将多个异常变成一个元祖
    print('出错啦')
finally:
    f.close()



#实际上并没有写入 因为 f没有close 所以用finally语句就可以close 这个文件就会写入我存在了！