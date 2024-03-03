#Write a Python Program to Read a String from
#the User and Append it into a File
a=open("text1.txt","a")
s=list(input("Enter the string:"))
z=a.writelines(s)
a.close

a=open("text1.txt","r")
c=a.readlines()
print(c)
a.close
