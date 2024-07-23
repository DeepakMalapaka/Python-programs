#sum of natural numbers
"""sum=0
for i in range(1,11):
	sum=sum+i
print("Sum is:",sum)
s=0
i=1
while i<11:
	s=s+i
	i+=1
print("Sum is:",s) """
#Tables 
"""n=int(input())
for i in range (1,11):
	print(n,"x",i,"=",n*i,"\n")
x=int(input())
j=1
while j<11:
	print(x,"x",i,"=",x*i,"\n")
	j+=1"""
#string and it's length
"""s=input()
for i in s:
	print(i)
print(len(s))"""
#Factorial of a given number
"""n=int(input())
fact=1
for i in range(n,0,-1):
	fact=fact*i
print("Factorial is:",fact)"""
# prime number or composite number
"""n=int(input())
count=0
for i in range(2,n):
	if n%2==0:
		count+=1
if count:
	print("Not a Prime Number")
else :
	print("Prime Number")"""
#sum of the digits
"""n=int(input())
sum=0
while n!=0:
	remainder=n%10
	sum=sum+remainder
	n //=10
print("Sum is:",sum)"""
#Reverse of a number 
"""n=int(input())
sum=0
reverse=0
while n!=0:
	remainder=n%10
	n //=10
	reverse=reverse*10+remainder
print("Reversed number is:",reverse)"""
#Palindrome 
"""n=int(input())
x=n
reverse=0
while n!=0:
	remainder=n%10
	n //=10
	reverse=reverse*10+remainder
if reverse==x:
	print("Palindrome")
else:
	print("Not a palindrome")"""
#Armstrong number
"""n=int(input())
sum=0
x=n
m=n
i=0
while n!=0:
	remainder=n%10
	i=i+1
	n //=10
while m!=0:
	remainder=m%10
	sum=sum+(remainder**i)
	m //=10
if x==sum:
	print("Armstrong number")
else :
	print("Not a armstrong number")
