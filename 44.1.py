'''
1. 相信大家已经意识到不对劲了：为毛一个月一定要31天?不知道有可能也是30天或者29天吗？（上一题我们的答案是假设一个月31天）

没错，如果要正确得到月份的天数，我们还需要考虑是否闰年，还有每月的最大天数，所以太麻烦了……如果我们不及时纠正，我们会在错误的道路上越走越远……

所以，这一次，小甲鱼提出了更优秀的解决方案（Python官方推荐）：
用 time 模块的 perf_counter() 和 process_time() 来计算，其中
 perf_counter() 返回计时器的精准时间（系统的运行时间）； process_time() 返回当前进程执行 CPU 的时间总和。

题目：改进我们课堂中的例子，这次使用 perf_counter() 和 process_time() 作为计时器。
另外增加一个 set_timer() 方法，用于设置默认计时器（默认是 perf_counter()，可以通过此方法修改为 process_time()）。

'''

import time as t

class MyTimer:

    def __init__(self):#类的属性名和方法名不能相同 否则属性会覆盖方法

        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0
        self.default_timer = t.perf_counter #赋值

    def __str__(self):
        return self.prompt

    __repr__ = __str__ #重写这两个魔法方法 两个等同 print（t1）和直接调用t1均显示结果

    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了 %0.2f 秒" % result
        return prompt

    #开始计时
    def start(self):
        self.prompt = '请先调用stop（）停止计时'
        self.begin = self.default_timer()
        print('计时开始')
    #停止计时
    def stop(self):
        #判断计时
        if not self.begin:
            print('提示：请先调用start（）计时')
        else:
            self.end = self.default_timer()
            self._calc() #对象.内部方法
            print('计时结束')


    # 内部方法 计算运行时间 内部用下划线开始
    def _calc(self):
        self.lasted = self.begin - self.end
        self.prompt = "总共运行了 %0.2f 秒" % self.laste

        #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0

        # 设置计时器(time.perf_counter() 或 time.process_time())
    def set_timer(self, timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print("输入无效，请输入 perf_counter 或 process_time")

