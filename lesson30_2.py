#
#编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇文件夹
#则进入文件夹继续搜索
#

#请输入待查找的初始目录： #E:\\TestFolder
#请输入需要查找的目标文件：  #测试3.txt

#输出  E:\\TestFolder\\SubFolder1\\SubFolder3\测试3.txt 
os.path.dirname


import os

file_path=input('请输入待查找的初始目录：')
os.chdir(file_path)

