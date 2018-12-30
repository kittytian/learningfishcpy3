

'''
编写一个用户登录程序
实现如图
这次
将功能封装成函数！！！！！


'''

user = dict()
def menu():


    while True:
        print('----新建用户:N/n----')
        print('----登录账号:E/e----')
        print('----退出程序:Q/q----')
        print('---请输入指令代码：')

        inputstr = input()
        if inputstr == 'N' or inputstr == 'n':
            createuser()
        if inputstr == 'E' or inputstr == 'e':
            loginin()
        if inputstr == 'Q' or inputstr == 'q':
            break


def createuser():

    while True:
        username = input('请输入用户名：') #要把这句放在while里面 continue跳出 会从这（进行下一轮while循环）继续开始再比较if
        if username in user:
            print('此用户名已被使用 请重新输入用户名')
            continue      #这个要会啊啊啊！！！！循环那再看看
        else:
            break                         #break跳出while循环 直接到下面请输入密码
    user[username] = input('请输入密码:')
    print('注册成功')




def loginin():


    while True:
        username = input('请输入用户名：')
        if username not in user:
            print('用户名不存在')
            continue
        else:
            break
    password = input('请输入密码:')
    if password == user[username]:
        print('welcome')
    else:
        print('密码错误')

menu()






