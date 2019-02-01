'''

第一种：import 模块名
第二种：from 模块名 import 函数名（from 模块名 import * 这种方法不建议使用，因为这样的话，命名空间的优势就荡然无存了，可能造成重名的困扰）
第三种：import 模块名 as 新名字 （推荐）

'''

#import _50example
#from _50example import c2f, f2c
import _50example as tc

print("32摄氏度 = %.2f华氏度" % tc.c2f(32))
print("99华氏度 = %.2f摄氏度" % tc.f2c(99))