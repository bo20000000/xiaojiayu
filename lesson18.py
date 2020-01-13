'''
0.编写一个符合以下要求的函数：
    a）计算打印所有参数的和乘以基数（base = 3）的结果
    b）如果参数中最后一个参数为（base = 5），则设定基数为5，基数不参与求和计算

'''
# def canshu(cs=[],jishu=3):
#     jieguo = 0
#     for each in cs:
#         jieguo += int(each)
#     result = jieguo*jishu
#     print(result)

# luru = list(input('请输入列表:'))
# if luru[-1]==5:
#     canshu(cs=luru[0,-2],jishu=5)
# else:
#     canshu(cs=luru,jishu)


# def mfun(*param,base = 3):
#     result = 0
#     for each in param:
#         result += each
#     result *= base

#     print("结果是：",result)

# mfun(1,2,3,4,5,base =5)

#水仙花数
def shuixianhua(x):
    a = x//100
    b = (x-a*100)//10
    c = x-a*100-b*10
    y= a**3+b**3+c**3
    if x == y:
        return(x)
    else:
        return;

for i in range(100,999):
    if shuixianhua(i):
        print(shuixianhua(i))

#一个子字符串在一个母字符串中出现的次数
def cishu(str1,str2):
    result = 0
    for each in range(len(str1)):
        if str1[each] ==str2[0] and str1[each+1] == str2[1]:
            result +=1
    return(result)

str1 = input("请输入长字符串：")
str2 = input("请输入短字符串：")

print("在长字符串中出现短字符串的次数为：",cishu(str1,str2))


# you cannot improve your pase, but you can improve your future. 
