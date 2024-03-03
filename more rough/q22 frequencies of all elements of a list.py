#Frequencies of all elements of a list

L=eval(input("Enter the numbers"))
l1=[]
l2=[]
for i in L:
    if i not in l2:
        x=L.count(i)
        l1.append(x)
        l2.append(i)

print("Element",'\t\t',"Frequency")
for i in range (len(l1)):
    print(l2[i],'\t\t\t',l1[i])
