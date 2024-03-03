#Write a Python Program to Copy the
#Contents of One File into Another
file=open("text.txt","r")
l=file.read()
#print(l)
file1=open("text2.txt","w")
a=file1.writelines(l)
file.close()
file1.close()
