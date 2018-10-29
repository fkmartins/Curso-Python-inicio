import math

xa=int(input("Entre com xa:"))
xb=int(input("Entre com xb:"))
ya=int(input("Entre com ya:"))
yb=int(input("Entre com yb:"))

x=ya-xa
y=yb-xb
z=x**2
k=y**2
c=z+k
a=math.sqrt(c)

if a>=10:
    print("longe")
else:
    print("perto")
        

    
