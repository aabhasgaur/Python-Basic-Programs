num=int(input("Enter the range of the Tribonacci series: "))
n1,n2,n3=0,0,1
print("The Tribonnaci series for the given range is ",n1,n2,n3,end=" ")
for i in range(2,num):
    n4=n1+n2+n3
    n1=n2
    n2=n3
    n3=n4
    print(n4,end=" ")

print()
