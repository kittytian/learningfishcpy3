'''
你可以利用异常的原理，修改下面的代码使得更高效率的实现吗？
自己改的 错了 应该考虑字典！！键存不存在问题：

print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    try:
        instr = int(input('\n请输入相关的指令代码：'))
    except ValueError as reason:
        print('出错啦：' + str(reason))
    else:
        if instr == 1:
            name = input('请输入联系人姓名：')
            if name in contacts:
                print(name + ' : ' + contacts[name])
            else:
                print('您输入的姓名不再通讯录中！')

        if instr == 2:
            name = input('请输入联系人姓名：')
            if name in contacts:
                print('您输入的姓名在通讯录中已存在 -->> ', end='')
                print(name + ' : ' + contacts[name])
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
            else:
                contacts[name] = input('请输入用户联系电话：')

        if instr == 3:
            name = input('请输入联系人姓名：')
            if name in contacts:
                del (contacts[name])  # 也可以使用dict.pop()
            else:
                print('您输入的联系人不存在。')

        if instr == 4:
            break

print('|--- 感谢使用通讯录程序 ---|')
小甲鱼：使用条件语句的代码非常直观明了，但是效率不高。
因为程序会两次访问字典的键，
一次判断是否存在（例如 if name in contacts），一次获得值（例如 print(name + ' : ' + contacts[name])）。

如果利用异常解决方案，我们可以简单避开每次需要使用 in 判断是否键存在字典中的操作。
因为只要当键不存在字典中时，会触发 KeyError 异常，利用此特性我们可以修改代码如下：

'''

print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        try:
            print(name + ' : ' + contacts[name])
        except KeyError:
            print('您输入的姓名不再通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        try:
            contacts[name]  # 有点“为赋新词强说愁”的感觉
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ' : ' + contacts[name])
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        except KeyError:
            contacts[name] = input('请输入用户联系电话：')

    if instr == 3:
        name = input('请输入联系人姓名：')
        try:
            del (contacts[name])  # 也可以使用dict.pop()
        except KeyError:
            print('您输入的联系人不存在。')

    if instr == 4:
        break

print('|--- 感谢使用通讯录程序 ---|')
