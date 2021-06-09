                         #leap Year
year=int(input("Enter The Year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("This IS The Leap year", year)
        else:
            print("This Is Not a Leap year",year)
    else:
        print("This Is a Leap year",year)
else:
    print("This is Not a Leap year",year)
