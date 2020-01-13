# for i in range(0,100):
#     if i%2==1:
#         print(i)
# for i in range(1,100,2):
#     print(i,end=' ')

# while True:
#     print(True)

# x%2==1
# x%3==2
# x%5==4
# x%6==5
# x%7==0
# for x in range(1000):
#     if x%2==1:
#         if x%3==2:
#             if x%5==4:
#                 if x%6==5:
#                     if x%7==0:
#                         print(x,end=' ')
#                         break;

x = 7
i = 1
flag = 0
while i <= 100:
    if(x%2==1)and(x%3==2)and(x%5==4)and(x%6==5):
        flag =1
        break;
    else:
        x= 7*(i+1)
    i+=1

if flag==1:
    print(x)
else:
    print('no')

                    

