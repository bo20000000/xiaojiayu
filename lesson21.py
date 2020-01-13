# def fun_A(x,y=3):
#     return x*y

# result=lambda x,y=3:x*y
# print(result(3,))

# lambda x:x if x%2 else None

# def fun_B(x):
#     if x%2:
#         return x
#     else:
#         return None

# 3.你可以利用lambda和filter（）表达式快速求出100以内的所有3的倍数么？
# lambda x:x if x%3 else None
# result = filter(lambda x:x if x%3==0 else None,range(100))
# print(list(result))

def make_repeat(n):
    # def fun_A(s):
    #   s=s*n
    return lambda s:s*n
double = make_repeat(2)
#n = 2
print(double(8))
print(double('FishC'))
