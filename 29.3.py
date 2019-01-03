'''

呃，不得不说我们的用户变得越来越刁钻了。要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。
（如输入13:21打印第13行到第21行，输入:21打印前21行，输入21:则打印从第21行开始到文件结尾所有内容）

这个参考小甲鱼老师的写
自己不会的点 strip（）
要模仿（row，linespoken）那样写 （begin，end）提示不同文字 从开始到第几行 全文 从第几行到末尾
begin 和 end 是字符串类型！！ 是输入的字符串分割后的
有一个需要注意的 末尾设置成-1了 所以要判断行数<0就是第几行到末尾
第几行到末尾的时候要先消耗从头 到begin第几行 再print（第几行到第几行也是）
'''

def file_views(file_name, linesnum):
    if linesnum.strip()==':':#要去掉linesnum的空格(我觉得是中英文格式 中文'：' 英文':'
        begin = '1'
        end = '-1'

    (begin, end) = linesnum.split(':')
    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'
    if begin == '1' and end == '-1':
        prompt = '的全文'
    elif begin == '1':
        prompt ='从开始到第%s行' % end
    elif end == '-1':
        prompt = '从第%s行到末尾' % begin
    else:
        prompt = '从第%s行到第%s行' %(begin, end)

    print('\n文件%s%s的内容如下：\n' % (file_name, prompt))

    f = open(file_name)
    begin = int(begin)
    end = int(end)
    lines = end - begin + 1

    for i in range(begin-1): #消耗之前的几行
        f.readline()

    if lines < 0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline())

    f.close()

file_name = input(r'请输入要打开的文件（C:\\test.txt）')
linesnum = input('请输入需要显示的行数【格式如13：21 或 ：21 或13：】')
file_views(file_name, linesnum)

