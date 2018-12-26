print("判断给定年份是否为闰年:")
temp = input("请输入四位年份（1980）：")
while not temp.isdigit():
    temp = input("输入有误！请输入例如1980的4位年份：")
userinput = int(temp)
if userinput % 4 == 0 and userinput % 100 != 0:
     print(temp+'是闰年')
else:
    if userinput % 400 == 0:
       print(temp+'是闰年')
    else:
       print(temp+'不是闰年')

print("结束")
