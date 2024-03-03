#Write a Python function to check whether a
#number is perfect or not
def perfect_number(num):
    new=0
    for i in range(1,num+1):
        #print(i)
        if num%i==0:
            new+=i
            #print(new)
        else:
            continue
    if new/2==num:
        print(num,"is a perfect number")
    else:
        print(num,"is not a perfect number")

n=int(input("Enter the number"))
perfect_number(n)
