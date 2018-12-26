'''
设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内

'''
count = 3
realpassword = 'FishC.com'
while count > 0:
    password = input('请输入密码： ')
    if password == realpassword:#记住 判断是双等于！！
        print('密码正确，进入程序')
        break
    elif '*' in password:
        print('密码中不能含有星号！您还有', count, '次机会!', end=' ')#count要这么写
        continue
    else:
        count -= 1
        print('密码输入有误！您还有', count, '次机会!', end=' ')
        continue

'''
我们先根据运行截图进行程序的分析：
1.在开始和用户输入错误的情况下，都有一个“请输入密码”的字样，且都在说明文字的末尾，证明“请输入密码”这段文字可重复应用，可以在while循环里，用continue语句实现。
2.根据题目要求，如果用户输入的内容中包含"*"则不计算在可输入错误的三次机会内，我们想到的是每次输入后，次数减去一，在含*语句的判断后，打印出的语句 次数加1 就实现了要求。
但感觉复杂了，这里其实依旧可以用continue语句实现，终止本次循环，进入下一次循环，次数减一的语句放在continue后面就好。
3.这里肯定要用到条件分支语句，先判断输入正确，还是输入错误，都可以，提议像小甲鱼一样先易后难，先判断输入正确，这样程序看起来更加的简洁，也符合通常的逻辑。

复制代码
count = 3
password = 'FishC.com'

while count:
    passwd = input('请输入密码：')
    if passwd == password:
        print('密码正确，进入程序......')
        break
    elif '*' in passwd:
        print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有', count-1, '次机会！', end=' ')    
    count -= 1
复制代码
 或者这样写：

复制代码
password = "FishC.com"
times = 3
passwd = 0
while passwd != password and times：#这里大可改成while times:  只是要掌握这种用法 前面提到过
    passwd = input("请输入密码：")
    if '*' in passwd:
        print("密码中不能含有*号！您还有"+str(times)+"机会",end=" ")
        continue
    elif passwd != password:
        print("密码输入错误！您还有"+ str(times-1) +"机会",end=" ")
    else:
        print("密码正确，进入程序...")
    times -= 1
复制代码
这里有个关于字符串的问题需要提出：

times=3
一、print("密码中不能含有*号！您还有"+times+"机会",end=" ")
二、print("密码中不能含有*号！您还有"+str(times)+"机会",end=" ")
三、print("密码中不能含有*号！您还有"，times，"机会",end=" ")

第一种报错，第二三种能运行。能解释下其中的原理吗？第二三种有何区别？

答：1.字符串和整型不能相加。
2.把times转换成字符串再拼接。
3.print可以有多个参数，参数可以有任何类型（假如不可打印的话就输出对象，最后这些参数都会被转换成字符串）， print会把转换后的东西拼接在一起的再输出。


'''





