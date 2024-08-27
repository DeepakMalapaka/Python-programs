#Arthematic operations
"""def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def floor_div(a,b):
	return a//b
print("Enter two numbers to perform basic arthematic operations using functions:")	
a=int(input())
b=int(input())
print(add(a,b),sub(a,b),mul(a,b),div(a,b),floor_div(a,b))"""

#Function multiple return values
"""def wishing(lan):
	if lan=="tel":
		return "Namaskaram"
	elif lan=="eng":
		return "Hello"
	elif lan=="hin":
		return "Namaskar"
lan=input("Enter your lang:")
print(wishing(lan))"""

#Gcd of two numbers


#Max and min in list
"""def maximum(list):
	print(max(list))
def minimum(list):
	print(min(list))
list=[1,2,3,4]
maximum(list)
minimum(list)"""

#Second largest element in the list
"""def second_max(list):
	x=max(list)
	list.remove(x)
	print(max(list))
list=[1,2,3,4]
second_max(list)"""

#Flattening the list
def Flattening_the_list(list):
	l=[]
	for i in list:
		for j in i:
			l.append(j)
	print("The flattend list is:",l)
list=[[1,2,3],[4,5,6],[7,8,9]]
Flattening_the_list(list)

#Reversing a list
def Rev(l):

n=int(input("Enter the size of "))




