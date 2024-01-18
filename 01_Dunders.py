class Vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	# def __del__(self):
	# 	print("Object is destructed")
	def __add__(self , other):
		return Vector(self.x + other.x , self.y + other.y)

	def __str__(self) -> str:
		return "Vector({},{})".format(self.x,self.y)



v1 = Vector(2,5)
v2 = Vector(5,-2)
v3 = v1 + v2
print(v3.x , v3.y)
