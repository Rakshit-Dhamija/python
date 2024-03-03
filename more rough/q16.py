#write a program to count the number of vowles in a line

string=input("Enter the line=")
l=list(string)
v=("A,E,I,O,U,a,e,i,o,u")
count=0

for i in l:
    if i in v:
        count+=1

print("Number of vowles are=",count)        
        
