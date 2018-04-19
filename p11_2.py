import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置是" ,self.x,self.y)

class Goldfish(Fish):
    pass
class Garp(Fish):
    pass
class Salmon(Fish):
    pass



class Shark(Fish):
    def __init__(self):

        # 1方法 解决新的init 方法没有初始化鲨鱼的坐标
        # Fish.__init__(self)

        # 使用super（）函数
        super().__init__()
        self.hungary = True
    def eat(self):
        if self.hungary:
            print("我是个吃货")
            self.hungary = False
        else:
            print("饱了·····")

fish = Fish()

print(fish.move())

goldfish = Goldfish()

print(goldfish.move())
print(goldfish.move())
print(goldfish.move())

shark = Shark()
print(shark.eat())
print(shark.eat())

print(shark.move())


# 多重继承

class Base1:
    def fool(self):
        print("我是fool 我在base1：")

class Base2:
    def fool2(self):
        print("我是fool2 我在base2")
class Base(Base1,Base2):
    pass

c = Base()
print(c.fool())
print(c.fool2())