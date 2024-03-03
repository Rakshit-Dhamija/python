#Write a Python function to check whether a number is in a given range.

def Range(num):
    a=int(input("Enter the first number of range:"))
    b=int(input("Enter the second number of range:"))
    c=int(input("Enter if any step or 1:"))
    range_1=range(a,b,c)
    if num in range_1:
        print(num,"is in the range.")
    else:
        print(num,"not in range")    

num1=int(input("enter the number:"))
Range(num1)
