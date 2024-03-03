#product of each number of list

def product_list(l):
    s=1
    for i in l:
        #print(i)
        s=s*i
    return s

list1=list(eval(input("Enter the list:")))
print(list1)
product=product_list(list1)
print(product)
