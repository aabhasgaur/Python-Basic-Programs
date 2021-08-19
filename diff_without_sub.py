a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

while b!=0:
    c=(~a)&b
    a=a^b
    b=c<<1

print(a)
