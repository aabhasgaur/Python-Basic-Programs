#num=int(input("Enter the range of the Fibonacci series: "))
num=10
n1,n2=0,1
print("The Fibonnaci series for the given range is ",n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()
