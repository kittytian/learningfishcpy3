'''
在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的。

例如，在不使用鸭子类型的语言中，我们可以编写一个函数，它接受一个类型为鸭子的对象，并调用它的走和叫方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的走和叫方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。任何拥有这样的正确的走和叫方法的对象都可被函数接受的这种行为引出了以上表述，这种决定类型的方式因此得名。

鸭子类型通常得益于不测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用。

从静态类型语言转向动态类型语言的用户通常试图添加一些静态的（在运行之前的）类型检查，从而影响了鸭子类型的益处和可伸缩性，并约束了语言的动态特性（Python 文档中有一句：鸭子类型应避免使用 type() 或 isinstance() 等测试类型是否合法）。

'''


# I love FishC.com!
class Duck:
    def quack(self):
        print("呱呱呱！")

    def feathers(self):
        print("这个鸭子拥有灰白灰白的羽毛。")


class Person:
    def quack(self):
        print("你才是鸭子你们全家人是鸭子！")

    def feathers(self):
        print("这个人穿着一件鸭绒大衣。")


def in_the_forest(duck):
    duck.quack()
    duck.feathers()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


game()

'''

从哪里可以看出 Python 是鸭子类型的风格呢? 

in_the_forest() 函数对参数 duck 只有一个要求：就是可以实现 quack() 和 feathers() 方法。然而 Duck 类和 Person 类都实现了 quack() 和 feathers() 方法，因此它们的实例对象 donald 和 john 都可以用作 in_the_forest() 的参数。这就是鸭子类型。

我们可以看出，鸭子类型给予 Python 这样的动态语言以多态。 但是这种多态的实现完全由程序员来约束强制实现（文档、清晰的代码和测试），并没有语言上的约束（如 C++ 继承和虚函数）。 因此这种方法即灵活，又提高了对程序员的要求。

'''