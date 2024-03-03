#WAP to enter marks in 5 subjects if percentage>33 then print if student is
#pass or fail. Also find the grade based of table.
#Percentage     Grade
# >=90            A
# >=80            B
# >=70            C
# >=60            D


English=int(input("Marks of English="))
Physics=int(input("Marks of Physics="))
Chemistry=int(input("Marks of Chemisty="))
Maths=int(input("Marks of Maths="))
ComputerSci=int(input("Marks of Computer Science="))

avg=(English+Physics+Chemistry+Maths+ComputerSci)//5

print("Percentage=",avg)

if avg>=90:
   print("Grade=A")
   print("Pass")
elif avg>=80:
   print("Grade=B")
   print("Pass")
elif avg>=70:
   print("Grade=C")
   print("Pass")
elif avg>=60:
   print("Grade=D")
   print("Pass")
elif avg>=34:
    print("Pass")
elif avg<=33:
    print("Fail") 
 
