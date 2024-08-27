"""def name(n):
	print("Hello",n)
name("Deepak")"""
#Positional arguments
"""def add(a,b,c):
	print(a+b+c)
add(1,2,3)"""
#Default arguments
"""def add(a,b=1,c=2):
	print(a+b+c)
add(3)"""
#Keyword arguments
"""def add(a,b=1,c=2):
	print(a+b+c)
add(b=3,c=1,a=4)"""
#Variable length arguments
def f(name,*a):
	print("Friends of "+name+" are")
	for i in a:
		print(i)
f('a','b','c','d')
