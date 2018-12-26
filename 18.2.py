'''

编写一个函数 findstr()，该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。
例如：假定输入的字符串为“You cannot improve your past, but you can improve your future.Once time is wasted, life is wasted.
，子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。



'''


def findstr(inputstr, objstr):
    count = 0
    length = len(inputstr)
    for i in range(length):
        if inputstr[i] == objstr[0] and inputstr[i + 1] == objstr[1]:
            count += 1
    print('子字符串在目标字符串中共出现 %d 次' % count)


inputstr = input('请输入目标字符串：')
objstr = input('请输入子字符串（两个字符）:')
findstr(inputstr, objstr)

'''

参考：
小甲鱼： 要加一个目标字符串中未找到的判断 再找
def findStr(desStr, subStr):
    count = 0
    length = len(desStr)
    if subStr not in desStr:
        print('在目标字符串中未找到字符串!')
    else:
        for each1 in range(length-1):      
            if desStr[each1] == subStr[0]:
                if desStr[each1+1] == subStr[1]:
                    count += 1
                    
        print('子字符串在目标字符串中共出现 %d 次' % count)
 
desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串(两个字符)：')
findStr(desStr, subStr)

网友的答案：


 def findstr():
	str1 = input('请输入目标字符串：')
	str2 = input('请输入子字符串（两个字符）：')
	count = 0
	for i in range(len(str1)-1):
		str3 = str1[i] + str1[i+1]
		if str3 == str2:
			count += 1
	print('子字符串在目标字符串中共出现%s次'%count)




'''
