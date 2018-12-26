'''
按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，自动转换为ABCD的形式打印。
解题方案：
method1.py
method2.py
method3.py

'''
score = int(input('请输入一个分数：'))
if 100 >= score >= 90: #若输入98 这句执行打印A 但后面if是并列条件 打印完还会继续执行
    print('A')
if 90 > score >= 80:
    print('B')
if 80 > score >= 60:
    print('C')
if 60 > score >= 0:
    print('D')
if score < 0 or score > 100:
    print('输入错误！')
