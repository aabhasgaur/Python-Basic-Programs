num=int(input("Enter a number: "))
factors=[ ]
for i in range(1,num):
    if (num%i==0):
        factors.append(i)
print("Factors of the given number are: ",factors)
