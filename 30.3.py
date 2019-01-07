#编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件
# （要求查找mp4 rmvb, avi的格式即可），
# 并把创建一个文件（vedioList.txt）存放所有找到的文件的路径，程序实现如图：
import os
def searchfile(start_dir, file_type):

    os.chdir(start_dir)

    for eachfile in os.listdir(os.curdir):
        temp = os.path.splitext(eachfile)[1]
        if temp in file_type:
            print(os.getcwd() + os.sep + eachfile)# 使用os.sep是程序更标准
            vediolist.append(os.getcwd() + os.sep + eachfile + os.linesep)
        else:
            if os.path.isdir(eachfile):
                searchfile(eachfile, file_type) # 递归调用
                os.chdir(os.pardir) # 递归调用后切记返回上一层目录



start_dir = input('请输入待查找的初始目录：')

file_type = ['.mp4', '.rmvb', '.avi'] #匹配
vediolist = [] #存文件路径

searchfile(start_dir, file_type)


f = open('vedioList.txt', 'w') #会写到用户输入的初始目录下 而且没分行 得写vediolist.append(os.getcwd() + os.sep + eachfile+os.linesep)
f.writelines(vediolist)
f.close()

'''
import os
 
def search_file(start_dir, target) :
    os.chdir(start_dir)
    
    for each_file in os.listdir(os.curdir) :
        ext = os.path.splitext(each_file)[1]
        if ext in target :
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep) # 使用os.sep是程序更标准
        if os.path.isdir(each_file) :
            search_file(each_file, target) # 递归调用
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录
 
start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd() #小甲鱼这个 写到当前运行程序的目录下
 
target = ['.mp4', '.avi', '.rmvb']
vedio_list = []
 
search_file(start_dir, target)
 
f = open(program_dir + os.sep + 'vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()

'''