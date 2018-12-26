'''
哎呀呀，现在的小屁孩太调皮了，邻居家的孩子淘气，把小甲鱼刚写好的代码画了个图案，
麻烦各位鱼油恢复下啊，另外这家伙画的是神马吗？怎么那么眼熟啊！？？
自己写的时候注意点 循环 还有判断！！一定要细心 会写

'''
name = input('请输入待查找的用户名:')
score = [['米兔', 85], ['黑夜', 80], ['小布丁', 65], ['娃娃', 95], ['意境', 90]]
flag = False
for each in score:#遍历
    if name in each:
        print(name + '的得分是:', each[1])
        flag = True
        break
if flag == False:
    print('查找的用户不存在')