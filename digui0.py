#十进制转换二进制。
def Dec2Bin(dec):
    result = ''  # result定义一个初始化的空字符串

    if dec:  # 老师定义的数字62太高端大气上档次了，我就简化个十进制的10，二进制是1010，也比较好举例子；
        # if dec表示dec不为零时，为零时返回值给result。

        result = Dec2Bin(dec // 2)  # 函数调用赋值实参10的时候，这里的结果应该是 result = Dec2Bin(10//2)；
        return result + str(dec % 2)  # return =Dec2Bin(10//2) + str(10%2) =Dec2Bin(5)+str(0)；
        #        从Dec2Bin(5)返回的是Dec2Bin(2)+str(5%2)=Dec2Bin(2)+str(1);
        #        从Dec2Bin(2)返回的是Dec2Bin(1)+str(2%2) =Dec2Bin(1)+str(0);
        #        从Dec2Bin(1)返回的是Dec2Bin(0) +str(1%2)= 0+str(1)  (这里Dec2Bin为0，执行的else语句)
    else:
        return result


print(Dec2Bin(10))  # 所以Dec2Bin(10) = 从末尾开始往回返倒序的“1010”
