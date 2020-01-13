#
#编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹包含子文件夹，则进入子文件夹继续搜索）所有含有
#该关键字的文本文件（.txt后缀），要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符）
#
#

#请将该脚本放于待查的文件夹内，请输入关键字：#小甲鱼
#请问是否需要打印关键字【小甲鱼】在文件中的具体位置（YES/NO）：#yes


#1 打印关键字在文件中的具体位置
text_num = 0
text_local = []
def text_search(search_text,each_file):
    #在文件中查找关键字出现的次数
    for each_line in each_file:
        if search_text in each_line:
            text_num += 1
            text_local = f.tell(each_file)
            print()    
        
    f.close(each_file)