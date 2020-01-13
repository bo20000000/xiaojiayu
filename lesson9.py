# 水仙花数
# int(x,y,z)

# i = 100*x+10*y+z
# x**3+y**3+z**3 = i
# for x in range(1,10):
#     for y in range(1,10):
#         for z in range(1,10):
#             i = 100*x+10*y+z
#             j = x**3+y**3+z**3
#             if(i == j):
#                 print(i)

#red = 3  yellow = 3 green= 6   number = 8
# number = 8
# while number>0:
#     for red in range(3):
#         print("red",end=' ')
#         for yellow in range(3):
#             print("yellow",end=' ')
#             for green in range(6):
#                 print("green",end = ' ')
#                 number -= 1
#     print('/n')

#     # number -= 1

# for i in range(100,1000):
#     sum = 0
#     temp = i #153
#     while temp: #153
#         sum = sum +(temp%10)**3 #180 = 153+(153%10)**3
#         temp//=10

#     if sum == i:
#         print(i)
print('red\tyellow\tbule')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                print(red, '\t', yellow, '\t', green)
