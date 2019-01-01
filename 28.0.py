'''
尝试将文件（  OpenMe.mp3 ）打印到屏幕上
编码会报错 用b二进制读/写 或者 encoding ='gb18030',errors='ignore'可以
'''
#f = open('OpenMe.mp3', encoding ='gb18030',errors='ignore')
f = open('OpenMe.mp3', 'rb')
for eachline in f:
    print(eachline, end='')
f.close()