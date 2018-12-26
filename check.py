'''

# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

'''

numbers = '0123456789'
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
specharacters = '~!@#$%^&*()_=-/,.?<>;:[]{}\|'

while True:
    password = input('请输入需要检查的密码组合： ')
    length = len(password)
    #添加判断 好好看看参考第一个代码 人家写的很好
    while (password.isspace() or length == 0):
        password = input('您输入的密码为空（或空格），请重新输入：')

    if 0 < length <= 8:
        flag2 = 1
    elif 8 < length <= 16:
        flag2 = 2
    elif password[0] in characters and length > 16:
        flag2 = 3

    flag1 = 0
    for each in password:
        if each in numbers:
            flag1 += 1
            break
    for each in password:
        if each in characters:
            flag1 += 1
            break
    for each in password:
        if each in specharacters:
            flag1 += 1
            break
    print('您的密码安全等级为：', end=' ')
    if flag1 == 2 and flag2 == 2:
            print('Medium')
            print('请提高密码等级')
    elif flag1 == 3 and flag2 == 3:
            print('HIGH')
            print('继续保持')
    else:
            print('LOW')
            print('请提高密码等级')



'''

方法一：

str1 = "~!@#$%^&*()_=-/,.?<>;:[]{}\|"
has_str1 = 0
has_num = 0
has_alpha = 0
t = 'y'
while t == 'y':
        password = input("请输入需要检查的密码组合：")
        length = len(password)
        while(password.isspace() or length == 0):
                password = input('您输入的密码为空（或空格），请重新输入：')
        for i in password:
                if i in str1:
                        has_str1 = 1
                if i.isdigit():
                        has_num = 1
                if i.isalpha():
                        has_alpha = 1
        has =  has_str1 + has_num + has_alpha
        if length <= 8 or password.isalnum():
                level = "低"
        if length > 8 and has ==2:
                level = "中"
        if length >= 16 and has == 3 and password[0].isalpha():
                level = "高"
        print("您的密码安全等级评定为：%s"%level)
        if level == "高":
                print("请继续保持")
        else:
                print("""请按以下方式提升您的密码安全级别： 
        1.密码必须由数字、字母及特殊字符三种组合 
        2.密码只能由字母开头 
        3.密码长度不能低于16位""")
        t = input("还要再测试么？（”y“继续，其他退出）")
注意：特殊的数字开头的高级密码没有判断

方法二：
symbols = "~!@#$%^&*()_=-/,.?<>;:[]{}\|"
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
t = 'y'
while t == 'y':
    passwd = input('请输入密码：')
    length = len(passwd)
#判断长度
    while(passwd.isspace() or length == 0):
        passwd = input('您输入的密码为空（或空格），请重新输入：')
        length = len(passwd)
    if length <= 8:
        flag_len = 1
    elif 8 < length <16:
        flag_len = 2
    else:
        flag_len = 3
    flag_con = 0
#判断是否包含特殊字符
    for each in passwd:
        if each in symbols:
            flag_con +=1
            break
#判断是否包含字母
    for each in passwd:
        if each in chars:
            flag_con += 1
            break
#判断是否包含数字
    for each in passwd:
        if each in nums:
            flag_con += 1
            break
#打印结果
    while 1:
        print("您的密码安全级别评定为：",end='')
        if flag_len == 1 or flag_con == 1:
            print("低")
        elif flag_len == 2 or flag_con == 2:
            print("中")
        else:
            print("高")
            print("请继续保持")
            break
        print("""请按以下方式提升您的密码安全级别： 
    1.密码必须由数字、字母及特殊字符三种组合 
    2.密码只能由字母开头 
    3.密码长度不能低于16位""")
        break
    t = input("还要再测试么？（”y“继续，其他退出）")
注意：判断高级密码没有条件 其他类型都是高级

方法三：
str0 = """请按以下方式提升您的密码安全级别： 
    1.必须由数字、字母及特殊字符三种组合（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}\|） 
    2.密码只能由字母开头 
    3.密码长度不能低于16位"""

str1 = '您的密码安全级别评定为：低\n' + str0 + """ 
    4.替王尼玛给隔壁老王送上一把水果刀 
    5.告诉你的孩子，他是充话费下送的 
    6.召集另外三只小甲鱼，喂他们突变剂，救纽约人民于水火 
    """
str2 = '您的密码安全级别评定为：中\n' + str0 + """ 
    4.扶老奶奶过马路，帮室友补袜子 
    """
str3 = '您的密码安全评定为：高\n请继续保持！'

special = "~!@#$%^&*()_=-/,.?<>;:[]{}\|"
letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
t = 'y'

while t == 'y':
    password = input("请输入需要检查的密码组合：")

    # 用num来统计字符类型出现次数  
    num = 0
    a = b = c = 0
    # 输入的不能为空  
    while password == '':
        password = input("不能为空，请重新输入：")
        # 计算num的值，如果输入的全部是字符，那么num=0，所以才会有<=1  
    if password.isnumeric() or password.isalpha():
        num = 1
    else:
        for i in password:
            if a == 0 and i in special:
                num += 1
                a = 1
            elif b == 0 and i in number:
                num += 1
                b = 1
            elif c == 0 and i in letter:
                num += 1
                c = 1
    if password[0] in letter and num == 3 and len(password) >= 16:
        print(str3)
    elif num >= 2 and len(password) >= 8:
        print(str2)
    elif num <= 1 and len(password) < 8:
        print(str1)
    t = input("还要再测试么？（”y“继续，其他退出）")  

'''
