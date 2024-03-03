#WAP to convert upper case into lower case and lower case into upper case in
#a given string.


a=input("Enter a string=")
new_str=""
for i in range (len(a)):
    if a[i].isupper():
        new_str+=a[i].lower()
    elif a[i].islower():
        new_str+=a[i].upper()
    else:
        new_str+=a[i]
print(new_str)
