'''
编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上，程序实现如图：
看 自己也能写出来呀！ 注意一下 按文件名打开 要输入r
file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
'''

def read_nlines(filename, n_lines):
    f = open(filename)
    while n_lines:
        print(f.readline())
        n_lines -= 1
    f.close()



filename = input('请输入要打开的文件：')
n_lines = int(input('请输入需要显示文件前几行:'))
read_nlines(filename, n_lines)

'''
def file_view(file_name, line_num):
    print('\n文件%s的前%s的内容如下：\n' % (file_name, line_num))
    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline(), end= '')
 
    f.close()
 
file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
line_num = input('请输入需要显示该文件前几行：')
file_view(file_name, line_num)

'''



