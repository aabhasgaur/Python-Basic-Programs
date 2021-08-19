n=int(input("Enter a number:"))
sq=n*n
co=0
while(n>0):
    if(n%10!=sq%10):
        print("Not Automorphic")
        co=1
        break
    n=n//10
    sq=sq//10

if(co==0):
    print("Automorphic")
