#Write a Python Program to Read a File
#and Capitalize the First Letter of
#every word in the file.
a=open("text.txt","r")
y=[]
data=a.read()
x=data.split()
for i in x:
    y.append(i.title())
print(y)    
a.close()
