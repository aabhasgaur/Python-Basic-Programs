def selection(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[min]>arr[j]):
                min=j

        arr[i],arr[min]=arr[min],arr[i]

arr=[64,2,89,1,15]
selection(arr)
print("Sorted arrays is",arr)
