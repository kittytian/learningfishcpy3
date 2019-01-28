'''
0. 按照课堂中的程序，如果开始计时的时间是（2022年2月22日16:30:30），
停止时间是（2025年1月23日15:30:30），
那按照我们用停止时间减开始时间的计算方式就会出现负数，你应该对此做一些转换。
这题直接参考答案 -1月实际上是11月
'''

import time as t

class MyTimer:

    def __init__(self):#类的属性名和方法名不能相同 否则属性会覆盖方法
        self.unit = ['年', '月', '日', '时', '分', '秒'] #六个元素单位 弄个列表 在_calc（）方法中self.prompt追加
        self.borrow = [0, 12, 31, 24, 60, 60] #借位 对应年月日时分秒 默认31天
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

    # 内部方法 计算运行时间 内部用下划线开始
    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):#localtime用前6个就行
            temp = self.end[index] - self.begin[index]
            # 低位不够减，需向高位借位

            if temp < 0: # 测试高位是否有得“借”，没得借的话向再高位借......
                i = 1
                while self.lasted[index - i] < 1:
                    self.lasted[index - i] += self.borrow[index - i] - 1
                    self.lasted[index - i] -= 1
                    i += 1

                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index - 1] -= 1
            else:
                self.lasted.append(temp)

        # 由于高位随时会被借位，所以打印要放在最后
        for index in range(6):
            if self.lasted[index]: #判断一下 不为0显示 为0不显示
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        #为下一轮计时初始化变量
        self.begin = 0
        self.end = 0
'''

1.        import time as t
2.        
3.        class MyTimer:
4.            def __init__(self):
5.                self.unit = ['年', '月', '天', '小时', '分钟', '秒']
6.                self.borrow = [0, 12, 31, 24, 60, 60]
7.                self.prompt = "未开始计时！"
8.                self.lasted = []
9.                self.begin = 0
10.                self.end = 0
11.            
12.            def __str__(self):
13.                return self.prompt
14.        
15.            __repr__ = __str__
16.        
17.            def __add__(self, other):
18.                prompt = "总共运行了"
19.                result = []
20.                for index in range(6):
21.                    result.append(self.lasted[index] + other.lasted[index])
22.                    if result[index]:
23.                        prompt += (str(result[index]) + self.unit[index])
24.                return prompt
25.            
26.            # 开始计时
27.            def start(self):
28.                self.begin = t.localtime()
29.                self.prompt = "提示：请先调用 stop() 停止计时！"
30.                print("计时开始...")
31.        
32.            # 停止计时
33.            def stop(self):
34.                if not self.begin:
35.                    print("提示：请先调用 start() 进行计时！")
36.                else:
37.                    self.end = t.localtime()
38.                    self._calc()
39.                    print("计时结束！")
40.        
41.            # 内部方法，计算运行时间
42.            def _calc(self):
43.                self.lasted = []
44.                self.prompt = "总共运行了"
45.                for index in range(6):
46.                    temp = self.end[index] - self.begin[index]
47.        
48.                    # 低位不够减，需向高位借位 
49.                    if temp < 0:
50.                        # 测试高位是否有得“借”，没得借的话向再高位借......
51.                        i = 1
52.                        while self.lasted[index-i] < 1:
53.                            self.lasted[index-i] += self.borrow[index-i] - 1
54.                            if self.lasted[index-i-1] – 1 < 0:           #判断更高位是否为0，若为0则继续借位。
55.                                      i += 1
56.                             else:                                                #若不为0则break
57.                                  self.lasted[index – i-1] -= 1          
58.                                  self.lasted[index-1] += 1              # 上面第一次运行会对self.lasted[index-1]减掉1，后面也会多减1。此处加上多减掉的1       
59.                                  break                         #我把这里改动了下，测试了没问题。大家可以参考一下，发现问题，互相学习。
60.                        
61.                        self.lasted.append(self.borrow[index] + temp)
62.                        self.lasted[index-1] -= 1
63.                    else:
64.                        self.lasted.append(temp)
65.        
66.                # 由于高位随时会被借位，所以打印要放在最后
67.                for index in range(6):
68.                    if self.lasted[index]:
69.                        self.prompt += str(self.lasted[index]) + self.unit[index]
70.                
71.                # 为下一轮计时初始化变量
72.                self.begin = 0
73.                self.end = 0

'''