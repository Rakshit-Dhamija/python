#function of values

#def calations():
    #z=int(input("Enter\n 0->Curved surface area\n 1->total surface area"))
from math import pi
from math import sqrt
u='units'
u2='Square units'
u3='Cube units'
rd1=0
#rd=0
ht=0
#bd=0
def space():
    print('\n')
def r():
    r=int(input('Radius:'))
    return r
def l():
    l=int(input('Length:'))
    return l
def b():
    b=int(input('Breadth:'))
    return b
def h():
    h=int(input('Hieght:'))
    return h
def L():
    while True:
        #global rd1
        #if rd1!=0 and ht!=0:
         #   L=sqrt(rd1**2+h**2)
          #  return L
        #elif rd1!=0 and if isinstance(ht,int):
         #   ht=h()
          #  L=sqrt(rd**2+ht**2)
           # return L
        #else:
        print('For entering slant hieght')
        print('1.By Radius and hieght')
        print('2.By directly giving value')
        ch=int(input('Enter choice:'))
        if ch==1:
            L=sqrt((r()**2)*(h()**2))
            return L
        else:
            L=int(input('Slant Hieght:'))
            return L
def s():
    s=int(input('Side:'))
    return s
def ba():
    ba=int(input('Enter base:'))
    return ba
def perimeter():
    while True:
        space()
        print('Select the shape for Perimeter:')
        print('1.Square')
        print('2.Rectangle')
        print('3.Circle')
        print('4.Triange')
        print('5.Exit')
        ch=int(input('Enter your choice:'))
        if ch==1:
            p=4*s()
            print('Perimeter of Square:',p,u)
        elif ch==2:
            p=2*(l()+b())
            print('Perimeter of Rectangle:',p,u)
        elif ch==3:
            p=2*pi*r()
            print('circumference of circle:',p,u)
        elif ch==4:
            p=3*s()
            print('Perimeter of triangle',p,u)
        elif ch==5:
            break
        else:
            print('Invalid choice! Enter again.')
            continue

def area():
    while True:
        space()
        print('Select the shape for Area')
        print('1.Square')
        print('2.Rectangle')
        print('3.Circle')
        print('4.Triange')
        print('5.Exit')
        ch=int(input('Enter your choice:'))
        if ch==1:
            a=s()**2
            print('Area of square:',a,u2)
        elif ch==2:
            a=l()*b()
            print('Area of ractangle:',a,u2)
        elif ch==3:
            a=pi*r()**2
            print('Area of circle',a,u2)
        elif ch==4:
            a=0.5*ba()*h()
            print('Area of triangle:',a,u2)
        elif ch==5:
            break
        else:
            print('Invalid choice! Enter again.')
            continue

def carea():
    while True:
        space()
        print('Select the shape for Curved surface area:')
        print('1.Cube')
        print('2.Cuboid')
        print('3.Cylinder')
        print('4.Cone')
        print('5.Hemisphere')
        print('6.Sphere')
        print('7.Exit')
        ch=int(input('Enter your choice:'))
        if ch==1:
            a=4*s()**2
            print('Curved Surface area for cube is:',a,u2)
        elif ch==2:
            a=2*h()*(l()+b())
            print('Curved Surface area for cuboid is:',a,u2)
        elif ch==3:
            a=2*pi*r()*h()
            print('Curved Surface area for cylinder is:',a,u2)
        elif ch==4:
            a=pi*r()*L()
            print('Curved Surface area for cone is:',a,u2)
        elif ch==5:
            a=2*pi*r()**2
            print('Curved surface area for hemisphere is:',a,u2)
        elif ch==6:
            print('There is no Curved surface area for sphere!')
        elif ch==7:
            break
        else:
            print('Invalid choice! Enter again.')
            continue
def tarea():
    while True:
        space()
        print('Select the shape for Total surface area:')
        print('1.Cube')
        print('2.Cuboid')
        print('3.Cylinder')
        print('4.Cone')
        print('5.Hemisphere')
        print('6.Sphere')
        print('7.Exit')
        ch=int(input('Enter your choice:'))
        if ch==1:
            a=6*s()**2
            print('Total Surface area for cube is:',a,u2)
        elif ch==2:
            ln=l()
            bh=b()
            ht=h()
            #print(ln,bh,ht)
            a=2*((ln*bh)+(bh*ht)+(ln*ht))
            print('Total Surface area for cuboid is:',a,u2)
        elif ch==3:
            rd=r()
            a=2*pi*rd*(rd+h())
            print('Total Surface area for cylinder is:',a,u2)
        elif ch==4:
            global rd1
            rd1=r()
            a=pi*rd1*(rd1+L())
            print('Total Surface area for cone is:',a,u2)
        elif ch==5:
            a=3*pi*r()**2
            print('Total surface area for hemisphere is:',a,u2)
        elif ch==6:
            a=4*pi*r()**2
            print('Total surface area for sphere is:',a,u2)
        elif ch==7:
            break
        else:
            print('Invalid choice! Enter again.')
            continue
        rd1=0
    

def vol():
    while True:
        space()
        print('Select the shape for Volume:')
        print('1.Cube')
        print('2.Cuboid')
        print('3.Cylinder')
        print('4.Cone')
        print('5.Hemisphere')
        print('6.Sphere')
        print('7.Exit')
        ch=int(input('Enter your choice:'))
        if ch==1:
            v=s()**3
            print('Volume for cube is:',v,u3)
        elif ch==2:
            v=l()*b()*h()
            print('Volume for cuboid is:',v,u3)
        elif ch==3:
            v=pi*r()**2*h()
            print('Volume for cylinder is:',v,u3)
        elif ch==4:
            v=(1/3)*pi*r()**2*h()
            print('Volume for cone is:',v,u3)
        elif ch==5:
            v=(2/3)*pi*r()**3
            print('Volume for hemisphere is:',v,u3)
        elif ch==6:
            v=(4/3)*pi*r()**3
            print('Volume for sphere!',v,u3)
        elif ch==7:
            break
        else:
            print('Invalid choice! Enter again.')
            continue

while True:
    space()
    print('Calculations:')
    print('1.Perimeter')
    print('2.Area of 2-D figure')
    print('3.Curved surface area for 3-D figure')
    print('4.Total surface area for 3-D figure')
    print('5.Volume')
    print('6.Exit')
    ch=int(input('Enter choice:'))
    if ch==1:
        perimeter()
    elif ch==2:
        area()
    elif ch==3:
        carea()
    elif ch==4:
        tarea()
    elif ch==5:
        vol()
    elif ch==6:
        break
    else:
        print('Invalid choice! Enter again.')
        continue
