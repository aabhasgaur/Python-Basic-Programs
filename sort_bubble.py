def bubbleSort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
#this is done to input the array

#n=int(input("Enter the size of array: "))
#a=[]
#for i in range(n):
#    element=int(input())
#    a.append(element)


a=[30,5,45,1,10,7]
bubbleSort(a)
print(a)
