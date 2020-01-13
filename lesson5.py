""" 
i = float(input('input the number'))
if i-int(i) > 0.5:
    i = int(i)+1
else:
    i = int(i)
print(i)
print(type(i))
print(isinstance(i,float))

"""

# 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活
# 运用）
"""
year = int(input('请输入4位年份：'))


if year%4==0:
    if  year%100 == 0 and year%400!=0:
        print('%d不是闰年！'%year)
    else:
        print('%d是闰年' %year)
else:
    print('%d不是闰年' %year)
"""
""" 
import random
times = 3
secret = random.randint(1, 10)
guess = 0
print("不妨猜一下是那个数字？", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit() and int(temp)<0 and int(temp)>10:
        temp = input("抱歉，请输入一个0-10的数字")
        
    guess = int(temp)
    times -= 1
    if guess == secret:
        print("猜对了")
    else:
        if guess > secret:
            print("大了")
        else:
            print("小了")
        if times > 0:
            print("在猜一次", end=" ")
        else:
            print("没机会了")
print("游戏结束")
 """

""" temp = input('Input a int: ')
number = int(temp)
i = 1
while number:
    print(i)
    i = i + 1
    number = number - 1
 """

""" temp = input("Input a int:")
number = int(temp)
while number:
    i = number -1
    while i:
        print(' ',end = '')
        i = i-1
    j = number
    while j:
        print('*',end = '')
        j = j-1
    print()
    number = number -1 """

number= (not 1) or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
