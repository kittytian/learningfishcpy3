'''
method 1
;假设给定以下列表：

member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']

要求将列表修改为：

member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

方法一：使用 insert() 和 append() 方法修改列表。

'''
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member.insert(1, 88)
member.insert(3, 90)
member.insert(5, 85)
member.insert(7, 90)
member.append(88)#或者写成 member.insert(9,88)也可以
print(member)

