# 0.如果希望在函数中改变全局变量的值，应该用什么关键字？
#   public
# 1.在嵌套的函数中，如果希望在内部函数修改外部函数的局部变量，应该使用什么关键字？
#   nolocal
# 
# def outside():
#     print('1111')
#     def inside():
#         print('2222')

# outside.inside()

# def outside():
#     var =  5 
#     def inside(var):
#         print(var)
#         var = 3
    
#     inside(var)
# outside()
# def outside():
#     var =  5 
#     def inside():
#         var = 3
#         print(var)
        
    
#     inside()
# outside()
# def funOut():
#     def funIn():
#         print('11111')
    # return funIn()

# funOut()()

# def funX():
#     x = 5
#     def funY():
#         nonlocal x
#         x += 1
#         return x
#     return funY

# a = funX()
# print(a())
# print(a())
# print(a())

#动动手
#0.请用已学过的知识编写程序，统计下边这个长字符串中各个字符出现的次数并找到小甲鱼送个大家的一句话
# import open from os
# filename =  'D:\\xiaojiayu\\string1.txt'
# f = open(filename)
# str1 = f.read()
# print (str1)
# list = []
# for each in str1:
#     '遍历打印txt文件中的所有字符'
#     # print(i)
#     if each not in list:
#         if each == '\\n':
#             print('\\n',str1.count(each))
#         else:
#             print(each,str1.count(each))
#         list.append(each)

#1.请用已学的知识编写程序，找到小甲鱼藏在下边这个长字符串中的密码，密码的埋藏点符合以下规律：
#       a）每位密码为单个小写字母
#       b）每位密码的左右两边且只有三个大写字母

filename =  'D:\\xiaojiayu\\string2.txt'
f = open(filename)
str1 = f.read()       
# passcode = []
# for each in str1:
'''
    a）每位密码为单个小写字母
    each.islower()
    b）每位密码的左右两边且只有三个大写字母
    1.先发现一个大写字母 str1[each].isupper()
    2.在发现第二个，第三个大写字母str1[cach+1].isupper,str1[each+2].isupper
    前三中一后三 提取7个字符 要符合规则
    提取9个字符 要符合规则
    [0,1,2,3,4,5,6,7,8,9]
    [-9,-8,-7,-6,-5,-4,-3,-2,-1]
    [-4,-3,-2,-1,0,1,2,3,4]
'''    

# substr = []
# for i in range(3,len(str1)-4):
#     if str1[i-4].islower and str1[i+4].islower:
#         for j in range (1,3):
#             if str1[i-j].isupper and str1[i+j].isupper:
#                 if str1[i].islower:
#                     return(str1[i])
#     else:
#         i+=1

# countA = 0
# countB = 0
# countC = 0
# length = len(str1)
# for i in range(length):
#     if str1[i] == '\n':
#         continue
#     if str1[i].isupper():
#         if countB ==1:
#             countC +=1
#             countA = 0
#         else:
#             countA += 1
#             continue
#     if str1[i].islower() and countA == 3:
#         countB =1
#         countA = 0
#         target = i
#         continue
#     if str1[i].islower() and countC == 3:
#         print(str1[target],end = ' ')
#     countA = 0
#     countB = 0
#     countC = 0





countA = 0  # 统计前边的大写字母
countB = 0  # 统计小写字母
countC = 0  # 统计后边的大写字母
length = len(str1)

for i in range(470,length):
    if str1[i] == '\n':
        continue

    """
    |如果str1[i]是大写字母：
    |-- 如果已经出现小写字母：
    |-- -- 统计后边的大写字母
    |-- 如果未出现小写字母：
    |-- -- 清空后边大写字母的统计
    |-- -- 统计前边的大写字母
    """
    if str1[i].isupper():
        if countB:
            countC += 1
        else:
            countC = 0
            countA += 1

    """
    |如果str1[i]是小写字母：
    |-- 如果小写字母前边不是三个大写字母（不符合条件）：
    |-- -- 清空所有记录，重新统计
    |-- 如果小写字母前边是三个大写字母（符合条件）：
    |-- -- 如果已经存在小写字母：
    |-- -- -- 清空所有记录，重新统计（出现两个小写字母）
    |-- -- 如果该小写字母是唯一的：
    |-- -- -- countB记录出现小写字母，准备开始统计countC
    """
    if str1[i].islower():
        if countA != 3:
            countA = 0
            countB = 0
            countC = 0
        else: 
            if countB:
                countA = 0
                countB = 0
                countC = 0
            else:
                countB = 1
                countC = 0
                target = i

    """
    |如果前边和后边都是三个大写字母：
    |-- 如果后边第四个字母也是大写字母（不符合条件）：
    |-- -- 清空记录B和C，重新统计
    |-- 如果后边仅有三个大写字母（符合所有条件）：
    |-- -- 打印结果，并清空所有记录，进入下一轮统计
    """
    if countA == 3 and countC == 3:
        if i+1 != length and str1[i+1].isupper():
            countB = 0
            countC = 0
        else:
            print(str1[target],i, end='')
            countA = 3
            countB = 0
            countC = 0

