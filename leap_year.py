try:
    year = int(input("Enter the year"))
    print("Year=", year)
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap Year")
    elif year % 4 == 0:
        print("Leap year")
    else:
        print("Not leap year")
except Exception:
    print("Year Cannt be character")
