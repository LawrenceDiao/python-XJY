
#__init__()

class Rectangle:
	def __init__(self,x,y):
		self.x =x
		self.y = y

	def getPeri(self):
		return(self.x + self.y) *2
	def getArea(self):
		return self.x * self.y

rect = Rectangle(3,4)
print(rect.getArea())
print(rect.getPeri())



#__new__(cls[,...])

class Capstr(str):
	def __new__(cls,string):
		string=string.upper()
		return str .__new__(cls,string)

a = Capstr("i love you")
print(a)