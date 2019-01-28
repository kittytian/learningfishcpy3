'''
0. 小李做事常常丢三落四的，写代码也一样，常常打开了文件又忘记关闭。
你能不能写一个 FileObject 类，给文件对象进行包装，从而确认在删除对象时文件能自动关闭？
'''
class FileObject:
    def __init__(self, filename='sample.txt'):
        self.file = open(filename, 'r+') #这个地方要注意 以读写模式打开
    def __del__(self):
        self.file.close()
        del self.file

