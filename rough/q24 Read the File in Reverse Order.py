#Python Program to Read the Contents
#of a File in Reverse Order
a=open("text.txt","r")
b=a.read()
x=b.split()
c=x[::-1]
print(c)
