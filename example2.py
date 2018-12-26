for i in range(10):#range默认从0开始
    if i % 2 != 0:
        print(i)#奇数打印出来 continue不执行 i+2和 print（i）跳到for开始对位置
        continue
    i += 2
    print(i)
