#Packing and unpaking tuple

T=eval(input("Enter 5 numbers="))
a,b,c,d,e=T
z=int(input("enter the number to be replaced instead of 3rd number"))
c=z
print(a)
print(b)
print(c)
print(d)
print(e)
T=(a,b,c,d,e)
print("Tuple",T)
