#Write a Python Program to Count the Number of
#Lines in a Text File
a=open("text.txt","r")
lines=a.readlines()
#print(lines)
print("Number of lines are:",len(lines))
a.close()
