'''
编写代码，将上一题中的文件（OpenMe.mp3）保存为新文件（OpenMe.txt）
'''
f1 = open('OpenMe.mp3', encoding ='gb18030',errors='ignore')
f2 = open('OpenMe.txt', 'w')
f2.write(f1.read())
f1.close()
f2.close()

'''
小甲鱼参考！ x也是写入模式！！！
f1 = open('OpenMe.mp3')
f2 = open('OpenMe.txt', 'x')        # 使用”x”打开更安全
f2.write(f1.read())
f2.close()
f1.close()


'''