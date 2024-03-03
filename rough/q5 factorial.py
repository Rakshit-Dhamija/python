# factorial of non negative number
def factorial(a):
    for i in range(1,a):
        if a<0:
            print("input a number greater than 0")
        else:
            a=a*i
    return a

num=int(input("Enter the number for factorial:"))
f=factorial(num)
print(f)
        
