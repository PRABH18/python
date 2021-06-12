a=int(input("enter any number"))
b=int(input("enter any number"))
c=int(input("enter any number"))
print("a=",a," b=",b," c=",c)
if a>b:
    if a>c:
        print("A is greatest")
    else:
        print("C is greatest")
elif b>c:
    print("b is greatest")
else:
    print("C is greatest")
