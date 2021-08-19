def insertionSort(arr):
    for i in range(0,len(arr)):
        key=arr[i]

        j=i-1
        while j >=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key

arr=[5,48,6,94,0,12]
insertionSort(arr)
print(arr)
