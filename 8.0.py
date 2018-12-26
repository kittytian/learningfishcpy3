'''
视频中小甲鱼使用 if elif else 在大多数情况下效率要比全部使用 if 要高，
但根据一般的统计规律，一个班的成绩一般服从正态分布，也就是说平均成绩一般集中在 70~80 分之间，
因此根据统计规律，我们还可以改进下程序以提高效率。
按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，自动转换为ABCD的形式打印。
'''
score = int(input('输入分数： '))
if 60 <= score <= 80:
    print('C')
elif 90 <= score <= 100:
    print('A')
elif 80 <= score <= 90:
    print('B')
elif 0 <= score <= 60:
    print('D')
else:
    print("输入有误！")
'''
1.	score = int(input('请输入一个分数：'))
2.	if 80 > score >= 60:
3.	    print('C')
4.	elif 90 > score >= 80:
5.	    print('B')
6.	elif 60 > score >= 0:
7.	    print('D')
8.	elif 100 >= score >= 90:
9.	    print('A')
10.	else:
11.	    print('输入错误！')

'''