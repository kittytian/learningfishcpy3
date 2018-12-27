#写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345) ==> [1, 2, 3, 4, 5]

result = []                                                #result初始化空列表，大神都喜欢初始化为空。
def get_digits(n):
        if n > 0:
                result.insert(0, n%10)                #这里使用insert插入符，12345%10 求余除，结果为5;  二次循环1234%10，结果为4；  三次循环123%10，结果为3；
                                                                #四次循环12%10，结果为2；  五次循环1%10，结果为1;   六次循环n值为0，跳出。

                get_digits(n//10)                        #get_digits函数经过整除后，结果为1234，也就是get_digits(1234)；   二次循环结果get_digits(123)；
                                                                #三次循环结果get_digits(12)；   四次循环结果get_digits(1)；   五次循环get_digits(0)

get_digits(12345)                                        #实际结果应该是从第五次循环结果为1开始，依次往回插入，也就是结果[1,2,3,4,5]
print(result)

