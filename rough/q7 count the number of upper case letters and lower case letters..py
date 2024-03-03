#Write a Python function that accepts a string
#and calculate the number of upper case letters
#and lower case letters.
def count_letters(s):
    lcount=0
    ucount=0
    for i in s:
        if i.isupper():
            ucount+=1
        if i.islower():
            lcount+=1
    print("number of lowercase:",lcount)
    print("number of upercase:",ucount)

str1=input("Enter the str")
count_letters(str1)
    
