#Reverse a string
"""s=input("Enter a string:")
rev_s=s[::-1]
print("The reversed string is:"+rev_s)"""

#Reverse a string without using a slicing operator
"""s=input("Enter a string:")
rev_s=""
for i in s:
	rev_s=i+rev_s
print("The reversed string is:"+rev_s)"""

#Palindrome or not
"""s=input("Enter a string:")
rev_s=s[::-1]
if (rev_s==s):
	print("The entered string is a palindrome")
else :
	print("The entered string is a not a palindrome")"""
	
#Length of a string 
"""s=input("Enter a string:")
x=0
for i in s:
	x+=1
print("The length of entered string is",x)"""

#Number of vowels and consonants in a string
"""s=input("Enter a string:")
x='aeiouAEIOU'
v,c=0,0
for i in s:
	if i in x:
		v+=1
	else :
		c+=1
print("Number of vowels are:",v,"and number of consonants are:",c)"""

#Even length words printing
"""s=input("Enter a string:").split()
for i in s:
	if len(i)%2==0:
		print(i)"""

 

