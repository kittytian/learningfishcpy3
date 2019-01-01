'''

编写一个程序，比较用户输入的两个文件，
如果不同，显示出所有不同处的行号与第一个不同字符的位置，程序实现如图：
~~~~(>_<)~~~~ 要学着自己有参考代码这种思路呀！！ 用函数！！！
'''
def file_compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0 #统计行数
    differ = [] #存不同行的数字

    for line1 in f1:
        line2 = f2.readline()
        count += 1    #特别是这里！！！一定要想到呀
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()

    return differ




file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')
differ = file_compare(file1, file2)
if len(differ) == 0:
    print('两个文件一样！')
else:
    print('两个文件有 %d 处不同 ' % len(differ))
    for each in differ:
        print('第 %d 行不一样' % each)