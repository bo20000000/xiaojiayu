def rab(n):
    if n<1:
        print('输入的数据有误！')
        return -1
    if n==1 or n==2:
        return 1
        
    else:
        return rab(n-1)+rab(n-2)

result = rab(100)
if result != -1:
    print('共有%d对小兔崽子' %result )

