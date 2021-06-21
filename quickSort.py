import random

def partition(arr):
    pivot = arr[0]
    i = 1
    for j in range(1, len(arr)):
        if arr[j]<=pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    
    arr = arr[1:i] + [pivot] + arr[i:]
    return arr, i-1

def quickSort(arr):
    if len(arr)>1:
        pivot = random.randint(0, len(arr)-1)
        arr[0], arr[pivot] = arr[pivot], arr[0] 
        arr, i = partition(arr)
        return quickSort(arr[:i]) + [arr[i]] + quickSort(arr[i+1:])
    return arr


arr = [1,2,7,2,5,1,4,9,10]
print(quickSort(arr))