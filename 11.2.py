list1 = ['1.JUST do it', '2.一切皆有可能', '3.让编程改变世界', '4.Impossible is Nothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.FISHC', '1.耐克']
list3 = []
for solgan in list1:
    for name in list2:
        if solgan[0] == name[0]:
            list3.append(name + ':' + solgan[2:])
print(list3)
for each in list3:
    print(each)

'''
这个程序得会写 运用切片 拼接 solgan 和 name 是列表里的成员 solgan[0] 还得知道索引 就是数字
1.	>>> list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
'''

