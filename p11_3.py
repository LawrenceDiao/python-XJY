
#组合 

class Turtle:
	def __init__(self,x):
		self.num = x
class  Fish():
	def __init__(self,x):
		self.num = x
class Pool():
	def __init__(self,x,y):
		self.turtle = Turtle(x)
		self.fish = Fish(y)
	def print_num(self):
		print("水池里共有%d 只小乌龟 和 %d 只小鱼"%(self.turtle.num,self.fish.num))

pool =Pool(1,10)
print(pool.print_num())