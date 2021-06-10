          #Additiom Subtraction, Multiplication, Division

print("1=Addition","2=Subtract","3=multiply","4=Divide")
num=float(input("Choose Any one 1,2,3,4 =" ))
if num==1:
    a=float(input("Enter The First Number"))
    b = float(input("Enter The Second Number"))
    c=a+b
    print("Addition a+b= ",c)
elif num == 2:
        e= float(input("Enter The First Number"))
        f= float(input("Enter The Second Number"))
        g = e-f
        print("Subtract e-f = ", g)
elif num == 3:
        p = float(input("Enter The First Number"))
        q = float(input("Enter The Second Number"))
        r = p*q
        print("Multiply p*q = ", r)
elif num == 4:
        x = float(input("Enter The First Number"))
        y = float(input("Enter The Second Number"))
        z = x / y
        print("Division x/y = ", z)
