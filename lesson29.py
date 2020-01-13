''' # 任务：将文件（record2.txt）中的数据进行分割并按照以下规律保存起来：
# 小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
# 小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
# 文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件（提示：文件中不同的对话间已经使用“==========”分割）
import io
def save_file_name(boy,girl,count):
    file_name_boy = 'boy_'+str(count)+'.txt'
    file_name_girl = 'girl_'+str(count)+'.txt'

    boy_file = open("D:\\xiaojiayu\\"+file_name_boy,'w')
    girl_file = open("D:\\xiaojiayu\\"+file_name_girl,'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    f = open("D:\\xiaojiayu\\record2.txt")
    # f.close()
    boy = []
    girl = []
    count = 1


    for each_line in f:
        if each_line [:6] != '======' :
            #我们在这里进行字符串分割操作
            (role,line_spoken) = each_line.split(':',1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            #文件的分别保存操作
            save_file_name(boy,girl,count)

            boy = []
            girl = []
            count +=1
            
    #文件的分别保存操作
    save_file_name(boy,girl,count)

    f.close()


# str1 = ("小客服:小甲鱼，今天一个会员想找你")
# if '小客服:' in str1:
#     print(str1[4:]) '''
# 方法1

# count = len(open(filepath, 'r').readlines())
# 这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。

# 方法2

# 可以利用enumerate()，统计文件函数：

# count = 0
# for index, line in enumerate(open(filepath,'r')):
#     count += 1
# print count

# file_name = input('请输入文件名：')
# f = open(file_name,'w')
# print('请输入内容【单独输入\':w\'保存退出】：')

# while True:
#     write_some = input()
#     if write_some != ':w':
#         f.write('%s\n' %write_some)
#     else:
#         break
# f.close()

#比较两个文件的不同之处，如有不同，显示出不同的次数与行号
#boy_1.txt  boy_1_other.txt

#两个文件 f1  f2
#次数 count(x)
#行号 for num,value in enumerate(f1):
#       print("行号：%s,内容：%s" %num,%value)

#讲每一行读取 each_line 进行比较

# f1 = open("boy_1.txt", 'rt')
# f2 = open("boy_1_other.txt", 'rt')

# count = 0


# for num,value in enumerate(f1):
#     print("行号：%s,内容：%s" %(num,value))
# def line_count(file_name):
#     num = 0
#     for index, value in enumerate(file_name):
#         num += 1
#     return num
# print()
# def file_compare(f1,f2):    
#     diff_line = []
#     count = 0
#     for line1 in f1:
#         line2 = f2.readline()
#         count+=1
#         if line1 != line2:
#             diff_line.append(count)
#     f1.close()
#     f2.close()
#     return diff_line


# diff = file_compare(f1,f2)
# if len(diff) == 0:
#     print("没有不一样的")
# else:        
#     print("两个文件共有%d行不一样" %len(diff))
#     for i in diff:
        
#         print("第%s行不一样" %i)

#
#
#编写一个程序，讲用户将文件名和行数输入之后，打印该文件前N行的内容
#
#

# file_name=input("请输入需要打印的文件名:")
# f = open(file_name+'.txt','rt')
# # for each_line in f:
# #     print(each_line)
# file_line_num = int(input("需要打印多少行？"))

# count = len(open(file_name+'.txt').readlines())

# def pr_line(file_name,file_line_num):
#     print("需要打印的%s文件的前%s行内容如下" %(file_name.name,file_line_num))
#     for i in range(file_line_num):
#         print(f.readline(),end = '')

# if file_line_num <0:
#     print("wrong")
# elif file_line_num > count:
#     print("需要打印的行数超过文件的总行数")
#     print("需要打印的%s文件的前%s行内容如下" %(file_name,file_line_num))
#     for each_line in f:
#         print(each_line)
# else:
#     pr_line(f,file_line_num)

# f.close()


#
#
#编写一个程序，讲用户将文件名和行数（N，M）输入之后，打印该文件从N-M行的内容
#
#

# 

# def file_view(file_name,line_num):
#     if line_num.strip() == ':':
#         #特殊情况，没有前后数字的时候
#         begin = '1'
#         end  =-1
#     #将m:n分别赋值给begin，end
#     (begin,end) = line_num.split(':')
    
#     #集中不同分割方式
#     if begin =='':
#         begin = '1'
#     if end =='':
#         end = '-1'
#     if begin == '1' and end == '-1':
#         prompt = '的全文'
#     elif begin == '1':
#         prompt = '从开始到%s' %end
#     elif end =='-1':
#         prompt = '从%s到结束' %begin
#     else:
#         prompt = '从%s开始，到%s结束' %(begin,end)

#     print('\n文件%s%s的内容如下:\n' %(file_name,prompt))

#     begin = int(begin) -1
#     end = int(end)
#     lines = end -begin
    
#     f = open(file_name)

#     for i in range(begin):
#         #消耗begin之前的内容
#         f.readline()

#     if lines<0:
#         print(f.read())
#     else:
#         for j in range(lines):
#             print(f.readline(),end = '')

#     f.close()



# file_name = input("请输入文件名（c:\\test.txt):")
# line_num = input("请输入需要显示的行数【格式入13:21或：21或21：或：】")

# file_view(file_name,line_num)


#
#编写一个程序，实现“全部替换”功能
#

# input("请输入文件名：") #somthing.text
# input("请输入需要替换的单词或字符：")  #愿
# input("请输入新的单词或字符：")  #希望

# print("文件 %s 中共有 %s 个【%s】")   #%(something.text,4,愿）
# print("你确定把所有的【%s】替换为【%s】吗？")   #%(愿，希望)
# input("【YES/NO】:")    # yes,Yes,YES/NO,No,no

file_name = 'record2.txt' #input("请输入文件名：")  #somthing.text
rep_word = '小甲鱼' #input("请输入需要替换的单词或字符：")
new_word = '小王八' #input("请输入新的单词或字符：") 
f = open(file_name,'rt')

content = []
record = 1
for each_list in f:
    # 寻找可替换的个数
    if rep_word in each_list:
        record += 1
f.close()
print("文件 %s 中共有 %s 个【%s】" %(file_name,record,rep_word))   #%(something.text,4,愿）   

print("你确定把所有的【%s】替换为【%s】吗？" %(rep_word,new_word))   #%(愿,希望)
commit = input("【YES/NO】:")



if commit in ['yes','Yes','YES']:

    f_write = open(file_name,'w')
    f_write.writelines(content)
    f_write.close()
f_write.close()
    



"""
def file_replace(file_name,rep_word,new_word):
    f_read = open(file_name)

    content = []
    count = 0

    for each_line in f_read:
        if rep_word in each_line:
            count = each_line.count(rep_word)
            each_line = each_line.replace(rep_word,new_word)
        content.append(each_line)

    decide = input('\n 文件 %s 中共有 %s 个【%s】\n你确定把所有的【%s】替换为【%s】吗？\n' %(file_name,count,rep_word,rep_word,new_word))

    if decide in ['yes','Yes','YES']:
        f_write = open(file_name,'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()

file_replace(file_name,rep_word,new_word)
"""