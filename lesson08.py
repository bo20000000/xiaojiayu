''' 
x=1
y=2
z=3
x,y,z = z,y,x
print(x,y,z)
 '''

# score = int(input("请输入一个0-100的分数："))
# if score<0 or score>100:
#     print('Wrong')
# else:
#     if score>=60 and score<=80:
#         print('C')
#     elif score>=90:
#         print('A')
#     elif score<90 and score>80:
#         print('B')
#     else:
#         print('D')

x, y, z = 6, 5, 4
# if x<y:
#     small = x
#     if z <small:
#         small=z
# elif y<z:
#     small = y
# else:
#     small =z
# print(small)
# if x<y<z:
#     print(x)
# elif y<x<z:
#     print(y)
# else:
#     print(z)

small = x if (x < y and x < z) else (y if y < z else z)
print(small)