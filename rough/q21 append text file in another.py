#Write a Python Program to Append the Contents
#of One File to Another File
file=open("text.txt","r")
l=file.read()
print(l)
file1=open("text3.txt","a")
b=file1.writelines("\n")
a=file1.writelines(l)
file.close()
file1.close()
