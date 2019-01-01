'''

任务：将文件（record.txt）中的数据进行分割并按照以下规律保存起来：
（1）小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
（2）小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”） 思路：
小客服的话 变量：line_spoken 存到一个列表中

split(sep=None, maxsplit=-1)             　　
　不带参数默认是以空格为分隔符切片字符串，如
果 maxsplit 参数有设置，则仅分隔 maxsplit 个子字符串，返回切片后的子字符串拼接的列表。

（3）文件中总共有三段对话，分别保存为
boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件
（提示：文件中不同的对话间已经使用“==========”分割）

'''

f = open('record.txt', encoding='gbk')
boy = []
girl = []#这两个列表存放小甲鱼和小客服的话

count = 1 #else语句把文件分别保存 所以要有个计数器

for each_line in f:
    if each_line[:6] != '======':#判断前6个是不是等号 不需要把所有=都敲上去
                                 #有一个问题 ！按等号划分运行后 第三段对话没有保存
        (role, line_spoken) = each_line.split(':',1)#进行字符串分割操作
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)

    else:#文件的分别保存操作
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        #把存对话的boy girl 列表写入文件 列表有很多字符串 （字符串序列）把序列写入 用writelines
        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1 #要对列表重新初始化 下次count计数变成2

        #别忘了关闭文件！！
#退出循环后保存第3段对话
file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'

boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()

f.close()








