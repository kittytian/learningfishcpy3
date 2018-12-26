'''
0. 编写一个函数，判断传入的字符串参数是否为“回文联”
（回文联即用回文形式写成的对联，既可顺读，也可倒读。例如：上海自来水来自海上）


'''

def huiwen(inputstr):
    flag = 0
    length = len(inputstr)
    for i in range(length):
        if inputstr[i] == inputstr[length-1-i]:
            flag = 1
        else:
            flag = 0
    if flag == 1:
        print('是回文联！')
    else:
        print('不是回文联！')




inputstr = input('请输入一句话：')
huiwen(inputstr)

'''
参考：
别忘了list可以转换为列表：reversed（sequence）
reversed（）方法用于返回逆向迭代序列的值。
同样的道理，实现效果跟列表的内建方法reserse（）一致。
区别是列表的内建方法是原地翻转，而reversed（）是返回一个翻转后的迭代器对象。你没看错，它不是返回一个列表，是返回一个迭代对象

方法二：
def palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return '是回文联!'
    else:
        return '不是回文联！'
print(palindrome('上海自来水来自海上'))

方法一：
def palindrome(string):
    length = len(string)
    last = length-1
    length //= 2
    flag = 1
    for each in range(length):
        if string[each] != string[last]:
            flag = 0
        last -= 1
 
    if flag == 1:
        return 1
    else:
        return 0
 
string = input('请输入一句话：')
if palindrome(string) == 1:
    print('是回文联!')
else:
    print('不是回文联！')




'''