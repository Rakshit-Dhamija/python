# WAP to print the list in ascending and descending orders

l=list(eval(input("Enter the list=")))
print("Orignal List:", l)
l.sort()
print("Ascending Order:", l)
l.sort(reverse=True)
print("Descending Order:", l)
