#Write a Python function that checks whether
#a passed stringis palindrome or not
def palindrome(s):
    if s==s[::-1]:
        print("str is palindrome")
    else:
        print("str is not a palindrome")

s1=input("Enter the string")
palindrome(s1)
    
