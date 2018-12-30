#要求去除列表[1,2,3,4,5,5,3,1,0]中重复的元素
'''
list1 = [1,2,3,4,5,5,3,1,0]
temp = []
for each in list1:
    if each not in temp:
        temp.append(each)
print(temp)
'''
'''
方法二：
list1 = [1,2,3,4,5,5,3,1,0]
temp = list1[:]
list1.clear()
for each in temp:
    if each not in list1:
        list1.append(each)

print(list1)
'''



list1 = [1,2,3,4,5,5,3,1,0]
list1 = list(set(list1))

print(list1)#会打印[0, 1, 2, 3, 4, 5] 顺序变了 得到的是无序的