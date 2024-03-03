#creating 2 even and odd list from one list

a=eval(input("Enter the list="))
l1=[]
l2=[]
for (i) in range(len(a)):
    if a[i]%2==0:
        l1.append(a[i])
    else:
        l2.append(a[i])
print(l1)
print(l2)
       
