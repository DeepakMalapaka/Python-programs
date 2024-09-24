#Write
f=open('sample.txt','w')
f.write("Hello world,I'm Deepak\n")
#Append
f=open('sample.txt','a')
f.write("Home town Bhimavaram\n")
f.write("Studying in Vishnu institute of technology\n")
#Read
print("-->Reading multiple lines at a time\n")
f=open('sample.txt','r')
print(f.read())
print("-->Reading single line\n")
f=open('sample.txt','r')
print(f.readline())
print("-->Reading lines and printing in a list\n")
f=open('sample.txt','r')
print(f.readlines())
#Write lines
lines=["Second year\n","Cse\n","Sec-C\n","23PA1A05E2\n"]
print()
f=open('sample.txt','a')
f.writelines(lines)
f=open('sample.txt','r')
print(f.read())
#Tell
f=open('sample.txt','r')
content=f.read(10)
print("Current Position",f.tell())
#Seek 
f=open('sample.txt','r')
print("Initial position:",f.tell())
f.seek(10)
print("Position after seeking:",f.tell())
print(f.read(5))
print("Position after read :",f.tell())
f.close()
