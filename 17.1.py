'''
编写一个函数，利用欧几里得算法https://baike.baidu.com/item/%E8%BE%97%E8%BD%AC%E7%9B%B8%E9%99%A4%E6%B3%95
求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数。
'''

def gcd(x, y):
    if x % y != 0:
        return gcd(y, x % y)
    else:
        return y

print(gcd(123456,7890))

'''
参考:
def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t

    return x
    
print(gcd(4, 6))
'''