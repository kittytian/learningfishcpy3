# 编写一个程序 计算当前文件夹下所有文件的大小
import os

all_files = os.listdir(os.curdir)  # 使用os.curdir表示当前目录更标准
file_dict = dict()

for each_file in all_files:
    if os.path.isfile(each_file):#判断文件是否存在且是文件
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size

for each in file_dict.items():#每一项 打印第0项key和第1项value
    print('%s【%dBytes】' % (each[0], each[1]))
