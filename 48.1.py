'''
1. 写一个迭代器，要求输出至今为止的所有闰年。如：
#>>> leapYears = LeapYear()
#>>> for i in leapYears:
        if i >=2000:
                print(i)
        else:
                break

2012
2008
2004
2000
提示：闰年判定法（(year%4 == 0 and year%100 != 0) or (year%400 == 0)）

'''
class LeapYear:
    def __init__(self):
        self.this_year = 2019

    def isLeapYear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self
    def __next__(self): #__next__()魔法方法，决定了迭代的规则 有返回值
        while not self.isLeapYear(self.this_year):
            self.this_year -= 1
        temp = self.this_year
        self.this_year -= 1
        return temp

leapYears = LeapYear()
for i in leapYears:
        if i >= 2000:
                print(i)
        else:
                break

'''
import datetime as dt
 
class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year
 
    def isLeapYear(self, year):
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False
        
    def __iter__(self):
        return self
 
    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1 
 
        temp = self.now
        self.now -= 1
        
        return temp


'''