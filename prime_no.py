n=5
i=2
while i<=n-1:    # 2,3,4
    if n%i==0:
        print("Not prime")
        break
    i = i + 1

else:  # loop else will be executed when loop  runs properly
    print("Prime no")
