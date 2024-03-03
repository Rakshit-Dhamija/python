#Write a Python Program to Count the Number of Words in a Text File.

a=open("text.txt","r")
data=a.read()
x=data.split()
print("number of words:",len(x))
a.close()
