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
per=(sum*100)/600
print("percentage",per)
if per<33:
    print("You are Fail")
elif per>=33 and per<45:
    print("You are Passed Third division")
elif per>=45 and per<60:
    print("You are Passed second division")
elif per>=60:
    print("You are Passed First division")