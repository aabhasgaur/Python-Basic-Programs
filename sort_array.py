size=int(input("Enter the size of array: "))
a=[]
for i in range(size):
    element=int(input())
    a.append(element)
print(a)
a.sort()
print(a)
