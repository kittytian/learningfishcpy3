#编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）
# 所有含有该关键字的文本文件（.txt后缀），
# 要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符），程序实现如图：
#参考小甲鱼的 下面这几个函数没用过：要注意一下 sorted之前用过 不熟
#walk(top)   遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件]) 类似下面这样：
# 【<class 'tuple'>: ('/Users/kittytian/PycharmProjects/xiaojiayu', ['venv', '.git', '.idea'], ['hello.py', '10.2.1.py'])
# 具体实现方案请看：第30讲课后作业^_^】
#字符串：find(sub[, start[, end]])            　　　　　 检测 sub 是否包含在字符串中，如果有则返回索引值，否则返回 -1，start 和 end 参数表示范围，可选。
#sorted（）方法用于返回一个排序的列表，大家还记得列表的内建方法sort（）吗？它们的实现效果是一样的，但列表的内建方法sort（）是实现列表原地排序；而sorted（）是返回一个排序后的新列表。
# os.path.join（）用于将路径名和文件名组合成一个完整的路径： 自己加C:\\ 反斜杠 或者写r
import os


def print_pos(key_dict):  #打印及排序字典函数   key_dict即是 处理好的，关键字所在的行数，和每行出现次数的字典
    keys = key_dict.keys()
    keys = sorted(keys)  # 由于字典是无序的，我们这里对行数进行排序
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key])))


def pos_in_line(line, key):   #处理关键字所在行数出现次数函数，文本的一行，关键字 处理关键字在一行出现次数返回一个pos列表
    pos = []                  #新建列表
    begin = line.find(key)        #查找关键数字是否存在，不存在会返回-1的值
    while begin != -1:           #等于-1，则不执行循环
        pos.append(begin + 1)  # 用户的角度是从1开始数，编程才是从0开始
        begin = line.find(key, begin + 1)  # 从下一个位置继续查找

    return pos             #pos是存放了关键字在那行的位置的列表


def search_in_file(file_name, key):  #文本路径和，关键字，字典函数
    f = open(file_name, encoding ='gb18030',errors='ignore')            # 打开文件
    count = 0  # 记录行数
    key_dict = dict()  # 字典，用户存放key所在具体行数对应具体位置

    for each_line in f:   #历遍搜寻到的文本
        count += 1          #行数加一次
        if key in each_line:   #如果关键字在文本里面
            pos = pos_in_line(each_line, key) #调用函数处理关键字在一行出现次数返回一个pos列表          # key在每行对应的位置
            key_dict[count] = pos     #count位关键字行数，是key，pos是关键字在一行出现次数在是value。

    f.close()
    return key_dict


def search_files(key, detail):  #第一个函数，处理函数
    all_files = os.walk(os.getcwd())  #历遍当前目录返回三元组
    txt_files = []             #新建一个列表存放文本完整路径

    for i in all_files:    # 历遍三元组
        for each_file in i[2]:    #历遍第三个元组，file
            if os.path.splitext(each_file)[1] == '.txt':  # 根据后缀判断是否文本文件
                each_file = os.path.join(i[0], each_file)  #把完整路径赋予each_file  i[0]是历遍的路径
                txt_files.append(each_file)        #把路径添加到列表

    for each_txt_file in txt_files:     #历遍列表   each_txt_file等于完整的txt文本路径
        key_dict = search_in_file(each_txt_file, key)   #调用函数，赋值
        if key_dict:
            print('================================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
            if detail in ['YES', 'Yes', 'yes']:
                print_pos(key_dict)     #调用函数


key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
search_files(key, detail)
