import math
print("enter the coffecients of quadratic equation")
a=float(input("Enter the value of a"))
b=float(input("Enter the value of b"))
c=float(input("Enter the value of c"))
print("a=",a," b=",b," c=",c)
d=b*b-4*a*c
print("D=",d)
if d==0:
    print("Roots are real and equal")
    x1=-b/(2*a)
    x2=x1
    print("Roots are x1=",x1," x2=",x2)
elif d>0:
    print("Roots are real and unequal")
    x1=(-b+math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are x1=", x1, " x2=", x2)
elif d<0:
    print("roots are imaginary")

