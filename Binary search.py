def binaryIter(arr, val):
    i = 0
    j = len(arr) - 1
    while (i<=j):
        mid = (j+i)//2
        if val > arr[mid]:
            i = mid+1
        elif val < arr[mid]:
            j = mid-1
        else:
            return mid
    
    return False

def binaryRec(arr, val, i, j):
    if i<=j:
        mid = (i+j)//2
        if val > arr[mid]:
            return binaryRec(arr, val, mid+1, j)
        elif val < arr[mid]:
            return binaryRec(arr, val, i, mid-1)
        else:
            return mid
    else:
        return False

arr = [1,6,10,18,112]

print(binaryIter(arr, 18))
print(binaryRec(arr, 11, 0, len(arr)-1))