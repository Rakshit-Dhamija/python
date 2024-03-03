#Write a Python Program to Read a Text File
#and Print all the Numbers Present in the
#Text File
a=open("text4.txt","r")
b=a.read()
count=[]
for i in b:
    if i.isdigit():
        count.append(i)
    else:
        continue
print("the digits are:",count)
a.close()
        
