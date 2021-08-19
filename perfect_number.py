num=int(input("Enter a number: "))
temp=0

for i in range(1,num):
    if(num%i==0):
        temp=temp+i
if(temp==num):
    print("Yes")
else:
    print("No")
