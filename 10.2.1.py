'''
2. 上一题打印的样式不是很好，能不能修改一下代码打印成下图的样式呢？【请至少使用两种方法实现】
'''
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
length = len(member)
for i in range(0,length):
    if i % 2 == 0:
        print(member[i],end= ' ')
    else:
        print(member[i])
