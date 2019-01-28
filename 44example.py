'''
基本要求：
1>> 定制一个计时器的类
2>> start和stop方法代表启动计时和停止计时
3>> 假设计时器对象t1，print(t1)和直接调用t1均显示结果
4>> 当计时器未启动或已经停止计时，调用stop方法会给予温馨的提示
5>> 两个计时器对象可以进行相加：t1 + t2
6>> 只能使用提供的有限资源完成

1>> 使用time模块的localtime方法获取时间
　  【扩展阅读】：time 模块详解（时间获取和转换）
2>> time.localtime返回struct_time的时间格式
3>> 表现你的类：__str__ ()和 __repr__()魔法方法
  （直接返回字符串）

localtime 时间元祖（time.struct_time）：

gmtime()，localtime() 和 strptime() 以时间元祖（struct_time）的形式返回。
9 个索引值 可以直接用属性得到或者属性值

这个程序还有几点不足的地方：
（1）如果开始计时的时间是（2022年2月22日16:30:30），停止时间是（2025年1月23日15:30:30），那按照我们用停止时间减开始时间的计算方式就会出现负数（3年-1月1天-1小时），你应该对此做一些转换。
（2）现在的计算机速度都非常快，而我们这个程序最小的计算单位却只是秒，精度是远远不够的。


'''
import time as t

class MyTimer:

    def __init__(self):#类的属性名和方法名不能相同 否则属性会覆盖方法
        self.unit = ['年', '月', '日', '时', '分', '秒'] #六个元素单位 弄个列表 在_calc（）方法中self.prompt追加
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__ #重写这两个魔法方法 两个等同 print（t1）和直接调用t1均显示结果

    def __add__(self, other):
        #做局部变量
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    #开始计时
    def start(self):
        self.prompt = '请先调用stop（）停止计时'
        self.begin = t.localtime()
        print('计时开始')
    #停止计时
    def stop(self):
        #判断计时
        if not self.begin:
            print('提示：请先调用start（）计时')
        else:
            self.end = t.localtime()
            self._calc() #对象.内部方法
            print('计时结束')
    '''
    """
    好，万丈高楼平地起，把地基写好后，应该考虑怎么进行计算了。
    localtime()返回的是一个时间元组的结构，只需要在前边6个元素，
    然后将stop的元素依此减去start对应的元素，将差值存放在一个新的列表里：
    """
    '''
    # 内部方法 计算运行时间 内部用下划线开始
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):#localtime用前6个就行
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]: #判断一下 不为0显示 为0不显示
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0

        #print(self.lasted) def _str__里面return了 这就不打印了

t1 = MyTimer()
print(t1)
t1.start()
t1.stop()
print(t1)





