#fibonacci series till range


n=int(input("Enter the limit="))
a=0
b=1
c=a+b
for i in range(0,n):
      if n>=0:
            c=a+b
            a=b
            b=c
            print(c,end=",")
      else:
          print("put limit greater than 0")
    
