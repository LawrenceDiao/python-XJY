class C():
	count = 0


a =C()
b =C()
c =C()

print(a.count)
a.count += 10
print(a.count)
C.count += 10
print(c.count)

C.count +=100
print(c.count)


class CC:
	def setXY(self ,x,y):
		self.x = x
		self.y =y
	def printXY(self):
		print(self.x,self.y)

dd=CC()
a = dd.__dict__

print(a)

dd.setXY(4,5)
a = dd.__dict__
print(a)


# Bif 内置函数

# issubclass（class, classinfo）

class A:
	pass

class B(A):
	pass

print(issubclass(A,B))


# isinistance(object,classinfo)

b1 = B()

print(isinstance(b1,B))

# hasattr(object,name)

class C:
	def __init__(self,x=0):
		self.x = x
c1 = C()

print(hasattr(c1,"x"))

# getarrt(object,name[,default])

print(getattr(c1,"y","木有"))

# setattr(object,name)
setattr(c1,"y","刁")
print(getattr(c1,"y","木有"))
# delattr(object,name)
print(delattr(c1,"y"))
print(getattr(c1,"y","木有"))



###########property()

class C:
	def __init__(self,size = 10):
		self.size = size
	def getSize(self):
		return self.size
	def setSize(self):
		self.