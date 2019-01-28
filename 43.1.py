'''
1. 定义一个单词（Word）类继承自字符串，重写比较操作符（参考自学：Python 魔法方法详解），
当两个 Word 类对象进行比较时，根据单词的长度来进行比较大小。
加分要求：实例化时如果传入的是带空格的字符串，则取第一个空格前的单词作为参数。

答：加分要求可以通过重载 __new__ 方法来实现（因为字符串是不可变类型），通过重写 __gt__、__lt__、__ge__、__le__ 方法来定义 Word 类在比较操作中的表现。

注意，我们没有定义 __eq__ 和 __ne__ 方法。这是因为将会产生一些怪异不符合逻辑的结果（比如 Word('FishC') 会等于 Word('Apple')）


'''
class Word(str):
    def __new__(cls, word):
        # 注意我们必须要用到 __new__ 方法，因为 str 是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print('Value contains spaces. Truncating to first space.')
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)
    def __gt__(self, other):
        return len(self) > len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __le__(self, other):
        return len(self) <= len(other)


a = Word('fish')
b = Word('i love')
print(a > b)