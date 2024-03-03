#WAP to perform the following task based on user choice
#a.Area of circle     b.Area of Rectangle
#c.Circimference of circle  d. Perimeter of rectangle

length=float(input('Enter the length='))
breadth=float(input('Enter the Breadth='))
radius=float(input('Enter the Radius='))

area_circle=3.14*(radius*radius)
area_rect=length*breadth
circumference_circle=2*3.14*(radius)
perimeter_rect=2*(length+breadth)

print("a. Area of circle=",area_circle)
print("b. Area of rectangle=",area_rect)
print("c. Circumference of circle=",circumference_circle)
print("d. Perimeter of rectangle=",perimeter_rect)
