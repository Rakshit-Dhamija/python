#Write a Python Program to Read the Contents of a File.

a=open("text.txt","r")
lines=a.readlines()
for line in lines:
    print(line,end=" ")
a.close()    
