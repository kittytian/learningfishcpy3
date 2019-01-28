'''
既然咱都做到了这一步，那不如再深入一下。再次改进我们的代码，让它能够统计一个函数运行若干次的时间。
要求一：函数调用的次数可以设置（默认是 1000000 次）
要求二：新增一个 timing() 方法，用于启动计时器
 

函数演示：

#>>> ================================ RESTART ================================
#>>>
#>>> def test():
        text = "I love FishC.com!"
        char = 'o'
        if char in text:
                pass


#>>> t1 = MyTimer(test)
#>>> t1.timing()
#>>> t1
总共运行了 0.27 秒
#>>> t2 = MyTimer(test, 100000000)
#>>> t2.timing()
#>>> t2
总共运行了 25.92 秒
#>>> t1 + t2
'总共运行了 26.19 秒'

'''
import time as t

class MyTimer:

    #初始化数据
    def __init__(self, func, number=1000000):     #func代表后传入的函数名

        self.prompt = "未开始计时！"     #直接调用的话，会显示这一句。
        self.lasted = 0.0
        self.default_timer = t.perf_counter
        self.func = func
        self.number = number

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    #相加
    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了 %0.2f 秒" % result       #格式化字符串，小数点后两位
        return prompt


    # 内部方法，计算运行时间
    def timing(self):
        self.begin = self.default_timer()
        for i in range(self.number):                         #for循环运行后传入的函数，运行number次。
            self.func()
        self.end = self.default_timer()
        self.lasted = self.end - self.begin
        self.prompt = "总共运行了 %0.2f 秒" % self.lasted

    # 设置计时器(time.perf_counter() 或 time.process_time())
    def set_timer(self, timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print("输入无效，请输入 perf_counter 或 process_time")
