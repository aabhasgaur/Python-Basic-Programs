size=int(input("Enter the size of array: "))
a=[]
for i in range(size):
    element=int(input())
    a.append(element)
#print("Reverse of the array is ",*a[::-1])
for t in range(0,len(a)//2):
    temp = a[t]
    a[t] = a[len(a) - t - 1]
    a[len(a) - t- 1] = temp
print(a)
