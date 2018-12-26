score = int(input('请输入一个分数：'))#和method2是一样的 只是改进 elif比较简洁  如果输入98 后面判断不会执行 节省CPU时间
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('C')
elif 60 > score >= 0:
    print('D')
else:
    print('输入错误！')