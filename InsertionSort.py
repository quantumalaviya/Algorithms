def insertionSort(arr): 
    for i in range(1, len(arr)): 
        og = arr[i] 
        j = i-1
        while j >= 0 and og < arr[j] : 
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j+1] = og
    return arr
  
def selectionSort(arr):
    for i in range(len(arr)): 
        min = i 
        for j in range(i+1, len(arr)): 
            if arr[min] > arr[j]: 
                min = j 
                    
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [1,2,7,2,5,1,4,9,10]
print(insertionSort(arr))
arr = [1,2,7,2,5,1,4,9,10]
print(selectionSort(arr))