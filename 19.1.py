'''
1. 编写一个函数count，分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其它字符的个数。
程序执行如图
偷看了一眼参考 等于空格 用字符串 == ‘’判断
英文字母 用 isalpha()
多个参数 params【i】记得遍历 params！！
print那句 %前不要加逗号 注意语法！！！
'''

def count(*params):
    length = len(params)
    for i in range(length):
        letter = 0
        space = 0
        digit = 0
        other = 0
        for each in params[i]:
            if each.isalpha():
                letter += 1
            elif each.isspace():
                space += 1
            elif each.isdigit():
                digit += 1
            else:
                other += 1
        print('第 %d 个字符串共有：英文字母 %d 个, 数字 %d 个, 空格 %d 个, 其他字符 %d 个.' % (i + 1, letter, digit, space, other))



count('i love you', 'taq love gym')

