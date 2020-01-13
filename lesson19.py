# def fun(var):
#     var = 1314
#     print(var,end = ' ')

# var = 520
# fun(var)
# print(var)
var = 'Hi '

# def fun1():
#     global var
#     var = 'Baby '
#     return fun2(var)

# def fun2(var):
#     var += 'I love you'
#     fun3(var)
#     return var

# def fun3(var):
#     var = ' 小甲鱼'

# print(fun1())

#回文联
#函数判断[0]==[-1]即可
# def palindrame(str):
#     for i in range(len(str)):
#         if str[i]!=str[len(str)-1-i]:
#             return('不是')
#             break;

#         else:
#             return('是')


# str = input("请输入一句话：")
# print('"'+str+'"'+huiwen(str)+'回文联')

# def palindrame(string):
#     length = len(string)
#     last = length-1
#     length//=2
#     flag = 1
#     for each in range(length):
#         if string[each] != string[last]:
#             flag = 0
#         last -=1

#     if flag ==1:
#         return 1
#     else:
#         return 0

# string = input("请输入一句话：")
# if palindrame(string) ==1:
#     print("是回文联")
# else:
#     print("不是回文联")



#编写一个函数，分别统计出传入字符串的参数（可能不止一个参数）的英文字母，空格，数字和其他字符的个数

def count(sting):
    for each in string:
        letters=0
        space =0
        digit = 0
        others = 0
        if each.isalpha():
            letters += 1
        elif each.isdigit():
            digit += 1
        elif each == ' ':
            space += 1
        else:
            others +=1


# 
# def count(*param):
#     for 
