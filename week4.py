#Fibonacci sequence
"""n=int(input())
x,y=0,1
while n>0:
	print(x," ")
	z=x+y
	x=y
	y=z
	n-=1"""

#perfect number
"""n=int(input())
sum=0
i=1
while i<n:
	if (n%i)==0:
		sum+=i
	i+=1
if sum==n:
	print("Perfect number")
else :
	print("Not perfect number")"""
	
#pattern printing
"""n=int(input())
for i in range (1,n+1):
	for j in range (1,i+1):
		print("* ",end=" ")
	print("")"""
	
#Number pattern
"""n=int(input())
for i in range (1,n+1):
	for j in range (1,i+1):
		print( j,end=" ")
	print("")"""
	
#Alphabet printing
"""l=65
n=int(input())
for i in range (1,n+1):
	for j in range (1,i+1):
		print(chr(l),end=" ")
	l+=1
	print("")
	
#########
l=65
n=int(input())
for i in range (1,n+1):
	for j in range (1,i+1):
		print(chr(l),end=" ")
		l+=1
	print("")"""
	
#Pascal triangle
def fact(n):
	f=1
	for i in range (1,n+1):
		f*=i
	return f
n=int(input())
for i in range(0,n+1):
	for j in range(0,i+1):
		
		print(fact(i)//(fact(i-j)*fact(j))," ",end=" ")
	print("")
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
