#Open a file in binary write mode
f=open('sample.bin','wb')
#Write binary data to the file
f.write(b'\x01\x02\x03\x04\x05')
#open a file in binary read mode
f=open('sample.bin','rb')
#Reading binary data
print(f.read())

