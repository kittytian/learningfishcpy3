'''
猜想一下 min() 这个BIF的实现过程
'''
min = list1[0]
for each in list1:
    if each < min:
        min = each
return min

'''


def min(x):
    least = x[0]

    for each in x:
        if each < least:
            least = each

    return least

print(min('123456789'))
'''