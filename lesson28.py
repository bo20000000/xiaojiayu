# f = open('loveyou.mp3','rb')
# for each_line in f:
#     print(each_line,end='')
# f.close()

f1 = open('loveyou.mp3')
f2 = open('loveyou.txt','xb')
f2.write(f1.read())
f2.close()
f1.close()
