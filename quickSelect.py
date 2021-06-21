import random

def partition(arr):
    pivot = arr[0]
    i = 1
    for j in range(1, len(arr)):
        if arr[j]<pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr = arr[1:i] + [pivot] + arr[i:]
    return arr, i-1

def quickSelect(arr, i, n):
    if n > 1:
        pivot = random.randint(0, n-1)
        arr[0], arr[pivot] = arr[pivot], arr[0]
        arr, x = partition(arr)
        if x==i:
            return arr[x]
        elif x>i:
            return quickSelect(arr[:x], i, x)
        else:
            return quickSelect(arr[x+1:], i-x-1, n-x-1)
    return arr[0]