'''
0. 问大家一个问题：Python 支持常量吗？
相信很多鱼油的答案都是否定的，但实际上 Python 内建的命名空间是支持一小部分常量的，
比如我们熟悉的 True，False，None 等，只是 Python 没有提供定义常量的直接方式而已。
那么这一题的要求是创建一个 const 模块，功能是让 Python 支持常量。

说到这里大家可能还是一头雾水，没关系，我们举个栗子。

test.py 是我们的测试代码，内容如下：

执行后的结果是：
#>>>
FishC
常量无法改变！
常量名必须由大写字母组成！


'''
# const 模块就是这道题要求我们自己写的
# const 模块用于让 Python 支持常量操作
import const

const.NAME = "FishC"
print(const.NAME)

try:
    # 尝试修改常量
    const.NAME = "FishC.com"
except TypeError as Err:
    print(Err)

try:
    # 变量名需要大写
    const.name = "FishC"
except TypeError as Err:
    print(Err)
