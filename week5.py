#Sum and average of list
"""l=[]
n=int(input("Enter the size of list:"))
print("Enter",n,"number of elements:")
for i in range (n):
	x=int(input())
	l.append(x)
print("The sum of elements in a list is:",sum(l))
print("The average of elements in list is:",(sum(l)/n))"""

#Reverse a list
"""l=[]
n=int(input("Enter the size of list:"))
print("Enter",n,"number of elements:")
for i in range (n):
	x=int(input())
	l.append(x)
l1=l[::-1]
print(l1)
l.reverse()
print(l)"""

#Exchange first and last
""" l=[]
n=int(input("Enter the size of list:"))
print("Enter",n,"number of elements:")
for i in range (n):
	x=int(input())
	l.append(x)
l[0],l[-1]=l[-1],l[0]
print(l)"""

#Remove first occurence
"""l=[]
n=int(input("Enter the size of list:"))
print("Enter",n,"number of elements:")
for i in range (n):
	x=int(input())
	l.append(x)
x=int(input("Enter a number to remove:"))
l.remove(x)
print(l)"""

#Extract even and odd number
"""l=[]
n=int(input("Enter the size of list:"))
print("Enter",n,"number of elements:")
for i in range (n):
	x=int(input())
	l.append(x)
even=[]
odd=[]
for i in range(n):
	if(l[i]%2==0):
		even.append(l[i])
	else :
		odd.append(l[i])
print("The even are",even,"The odd are",odd)"""

#position of max and min
"""l=[]
n=int(input("Enter the size of list:"))
print("Enter",n,"number of elements:")
for i in range (n):
	x=int(input())
	l.append(x)
a=l.index(max(l))
b=l.index(min(l))
print("The max position is",a,"and the min position is",b)"""

#concate two lists 
l1=["M","na","i","Abhi"]
l2=["y","me","s","Ram"]
l=[]
print(list(zip(l1,l2)))
for i in range (len(l1)) :
	l.append(l1[i]+l2[i])
print(l)
















