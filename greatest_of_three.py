a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

d=a if a>b and a>c else b if b>a and b>c else c
e=a if a<b and a<c else b if b<a and b<c else c
print("Largest of three:",d)
print("Smallest of three:",e)
