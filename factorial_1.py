'''
写一个求阶乘的函数
---正整数阶乘指从1乘以2乘以3乘以4一直乘到所要求的数。
---例如所给的数是5，则阶乘式是1×2×3×4×5，得到的积是120，所以120就是4的阶乘
以下是非递归版本
'''

def factorial(n):
    result = n #注意初始值是n
    for i in range(1, n): #因为范围是1到n-1 
        result *= i

    return result

number = int(input('请输入一个正整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number, result))