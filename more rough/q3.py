#WAP to find the largest number among three inputed numbers

n1=int(input("Enter first number="))
n2=int(input("Enter second number="))
n3=int(input("Enter third number="))

large=n1
if large<n2:
    large=n2
if large<n3:
    large=n3
print("Largest number =",large)    
