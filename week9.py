#Factorial Recursion
"""def fact(n):
	if n==0:
		return 1
	else :
		return n*fact(n-1)
a=int(input("Enter a number:"))
print("The factorial of",a,"is",fact(a))"""

#Fibonacci seqence
"""def fib(n):
	if n<=1:
		return n
	else :
		return (fib(n-1)+fib(n-2))
a=int(input("Enter the number of elements should be print:"))
if a<=0:
	print("please enter the positive number only")
else :
	for i in range(a):
		print(fib(i))"""
		
#GCD of two numbers using recursion
"""def gcd_fun(a,b):
	if b==0:
		return a
	else :
		return gcd_fun(b,a%b)
a=int(input("Enter the first input:"))
b=int(input("Enter the second input:"))
print("The gcd of entered numbers",a,",",b,"is",gcd_fun(a,b))"""

#Finding key in a dictionary
"""dict1={
1:"Hello",
2:"World",
3:"This",
4:"is",
5:"Deepak"
}
key=int(input())
if key in dict1.keys():
	print("Key is found")
else :
	print("Key is not found")"""
	
#Add new key value pair to dictionary
"""dict1={
1:"Hello",
2:"World",
3:"This",
4:"is",
5:"Deepak"
}
dict1.update({6:"Balaji"})
print(dict1)"""

#Sum of values in dictionary
"""dict1={
1:"Hello",
2:"World,",
3:"This",
4:"is",
5:"Deepak"
}
sum=""
for i in dict1.values():
	sum=sum+i+" "
print(sum)"""

#Even or Odd using lambda function
n=int(input("Enter any number:"))
x=lambda n:n%2
if x(n)==0:
	print("Even")
else :
	print("Odd")
	 
