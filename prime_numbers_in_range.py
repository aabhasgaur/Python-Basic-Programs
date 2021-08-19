li=[]
n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))
for i in range(n1,n2):
    f=0
    for j in range(2,i//2):
        if(i % j == 0):
            f=1
            break
    if f==0:
        li.append(i)
else:
    print("Prime Numbers in the given range are:",li)
