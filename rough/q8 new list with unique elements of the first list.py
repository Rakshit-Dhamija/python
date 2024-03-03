#Write a Python function that takes a list and
#returns a new list with unique elements of the
#first list.
def unique_list(l):
    nlist=[]
    for i in l:
        if i not in nlist:
            nlist.append(i)
        else:
            continue
    print(nlist)

list1=list(eval(input("Enter the list")))
unique_list(list1)
