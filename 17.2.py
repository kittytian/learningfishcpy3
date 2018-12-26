'''
编写一个将十进制转换为二进制的函数，要求采用“除2取余”https://baike.baidu.com/item/%E5%8D%81%E8%BF%9B%E5%88%B6%E8%BD%AC%E4%BA%8C%E8%BF%9B%E5%88%B6
的方式，结果与调用bin()一样返回字符串形式。
'''

def dectobin(x):
    str1 = []
    result = '' #必须要提前声明是字符串
    while x:
        yushu = x % 2
        x = x // 2
        str1.append(yushu)
        str1.reverse()
    for each in str1:
        result += str(each)
    return result




print(dectobin(100))


'''
参考 可用pop逆序
def Dec2Bin(dec):
    temp = []
    result = ''
    
    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)

    while temp:
        result += str(temp.pop())
    
    return result

print(Dec2Bin(62))
'''
