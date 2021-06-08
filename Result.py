                                            #Result

hindi=int(input("Enter the number"))
english=int(input("Enter the  number"))
math=int(input("Enter the  number"))
computer=int(input("Enter the  number"))
physics=int(input("Enter the  number"))
chemistry=int(input("Enter the  number"))
print("hindi",hindi, "english",english,"math",math, "computer",computer, "physics",physics, "Chemistry",chemistry)

sum=hindi+english+math+computer+physics+chemistry
print("sum=",sum)
per=sum/6
print("percentage",per)
if per>60:
    if per>=45:
        print("First Division")
    else:
        print("Third Division")
elif per>=33:
    print("Sec Division")
else:
    print("Fail")

