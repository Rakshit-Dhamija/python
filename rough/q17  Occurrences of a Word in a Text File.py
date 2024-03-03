#Write a Python Program to Count the Occurrences
#of a Word in a Text File
file=open("text.txt","r")
l=file.read()
#print(l)
x=l.split()
c=x.count(input("Enter the word:"))
print("the occurance:",c)
file.close()
