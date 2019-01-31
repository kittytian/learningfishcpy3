'''

1. 10 以内的素数之和是：2 + 3 + 5 + 7 = 17，那么请编写程序，计算 2000000 以内的素数之和？
答：如果你的策略是将 2000000 以内的所有素数找到并存放到一个列表中，再依次进行求和计算，那么这个列表极有可能会撑爆你的内存。所以这道题就必须用到生成器来实现啦。

详细解释请参考：解释 yield 和 Generators（生成器）
https://blog.csdn.net/qq_41556318/article/details/84885831

结果是 142913828922，你答对了吗？！

判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数

如果是直接运行的程序则__name__的值为"__main__"
如果是import导入的程序则__name__的值为模块名。
这是为了区分是否直接执行程序的方法，主要用在模块中。
'''
import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2): #2,3,5,7填进去都会导致数列第一个元素小于等于数列最后一个元素-1，就会生成一个空的可送代对象
                                                           # 这样会导致for循环不会执行哪怕一次，因为没有元素可以送代。
            if number % current == 0:
                return False
        return True
    return False


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def solve():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return


if __name__ == '__main__':
    solve()


