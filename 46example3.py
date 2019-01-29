'''
看41.1
先定义一个温度类，
然后定义两个描述符类 涉及到三个方法 用于描述摄氏度和华氏度两个属性。

•要求两个属性会自动进行转换，也就是说你可以给摄氏度这个属性赋值，然后打印的华氏度属性是自动转换后的结果。

公式：摄氏度 * 1.8 + 32 = 华氏度
'''
class Celsius:
    def __init__(self, value=26.0):#温度初始化
        self.value = float(value) #统一浮点型
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner): #instance 拥有者 就是Temperature的实例对象
        return instance.cel * 1.8 + 32
    def __set__(self, instance, value):
        instance.cel = (float(value) - 32 ) /1.8 #反运算

class Temperature:
    cel = Celsius()
    fah = Fahrenheit() #当这个属性被赋值的时候 执行描述符类的set方法


temp = Temperature()
print(temp.cel)
temp.cel = 30
print(temp.fah)
temp.fah = 100
print(temp.cel)
