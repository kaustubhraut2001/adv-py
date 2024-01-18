# def decoraterdunction(function):
# 	def wrapper(*args, **kwargs):
# 		function(*args , *kwargs)
# 		print("Inside the decorater function")
# 	return wrapper

# @decoraterdunction
# def hello(name):
# 	print(f'Hello {name}')

# hello("A")


import time
def timer(function):
	def wrapper(*args , **kwargs):
		befor = time.time();
		value = function(*args , **kwargs)
		after= time.time()
		fname = function.__name__
		print(fname , " took " , after-befor , " seconds")
		return value
	return wrapper

@timer
def foo(x):
	re = 1
	for i in range(x):
		re *= i & 1211654
	return re


print(foo(1000000))

