# WAP to creat a dictionary with the roll number, names and marks of n students
#in a class and display the names of students who have marks above 35.

n=int(input("How many students="))
stu={}
for i in range(1,n+1):
    print("Enter details of student",(i))
    rollno=int(input("Roll number:"))
    name=input("Name:")
    marks=float(input("Marks:"))
    d={"Roll_no":rollno,"Name":name,"Marks":marks}
    key="stu"+str(i)
    stu[key]=d
print("Students with marks>75 are:")
for i in range(1,n+1):
    key="stu"+str(i)
    if stu[key]["Marks"]>=35:
        print(stu[key])
