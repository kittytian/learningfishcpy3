'''
0. 编写一个程序，接受用户的输入并保存为新的文件，程序实现如图：

'''

file_name = input('请输入文件名:')
f = open(file_name, 'w')
print('请输入内容【单独输入‘：w’保存退出】：')
while True:
    write_content = input()
    if write_content != ':w':
        f.write('%s\n' % write_content)
        #改成这样 才能换行！！！！！没有\n 不换行
        #f才是file obj 不能写成file_name.write
    else:
        break
f.close()

'''
写成函数！
def file_write(file_name):
    f = open(file_name, 'w')
    print('请输入内容【单独输入\':w\'保存退出】：')
 
    while True:
        write_some = input()
        if write_some != ':w':
            f.write('%s\n' % write_some) 这句！！
        else:
            break
 
    f.close()
 
file_name = input('请输入文件名：')
file_write(file_name)

'''