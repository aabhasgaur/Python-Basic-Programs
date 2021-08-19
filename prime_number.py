factors=[]
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if(n % i == 0):
        factors.append(i)
if(len(factors)==2):
    print("The given number is a Prime Number.")
else:
    print("The given number is NOT a Prime Number.")
print("Factors of the given number are ",factors)
