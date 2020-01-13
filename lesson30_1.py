#
#编写一个程序，计算当前文件夹下所有文件的大小
#

import os
all_files = os.listdir(os.getcwd())

for each_file in all_files:
    if os.path.isdir(each_file) == False:
        print('%s 【%s Bytes】 ' %(each_file,os.path.getsize(each_file)))
    

