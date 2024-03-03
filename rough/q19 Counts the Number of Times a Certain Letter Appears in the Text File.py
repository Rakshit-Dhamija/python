#Write a Python Program that Reads a Text File and
#Counts the Number of Times a Certain Letter Appears
#in the Text File
file=open("text.txt","r")
l=list(file.read())
#print(l)
c=l.count(input("Enter the letter:"))
print("the occurance:",c)
file.close()
