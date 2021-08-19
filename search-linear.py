def search(arr,n,x):
    for i in range(0,n):
        if (arr[i]==x):
            return i
    return -1

arr=[1,2,5,9,11,22,597]
x=11

result=search(arr,len(arr),x)
if result!=-1:
    print("Element is at location",result)
else:
    print("Element is not in array.")
