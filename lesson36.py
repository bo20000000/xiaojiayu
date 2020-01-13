#0.对象中的属性和方法，在编程中实际是什么？
#属性就是变量，方法就是过程
# class Cat:
#     color = 'black'
#     leg = 4
#     tail = 'long'
#     def walk(self):
#         print("我在溜达")
#     def run(self):
#         print("我在跑")
#     def eat(self):
#         print("我在吃东西")

# cat = Cat()
# cat.walk()

# class Person:
#     name = "小甲鱼"
#     def print_name(self):
#         print(self.name)

# person = Person()
# person.print_name()

class Rectangle:
    long = 5.00
    wide = 4.00
    def setRect(self):
        print("请输入矩形的长和宽。。。。。")
        self.long = float(input("请输入长："))
        self.wide = float(input("请输入宽："))

    def getRect(self):
        print('这个矩形的长是%.2f宽是%.2f' %(self.long,self.wide))
    def getArea(self):
        return self.long*self.wide

rectangle = Rectangle()
rectangle.setRect()
rectangle.getRect()  
        