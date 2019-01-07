#编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。
# 如遇到文件夹，则进入文件夹继续搜索，程序实现如图：
#一定要养成函数的思维 参考小甲鱼老师的 这个递归没想到（进入文件夹继续搜索！）
#还得返回
# os.chdir换到查找初始目录 再遍历查找


import os
def searchfile(start_dir, target):

    os.chdir(start_dir)

    for eachfile in os.listdir(os.curdir):
        if eachfile == target:
            print(os.getcwd() + os.sep + eachfile)# 使用os.sep是程序更标准
        else:
            if os.path.isdir(eachfile):
                searchfile(eachfile, target) # 递归调用
                os.chdir(os.pardir) # 递归调用后切记返回上一层目录


start_dir = input('请输入待查找的初始目录：')
target = input('请输入需要查找的目标文件：')
searchfile(start_dir, target)

