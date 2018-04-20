class Potato:
	def __init__ (self,name):
		self.name = name

	def kick(self):
		print(self.name)

p = Potato('土豆')
p.kick()

p = Potato('花生')
p.kick()


# class Persion:
# 	__name = '刁'
# p = Persion()

# print(p.__Persion__name)

# 内部访问python

class Persion:
	def __init__(self,name):
		self.__name = name
	def getName(self):
		return self.__name

p = Persion('diao ')

# print(p.__name)
print(p.getName())
		

class Parent:
	def hello(self):
		print('正在调用父类的方法。。。。')

class Child(Parent):
	pass

p = Parent()

print(p.hello())

c = Child()
print(c.hello())


class Ball:
	def __init__(self,name):
		self.name = name
	def kick(self):
		print("我叫"+ self.name + "别替我")

b = Ball('土豆')
b.kick()


# 继承

class Parent:
	def hello(self):
		print("12456")

class Child(Parent):
	pass

c = Child()
print(c.hello())