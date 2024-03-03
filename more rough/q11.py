#Write a program to print pattren.
#(i)1       (ii)54321    (iii)A      (iv)X
#   12          4321          AB         XX
#   123         321           ABC        XXX 
#   1234        21            ABCD       XXXX
#               1             ABCDE

print('(i)')
for i in range(2,6,1):
    for j in range(1,i,1):
        print(j, end='')
    print( )
    
print( )
print('(ii)')
for a in range(5,0,-1):
    for b in range(a,0,-1):
        print(b, end ='')
    print( )

print( )
print('(iii)')
for c in range(65,71):
    for d in range(65,c):
        print(chr(d), end='')
    print( )
    
print( )
print('(iv)')
for e in range(0,5):
    for f in range(e):
        print(chr(f), end='X')
    print( )    
