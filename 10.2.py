'''
2. 上一题打印的样式不是很好，能不能修改一下代码打印成下图的样式呢？【请至少使用两种方法实现】
'''
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for i in member:
    if type(i) == str:
        print(i, end=' ')
    else:
        print(i)

'''
参考：
方法一：
count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1])
    count += 2

方法二：    
    
for each in range(len(member)):
    if each%2 == 0:
        print(member[each], member[each+1])


小甲鱼 88
黑夜 90
迷途 85
怡静 90
秋舞斜阳 88
们来分析下：题目要求是要将每个名字跟对应的成绩打印在同一行。
我们来看看，第一列全是名字，索引值依此是0，2，4，6，8，
同理第二列的成绩全是奇数，索引值依此是1，3，5，7，9.不由得让人想到了判断奇偶数的%，
另外，要呈现print（number[x],number[x+1])的结果，里面的第一个索引值可以依赖for循环的range（）内建函数，加上奇偶的判断实现。 
方法一是通过while循环，每次循环加2。同样的原理。
值得注意的一点是这里 range（）内建函数的 each的值不会受到 循环体内 range变量变化的影响。
'''