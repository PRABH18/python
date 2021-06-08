from Result import math

print("area of trangle")
a=float(input("enter the value of a"))
b=float(input("enter the value of b"))
c=float(input("enter the value of c"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of trangle is",area)