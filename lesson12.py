# list1=[1,[1,2,['小甲鱼'],3,5,8,13,18]]
# list1[1][2][0]='小鱿鱼'
# print(list1)

# list1.sort()
# print(list1)
# list1=[(x,y)for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
# print(list1)
list1=[]
for x in range(10):
    for y in range(10):
        if x%2==0:
            if y%2!=0:
                list1.append((x,y))
                print(list1)