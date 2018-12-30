'''
尝试用字典的特性编写一个通讯录程序 功能如图
脑子要清晰 ！ 联系人 姓名是 key 电话是value!!!
删除用del del 是python的内置函数，可以直接删去一些对象中的一些元素或对象本身
也可用dict.pop()
还是参考答案写的~~~~(>_<)~~~~
'''
print('--- 欢迎进入通讯录程序 ---')
print('--- 1 ：查询联系人资料 ---')
print('--- 2：插入新的联系人 ---')
print('--- 3：删除已有联系人 ---')
print('--- 4：退出通讯录程序 ---')

contact = dict()

while True:
    inputstr = input('请输入相关的指令代码 ：')

    if inputstr == '1':
        for name in contact:
            if name == input('请输入联系人姓名:'):
                print(name + ':' + contact[name])

    if inputstr == '2':
        name = input('请输入联系人姓名：')
        if name in contact:
            print('您输入的姓名在通讯录已存在 - - >', end='')
            print(name +':'+contact[name])
            if input('是否修改用户资料（YES/NO ）:') =='YES':
                contact[name] = input('请输入用户联系电话：')
        else:
            contact[name] = input('请输入用户联系电话：')

    if inputstr == '3':
        name = input('请输入要删除的联系人姓名:')
        if name in contact:
            del(contact[name])
        else:
            print('您输入的联系人不存在')


    if inputstr == '4':
        print('bye')
        break






