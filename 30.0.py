#编写一个程序，统计当前目录下每个文件类型的文件数，程序实现如图：
#思路 创建一个空字典 key存文件类型 value存个数 listdir当前目录下所有文件 遍历
#要会用字典的一些函数
import os
files = os.listdir(os.curdir)
filetype = dict()
for eachfile in files:#判断一下是不是路径 是的话存成文件夹 不是的话就是后缀
    if os.path.isdir(eachfile):
        filetype.setdefault('文件夹', 0)
        filetype['文件夹'] += 1 #设置键和值 这个要会！
    else:
        temp = os.path.splitext(eachfile)[1]
        filetype.setdefault(temp, 0)
        filetype[temp] += 1
#for each in type:
    #print(type.items())
for each in filetype.keys(): #要会遍历字典的方式
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each, filetype[each]))
