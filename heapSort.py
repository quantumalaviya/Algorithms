def maxHeapSort(arr):
    def bubbleDown(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
                
        if l < n and arr[largest] < arr[l]:
            largest = l
         
        if r < n and arr[largest] < arr[r]:
            largest = r
         
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] 
            bubbleDown(arr, n, largest)
                
    def heapSort(arr):
        n = len(arr)
        
        for i in range(n//2 - 1, -1, -1):
            bubbleDown(arr, n, i)
        
        print("MaxHeap: "+ str(arr))
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            bubbleDown(arr, i, 0)
    
    heapSort(arr)
    
arr = [1,2,7,2,5,1,4,9,10]
maxHeapSort(arr)
print(arr)

def minHeapSort(arr):
    def bubbleDown(arr, n, i):
        lowest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and arr[lowest] > arr[l]:
            lowest = l
        
        if r < n and arr[lowest] > arr[r]:
            lowest = r
            
        if lowest != i:
            arr[i], arr[lowest] = arr[lowest], arr[i]
            bubbleDown(arr, n , lowest)
    
    def heapSort(arr):
        n = len(arr)
        
        for i in range(n//2 - 1, -1, -1):
            bubbleDown(arr, n, i)
        
        print("MinHeap: " + str(arr))
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            bubbleDown(arr, i, 0)
        arr = arr.reverse()
    
    heapSort(arr)
            
arr = [1,2,7,2,5,1,4,9,10]
minHeapSort(arr)
print(arr)
