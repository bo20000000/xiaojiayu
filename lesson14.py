#定义一个跨越多行的字符串 至少两种方法
# steam1 = '111111111\n11111111'
# print(steam1)

# steam2 = '''222222
#             222222'''
# print(steam2)

#code
# alpha num   len<8
#alpha num    len>8

# code=input('please input the password')

# 密码安全性检查
#
#低级密码要求：
#   1.密码由单纯的数字或字母组成
#   2.密码长度小于等于8位
#
#中级密码要求：
#   1.密码必须由数字、字母或特殊字符（仅限~!@#$%^&*()_=-/,.?<>;:[]{}|\)
#   任意两种组合
#   2.密码长度不能低于8位
#
#高级密码要求：
#   1.密码必须由数字、字母及特殊字符三种组合
#   2.密码只能由字母开头
#   3.密码长度不能低于16位

symbols = r'~!@#$%^&*()_=-/,.?<>;:[]{}\|'

chars = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'

# for i in symbols:
#     print(i)
password = input("请输入密码")
l = len(password)
while(password.isspace() or len==0):
    print("密码不能为空")
if l<= 8:
    len_level = 1
elif l>8 and l<16:
    len_level = 2
else:
    len_level = 3

flag_con = 0
#判断是否有特殊字符
for each in password:
    if each in symbols:
        flag_con +=1
        break;

#判断是否包含字母
for each in password:
    if each in chars:
        flag_con +=1
        break;

#判断是否包含数字
for each in password:
    if each in nums:
        flag_con +=1
        break;

while 1:
    print("你的密码安全级别评定为： ",end='')
    if len_level==1 or flag_con ==1:
        print("低")
    elif len_level==2 or flag_con ==2:
        print("中")
    else:
        print("高")
    break;


