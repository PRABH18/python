import os
print("1. Press 1 to Shutdown")
print("2. Press 2 to Restart")
print("3. Press 3 to Exit")
option=int(input("\n Enter your option"))
if option>=1 and option<2:
    if option==1:
        os.system("shutdown \s \t 1")
    else:
        os.system("restart \r \t 2")
else:
    exit()
