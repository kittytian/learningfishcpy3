'''
请恢复以下代码中马赛克挡住的内容，使得程序执行后可以按要求输出
答：这道题比较考脑瓜，你想到了吗？
没想到 根据输出 用 raise keyboardinterrupt
'''
try:
    for i in range(3):
        for j in range(3):
            # 被挡住的内容
            if i == 2:
                raise KeyboardInterrupt
            #被挡住的内容
            
            print(i,j)
except KeyboardInterrupt:
    print('退出啦')
