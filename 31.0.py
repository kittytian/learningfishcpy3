'''
编写一个程序，这次要求使用pickle将文件（  record.txt (1.1 KB, 下载次数: 3561) ）里的对话按照以下要求腌制成不同文件
（没错，是第29讲的内容小改，考考你自己能写出来吗？）：
小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件
（提示：文件中不同的对话间已经使用“==========”分割）


'''
import pickle

def save_file(boy, girl, count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'wb') #一定别忘了加b二进制！！
    girl_file = open(file_name_girl, 'wb')

    # pickle.dump(data, file) # 第一个参数是待存储的数据对象，第二个参数是目标存储的文件对象，注意要先使用'wb'的模式open文件哦^_^
    pickle.dump(boy, boy_file)
    pickle.dump(girl, girl_file)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    f = open(file_name, encoding='gbk')
    boy = []
    girl = []  # 这两个列表存放小甲鱼和小客服的话

    count = 1  # else语句把文件分别保存 所以要有个计数器

    for each_line in f:
        if each_line[:6] != '======':  # 判断前6个是不是等号 不需要把所有=都敲上去
            # 有一个问题 ！按等号划分运行后 第三段对话没有保存
            (role, line_spoken) = each_line.split(':', 1)  # 进行字符串分割操作
            #(role, line_spoken)这是一个元组，接受两个值。指定为1将字符串分割为2部分，
            # 刚好。不指定的话，无法对应值。

            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)

        else:  # 文件的分别保存操作
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1  # 要对列表重新初始化 下次count计数变成2

            # 别忘了关闭文件！！
    # 退出循环后保存第3段对话
    save_file(boy, girl, count)

    f.close()

split_file('record.txt')