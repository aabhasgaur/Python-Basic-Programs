l=int(input("Enter the lower limit:"))
u=int(input("Enter the lower limit:"))
for num in range(l,u):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
        if(num==sum):
            print(sum)
