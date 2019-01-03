#编写一个程序，实现“全部替换”功能，程序实现如图
#别忘了 字符串  replace(old, new[, count])           　　　　
#  把字符串中的 old 子字符串替换成 new 子字符串，如果 count 指定，则替换不超过 count 次
#思路 每行每行的遍历 找到替换的单词 replace后 换过的行和没换过的全存到一个列表里 然后 文件用writelines重新写入
def file_replace(file_name, origin, replace):
    count = 0 #计数替换的单词数
    content = []#空列表 为了写入用
    f_read = open(file_name)
    for eachline in f_read:
        if origin in eachline: # 判断需要改的字符串或单词是否在这一行中
            count1 = eachline.count(origin)# 每行中需要改的字符串的个数
            eachline = eachline.replace(origin, replace) # 改字符串
            count += count1 # 自加每行的个数
        content.append(eachline)    # 加到列表中去

    decide = input('\n文件中共有%s个【%s】\n您确定要把所有的【%s】替换成【%s】吗？\n[YES/NO]:' % (count, origin, origin, replace))
    if decide == 'YES' or 'yes':
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()
        print('更改成功')
    else:
        print('不更改')
    f_read.close()

file_name = input('请输入文件名：')
origin = input('请输入要替换的单词或字符：')
replace = input('请输入新的单词或字符：')
file_replace(file_name, origin, replace)