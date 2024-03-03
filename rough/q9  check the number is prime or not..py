#Write a Python function that takes a number as a
#parameter and check the number is prime or not.
def prime(a):
    count=0
    if a==1:
        print("input another number")
        a=int(input("Enter the number to check if it is prime or not"))
    for i in range(2,a):
        #print(i)
        if a%i==0:
            count+=1
        else:
            continue
    if count>0:
        print("the input number is a not prime number.")
    else:
        print("the input number is a prime number")
            
num=int(input("Enter the number to check if it is prime or not"))
prime(num)
