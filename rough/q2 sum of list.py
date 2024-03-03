#Sum of all numbers of list
def sum_list(l):
    print(l)
    return sum(l)

list1=list(eval(input("Enter the list:")))
s=sum_list(list1)
print("Sum of list is:",s)
