#find the max in three numbers
def Max():
    l=[]
    for i in range(3):
        a=int(input("Enter the number:"))
        l.append(a)
    print("max in these is:",max(l))
    print(l)


Max()
