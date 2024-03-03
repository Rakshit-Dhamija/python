#Write a Python Program to Count the Number
#of Blank Spaces in a Text File

file=open("text.txt","r")
l=list(file.read())
#print(l)
c=l.count(input("Enter the word to be found:"))
print("the occurance:",c)
file.close()
