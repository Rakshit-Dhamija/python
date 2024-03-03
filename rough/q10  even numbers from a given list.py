#Write a Python program to print the even
#numbers from a given list.
def list_even(l):
    elist=[]
    for i in l:
        if i%2==0:
            elist.append(i)
        else:
            continue
    return elist   

List=list(eval(input("Enter the list")))
nlist=list_even(List)
print(nlist)
            
